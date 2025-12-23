def approve_booking():
    selected_item = tree.focus()

    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn đơn đặt phòng")
        return

    current_status = tree.set(selected_item, "status")

    # Kiểm tra trạng thái
    if current_status != "Chờ duyệt":
        messagebox.showerror(
            "Không hợp lệ",
            "Chỉ có thể duyệt đơn đang ở trạng thái 'Chờ duyệt'"
        )
        return

    # Cập nhật trạng thái
    tree.set(selected_item, "status", "Đã duyệt")

    messagebox.showinfo("Thành công", "Đơn đặt phòng đã được duyệt")
