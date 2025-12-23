from tkinter import simpledialog, messagebox

def reject_booking():
    selected_item = tree.focus()

    if not selected_item:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn đơn đặt phòng")
        return

    current_status = tree.set(selected_item, "status")

    # Chỉ cho từ chối đơn chờ duyệt
    if current_status != "Chờ duyệt":
        messagebox.showerror(
            "Không hợp lệ",
            "Chỉ có thể từ chối đơn đang ở trạng thái 'Chờ duyệt'"
        )
        return

    # Nhập lý do từ chối
    reason = simpledialog.askstring(
        "Từ chối đơn",
        "Nhập lý do từ chối:"
    )

    if reason is None or reason.strip() == "":
        messagebox.showwarning(
            "Thiếu thông tin",
            "Vui lòng nhập lý do từ chối"
        )
        return

    # Cập nhật trạng thái và lý do
    tree.set(selected_item, "status", "Từ chối")
    tree.set(selected_item, "reason", reason)

    messagebox.showinfo("Hoàn tất", "Đơn đặt phòng đã bị từ chối")
