# Dữ liệu giả lập
rooms = {
    "P101": {"trang_thai": "Đang ở"},
    "P102": {"trang_thai": "Trống"}
}

bookings = {
    "DK01": {"phong": "P101", "trang_thai": "Đã đăng ký"}
}

def huy_dang_ky(ma_dk):
    if ma_dk not in bookings:
        print("Không tìm thấy đăng ký")
        return

    phong = bookings[ma_dk]["phong"]

    # Cập nhật trạng thái đăng ký
    bookings[ma_dk]["trang_thai"] = "Đã hủy"

    # Cập nhật trạng thái phòng
    rooms[phong]["trang_thai"] = "Trống"

    print(f"Hủy đăng ký {ma_dk} thành công")
    print(f"Phòng {phong} đã chuyển về trạng thái Trống")

# Test chức năng
huy_dang_ky("DK01")
