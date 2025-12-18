# US-001: Đăng ký tài khoản

def register(users):
    print("\n--- ĐĂNG KÝ TÀI KHOẢN ---")
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")

    for user in users:
        if user["username"] == username:
            print("❌ Tài khoản đã tồn tại.")
            return False

    users.append({
        "username": username,
        "password": password
    })

    print("✅ Đăng ký thành công!")
    return True
