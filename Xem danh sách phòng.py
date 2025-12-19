# ================================
# QUẢN LÝ DANH SÁCH PHÒNG (CONSOLE)
# ================================

rooms = [
    {"so_phong": "101", "loai": "Đơn", "gia": 500000, "tinh_trang": "Trống"},
    {"so_phong": "102", "loai": "Đôi", "gia": 800000, "tinh_trang": "Đã thuê"},
    {"so_phong": "201", "loai": "VIP", "gia": 1500000, "tinh_trang": "Trống"},
]

simulate_error = False  # đổi thành True để test lỗi kết nối


# -------------------------------
def hien_thi_danh_sach():
    print("\n===== DANH SÁCH PHÒNG =====")

    if simulate_error:
        print("❌ Lỗi kết nối dữ liệu!")
        return

    if len(rooms) == 0:
        print("⚠ Không có dữ liệu phòng!")
        return

    print("{:<10}{:<15}{:<15}{:<15}".format(
        "Số phòng", "Loại phòng", "Giá", "Tình trạng"
    ))

    for r in rooms:
        print("{:<10}{:<15}{:<15}{:<15}".format(
            r["so_phong"],
            r["loai"],
            f"{r['gia']:,}",
            r["tinh_trang"]
        ))


# -------------------------------
def lam_moi():
    print("\n🔄 Làm mới danh sách...")
    hien_thi_danh_sach()


# -------------------------------
def sua_phong():
    print("\n✏ Chức năng SỬA phòng (đang phát triển)")


def xoa_phong():
    print("\n🗑 Chức năng XÓA phòng (đang phát triển)")


def cap_nhat_trang_thai():
    print("\n🔄 Chức năng CẬP NHẬT TRẠNG THÁI (đang phát triển)")


# -------------------------------
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Hiển thị danh sách phòng")
        print("2. Làm mới danh sách")
        print("3. Sửa phòng")
        print("4. Xóa phòng")
        print("5. Cập nhật trạng thái phòng")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            hien_thi_danh_sach()
        elif choice == "2":
            lam_moi()
        elif choice == "3":
            sua_phong()
        elif choice == "4":
            xoa_phong()
        elif choice == "5":
            cap_nhat_trang_thai()
        elif choice == "0":
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


# -------------------------------
menu()