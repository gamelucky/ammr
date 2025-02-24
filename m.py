pip install requests
import unidecode, concurrent.futures, string, random, requests
from fake_headers import Headers;
from colorama import Fore, Style

# Setting
ma_moi = "V0C6lW" # Nhập mã mời của bạn vào đây



_header = Headers(
    headers=False  # generate misc headers
)



ho = [ "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Vũ", "Võ", "Phan", "Trương", "Bùi", "Đặng", "Đỗ", "Ngô", "Hồ", "Dương", "Đinh", "Trịnh", "Lý"]

ten_dem_nam = ["Văn", "Hữu", "Đình", "Công", "Xuân", "Nhật", "Minh", "Thế", "Trung", "Tấn", "Phúc", "Gia", "Đức", "Bảo", "Thanh", "Hoàng", "Hải"]
ten_dem_nu = ["Thị", "Ngọc", "Bích", "Như", "Diễm", "Hồng", "Kim", "Thanh", "Tuyết", "Cẩm", "Mai", "Phương", "Minh", "Xuân", "Ánh", "Quỳnh"]

nam = ["Huy", "Khang", "Bảo", "Minh", "Phúc", "Anh", "Khoa", "Phát", "Đạt", "Khôi", "Long", "Nam", "Duy", "Quân", "Kiệt", "Thịnh", "Tuấn", "Hưng", "Hoàng", "Hiếu", "Nhân", "Trí", "Tài", "Phong", "Nguyên", "An", "Phú", "Thành", "Đức", "Dũng", "Lộc", "Khánh", "Vinh", "Tiến", "Nghĩa", "Thiện", "Hào", "Hải", "Đăng", "Quang", "Lâm", "Nhật", "Trung", "Thắng", "Tú", "Hùng", "Tâm", "Sang", "Sơn", "Thái", "Cường", "Vũ", "Toàn", "Ân", "Thuận", "Bình", "Trường", "Danh", "Kiên", "Phước", "Thiên", "Tân", "Việt", "Khải", "Tín", "Dương", "Tùng", "Quý", "Hậu", "Trọng", "Triết", "Luân", "Phương", "Quốc", "Thông", "Khiêm", "Hòa", "Thanh", "Tường", "Kha", "Vỹ", "Bách", "Khanh", "Mạnh", "Lợi", "Đại", "Hiệp", "Đông", "Nhựt", "Giang", "Kỳ", "Phi", "Tấn", "Văn", "Vương", "Công", "Hiển", "Linh", "Ngọc", "Vĩ"]
nu = ["Anh", "Vy", "Ngọc", "Nhi", "Hân", "Thư", "Linh", "Như", "Ngân", "Phương", "Thảo", "My", "Trân", "Quỳnh", "Nghi", "Trang", "Trâm", "An", "Thy", "Châu", "Trúc", "Uyên", "Yến", "Ý", "Tiên", "Mai", "Hà", "Vân", "Nguyên", "Hương", "Quyên", "Duyên", "Kim", "Trinh", "Thanh", "Tuyền", "Hằng", "Dương", "Chi", "Giang", "Tâm", "Lam", "Tú", "Ánh", "Hiền", "Khánh", "Minh", "Huyền", "Thùy", "Vi", "Ly", "Dung", "Nhung", "Phúc", "Lan", "Phụng", "Ân", "Thi", "Khanh", "Kỳ", "Nga", "Tường", "Thúy", "Mỹ", "Hoa", "Tuyết", "Lâm", "Thủy", "Đan", "Hạnh", "Xuân", "Oanh", "Mẫn", "Khuê", "Diệp", "Thương", "Nhiên", "Băng", "Hồng", "Bình", "Loan", "Thơ", "Phượng", "Mi", "Nhã", "Nguyệt", "Bích", "Đào", "Diễm", "Kiều", "Hiếu", "Di", "Liên", "Trà", "Tuệ", "Thắm", "Diệu", "Quân", "Nhàn", "Doanh"]

def random_name(gender):
    ten = nam if gender == 1 else nu
    ten_dem = ten_dem_nam if gender == 1 else ten_dem_nu
    return f"{random.choice(ho)} {random.choice(ten_dem)} {random.choice(ten)}"

def random_email(name):
    name = unidecode.unidecode(name.lower().replace(" ", ""))
    number = random.randint(1000, 999999)
    special_char = random.choice(string.ascii_lowercase + string.digits)
    return f"{name}{number}{special_char}@gmail.com"

def random_password():
    length = random.randint(8, 12)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def random_phone():
    return "09" + "".join(str(random.randint(0, 9)) for _ in range(8))
# Generate data



def create(number):
    request_cout = 0;
    for _ in range(number):
        header = _header.generate()
        gender = random.choice([0, 1])
        full_name = random_name(gender)
        gmail = random_email(full_name)

        json_data = {
            "email": gmail,
            "referral_code": ma_moi,
            "password": random_password(),
            "name": full_name,
            "mobile": random_phone(),
            "province_id": 30,
            "district_id": 297,
            "ward_id": 10999,
            "gender": gender,
        }
        response = requests.post('https://api.greenfy.vn/api/v1/register', headers=header, json=json_data)
        if response.status_code == 200:
            request_cout += 1;
            print(Fore.GREEN + "✅ " + str(request_cout) + ". " + json_data["name"] + Style.RESET_ALL)

        else:
            print(Fore.RED + f"❌ Lỗi! Status code: {response.status_code}" + Style.RESET_ALL)

n = 1000  # Chỉnh số lần chạy theo nhu cầu
num_threads = 100  # Số luồng

# Chia đều số lần chạy cho từng luồng
tasks = [n // num_threads] * num_threads
for i in range(n % num_threads):  # Nếu n không chia hết, phân bổ thêm cho một số luồng
    tasks[i] += 1



# Chạy đa luồng
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(create, tasks)
