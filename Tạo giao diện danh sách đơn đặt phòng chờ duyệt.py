import tkinter as tk
from tkinter import ttk, messagebox

# ================== DỮ LIỆU GIẢ LẬP ==================
bookings = [
    ("DP001", "Nguyễn Văn A", "Phòng 101", "01/01/2026", "03/01/2026", "Chờ duyệt"),
    ("DP002", "Trần Thị B", "Phòng 202", "02/01/2026", "04/01/2026", "Chờ duyệt"),
    ("DP003", "Lê Văn C", "Phòng 303", "05/01/2026", "06/01/2026", "Chờ duyệt")
]

# ================== DUYỆT ĐƠN ==================
def approve_booking():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn đơn đặt phòng")
        return

    tree.set(selected, column="status", value="Đã duyệt")
    messagebox.showinfo("Thành công", "Đơn đặt phòng đã được duyệt")

# ================== TỪ CHỐI ĐƠN ==================
def reject_booking():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn đơn đặt phòng")
        return

    tree.set(selected, column="status", value="Từ chối")
    messagebox.showinfo("Thông báo", "Đơn đặt phòng đã bị từ chối")

# ================== CỬA SỔ CHÍNH ==================
root = tk.Tk()
root.title("Danh sách đơn đặt phòng chờ duyệt")
root.geometry("800x400")
root.resizable(False, False)

# ================== TIÊU ĐỀ ==================
title = tk.Label(root, text="DANH SÁCH ĐƠN ĐẶT PHÒNG CHỜ DUYỆT",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

# ================== BẢNG DANH SÁCH ==================
columns = ("id", "customer", "room", "checkin", "checkout", "status")

tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

tree.heading("id", text="Mã đơn")
tree.heading("customer", text="Khách hàng")
tree.heading("room", text="Phòng")
tree.heading("checkin", text="Ngày nhận")
tree.heading("checkout", text="Ngày trả")
tree.heading("status", text="Trạng thái")

tree.column("id", width=80, anchor="center")
tree.column("customer", width=150)
tree.column("room", width=100, anchor="center")
tree.column("checkin", width=100, anchor="center")
tree.column("checkout", width=100, anchor="center")
tree.column("status", width=100, anchor="center")

for booking in bookings:
    tree.insert("", tk.END, values=booking)

tree.pack(pady=10)

# ================== NÚT CHỨC NĂNG ==================
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_approve = tk.Button(button_frame, text="Duyệt đơn",
                        width=15, command=approve_booking)
btn_approve.pack(side="left", padx=10)

btn_reject = tk.Button(button_frame, text="Từ chối đơn",
                       width=15, command=reject_booking)
btn_reject.pack(side="left", padx=10)

root.mainloop()
