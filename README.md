# Nhap-m-n-cnpm-nhom3-quan-li-he-thong-khach-san
Một ứng dụng quản lí he thong khach san đơn giản bằng Python.
rooms = {
    101: {"type": "Single", "price": 500000, "booked": False},
    102: {"type": "Double", "price": 750000, "booked": False},
    201: {"type": "Deluxe", "price": 1200000, "booked": False}
}

bookings = []

def show_rooms():
    print("\n--- DANH SÁCH PHÒNG ---")
    for rid, info in rooms.items():
        status = "Đã đặt" if info["booked"] else "Còn trống"
        print(f"Phòng {rid} | {info['type']} | {info['price']} VNĐ | {status}")
    print("-----------------------")

def book_room():
    show_rooms()
    rid = int(input("Nhập số phòng muốn đặt: "))
    if rid not in rooms:
        print("Phòng không tồn tại.")
        return
    if rooms[rid]["booked"]:
        print("Phòng đã có người đặt.")
        return
    name = input("Nhập tên khách: ")
    days = int(input("Số ngày ở: "))
    total = rooms[rid]["price"] * days
    bookings.append({"room": rid, "guest": name, "days": days, "total": total})
    rooms[rid]["booked"] = True
    print(f"✅ Đặt phòng thành công! Tổng tiền: {total} VNĐ")

def show_bookings():
    print("\n--- DANH SÁCH ĐẶT PHÒNG ---")
    if not bookings:
        print("Chưa có đặt phòng nào.")
        return
    for b in bookings:
        print(f"Khách: {b['guest']} | Phòng: {b['room']} | {b['days']} ngày | Tổng: {b['total']} VNĐ")

def cancel_booking():
    name = input("Nhập tên khách để hủy đặt phòng: ")
    for b in bookings:
        if b["guest"] == name:
            rooms[b["room"]]["booked"] = False
            bookings.remove(b)
            print("❌ Đã hủy đặt phòng.")
            return
    print("Không tìm thấy đặt phòng của khách này.")

def main():
    while True:
        print("""
=== HỆ THỐNG ĐẶT PHÒNG KHÁCH SẠN ===
1. Xem phòng
2. Đặt phòng
3. Xem đặt phòng
4. Hủy đặt phòng
5. Thoát
""")
        choice = input("Chọn (1-5): ")
        if choice == "1":
            show_rooms()
        elif choice == "2":
            book_room()
        elif choice == "3":
            show_bookings()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()