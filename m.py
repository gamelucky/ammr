import time
import random
import string
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ✅ Hàm tạo email tạm thời từ 1secmail
def generate_temp_email():
    domain = "1secmail.com"
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@{domain}", username

# ✅ Hàm lấy mã xác minh từ email
def get_verification_code(email_username):
    api_url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={email_username}&domain=1secmail.com"
    for _ in range(30):  # Chờ tối đa 30 giây
        response = requests.get(api_url).json()
        if response:
            email_id = response[0]['id']
            email_content_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={email_username}&domain=1secmail.com&id={email_id}"
            email_content = requests.get(email_content_url).json()
            if 'body' in email_content:
                import re
                match = re.search(r'(\d{6})', email_content['body'])  # Tìm mã 6 chữ số
                if match:
                    return match.group(1)
        time.sleep(3)
    return None

# ✅ Cấu hình trình duyệt Selenium
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ✅ Truy cập link giới thiệu Greenfy
referral_link = "https://app.greenfy.vn/sign-in?gfy=V0C6lW"
driver.get(referral_link)

# ✅ Nhấn vào nút "Sign Up" nếu cần
try:
    sign_up_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign Up')]"))
    )
    sign_up_button.click()
except:
    print("Không cần nhấn Sign Up, trang đăng ký đã mở sẵn.")

# ✅ Tạo email ngẫu nhiên và nhập vào form đăng ký
email, email_username = generate_temp_email()
password = "YourSecurePass123"

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Email"))).send_keys(email)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "confirm_password"))).send_keys(password)

# ✅ Đồng ý điều khoản và nhấn nút đăng ký
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "terms"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign Up')]"))).click()

time.sleep(5)  # Đợi chuyển trang

# ✅ Lấy mã xác minh từ email
verification_code = get_verification_code(email_username)
if verification_code:
    print(f"Mã xác minh: {verification_code}")
    # ✅ Nhập mã xác minh vào form
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "verification_code"))).send_keys(verification_code)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Verify')]"))).click()
    print("✅ Tài khoản đã được xác minh!")
else:
    print("❌ Không nhận được email xác minh!")

# ✅ Giữ trình duyệt mở
input("Nhấn Enter để thoát...")
