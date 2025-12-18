# US-002: Đăng nhập

def login(users):
    print("\n--- ĐĂNG NHẬP ---")
    username = input("Tên đăng nhập: ")
    password = input("Mật khẩu: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("✅ Đăng nhập thành công!")
            return user

    print("❌ Sai tên đăng nhập hoặc mật khẩu.")
    return None
