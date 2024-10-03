def menu():
    print("=== MENU ===")
    print("1.Xem danh sách nhận viên")
    print("2.Xóa nhân viên")
    print("3.Sửa nhân viên")
    print("4.Thêm mới  nhân viên")
    print("0. Thoát")

while True:
    menu()
    choice = input("Chọn một tùy chọn (0 để thoát): ")

    if choice == '1':
        print("Bạn đã chọn Tùy chọn 1.")
    elif choice == '2':
        print("Bạn đã chọn Tùy chọn 2.")
    elif choice == '3':
        print("Bạn đã chọn Tùy chọn 3.")
    elif choice == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")