import tkinter as tk
from tkinter import messagebox

rooms = {"P101": {"ten":"Phòng 101","loai":"Đơn","gia":"300000","tt":"Trống"}}

def load():
    r = rooms.get(e_id.get())
    if not r: return messagebox.showerror("Lỗi","Không có phòng")
    for e,v in zip((e_ten,e_loai,e_gia,e_tt), r.values()):
        e.delete(0,tk.END); e.insert(0,v)

def save():
    if e_id.get() not in rooms:
        return messagebox.showerror("Lỗi","Không có phòng")
    rooms[e_id.get()] = {
        "ten":e_ten.get(),
        "loai":e_loai.get(),
        "gia":e_gia.get(),
        "tt":e_tt.get()
    }
    messagebox.showinfo("OK","Đã cập nhật")

root = tk.Tk()
root.title("Sửa phòng")

for i,t in enumerate(("Mã","Tên","Loại","Giá","Trạng thái")):
    tk.Label(root,text=t).grid(row=i,column=0)
    tk.Entry(root)

e_id = tk.Entry(root); e_id.grid(row=0,column=1)
e_ten = tk.Entry(root); e_ten.grid(row=1,column=1)
e_loai = tk.Entry(root); e_loai.grid(row=2,column=1)
e_gia = tk.Entry(root); e_gia.grid(row=3,column=1)
e_tt = tk.Entry(root); e_tt.grid(row=4,column=1)

tk.Button(root,text="Tải",command=load).grid(row=0,column=2)
tk.Button(root,text="Lưu",command=save).grid(row=5,column=1)

root.mainloop()
