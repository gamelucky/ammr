from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Thiết lập các tùy chọn để mở Chrome ở chế độ ẩn danh
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Chế độ ẩn danh

# Khởi tạo Chrome WebDriver với các tùy chọn
driver = webdriver.Chrome(executable_path="path_to_chromedriver", options=chrome_options)  # Cập nhật đường dẫn đến chromedriver của bạn

# Bước 1: Mở URL
driver.get("https://cloudminecrypto.com/?invite_code=nzZ1JRlmAx2kV5a8")
print("Bước 1: Mở trang web thành công!")

# Bước 2: Chờ để trang tải và click vào Web App
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "web-app-button")))  # Cập nhật ID chính xác nếu cần
web_app_button = driver.find_element(By.ID, "web-app-button")
web_app_button.click()
print("Bước 2: Đã click vào Web App!")

# Bước 3: Đợi 30 giây
time.sleep(30)
print("Bước 3: Đã chờ 30 giây!")

# Bước 4: Nhấn "Confirm"
confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]")  # Cập nhật XPath nếu cần
confirm_button.click()
print("Bước 4: Đã nhấn 'Confirm'!")

# Bước 5: Nhấn "Skip" (có thể là các ngôn ngữ khác)
skip_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Skip')]")  # Cập nhật XPath nếu cần
skip_button.click()
print("Bước 5: Đã nhấn 'Skip'!")

# Bước 6: Đợi 10 giây và nhấn vào phần ngoài khung
time.sleep(10)
outside_frame = driver.find_element(By.XPATH, "//div[contains(@class, 'outside-frame-class')]")  # Cập nhật XPath của phần ngoài khung
outside_frame.click()
print("Bước 6: Đã nhấn vào phần ngoài khung!")

# Bước 7: Nhấn vào 8 giờ
while True:
    time.sleep(10)  # Đợi 10 giây
    eight_hours_button = driver.find_element(By.XPATH, "//button[contains(text(), '8 hours')]")  # Cập nhật XPath nếu cần
    eight_hours_button.click()
    print("Bước 7: Đã nhấn '8 hours'!")

    # Lặp lại mỗi 8 giờ
    time.sleep(8 * 60 * 60)  # Lặp lại sau 8 giờ (28800 giây)
