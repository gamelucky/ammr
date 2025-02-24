
while 1>0:
    import requests, random, string

    def random_string(length, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choices(chars, k=length))

    def generate_email():
        return f"{random_string(8)}@{random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])}"

    def generate_phone():
        return random.choice(["076", "086", "096", "097", "098"]) + random_string(7, string.digits)

    def generate_name():
        return f"{random.choice(['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Đặng', 'Bùi', 'Võ'])} " \
               f"{random.choice(['Văn', 'Hữu', 'Thành', 'Đình', 'Hải', 'Thái', 'Minh'])} " \
               f"{random.choice(['An', 'Bảo', 'Duy', 'Hiếu', 'Nam', 'Sơn', 'Tuấn', 'Thịnh'])}"

    payload = {
        "email": generate_email(), "name": generate_name(), "mobile": generate_phone(),
        "password": random_string(random.randint(8, 12), string.ascii_letters + string.digits),
        "gender": random.choice([0, 1]), "province_id": 24, "district_id": 218, "ward_id": 7504,
        "referral_code": V0C6lW
    }

    headers = {
        "accept": "application/json", "content-type": "application/json",
        "origin": "https://app.greenfy.vn", "referer": "https://app.greenfy.vn/",
        "user-agent": "Mozilla/5.0", "x-requested-with": "XMLHttpRequest"
    }

    response = requests.post("https://api.greenfy.vn/api/v1/register", json=payload, headers=headers)
    print(f"✅ Tạo tài khoản thành công!\n- {payload}" if response.status_code == 200 else f"❌ Lỗi: {response.text}")
