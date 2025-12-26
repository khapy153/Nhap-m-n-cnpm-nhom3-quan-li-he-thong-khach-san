import sqlite3
import tkinter as tk
from tkinter import messagebox

# ================== DATABASE ==================
def init_db():
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT,
        room TEXT,
        status TEXT
    )
    """)

    # tạo sẵn admin
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin','123','admin')")
    conn.commit()
    conn.close()

# ================== LOGIN ==================
current_user = {"username": None, "role": None}

def login():
    u = entry_user.get()
    p = entry_pass.get()

    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT role FROM users WHERE username=? AND password=?",
        (u, p)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        current_user["username"] = u
        current_user["role"] = user[0]
        login_frame.pack_forget()
        main_frame.pack()
        load_orders()
    else:
        messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu")

# ================== ORDERS ==================
def load_orders():
    listbox.delete(0, tk.END)
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    for o in cursor.fetchall():
        listbox.insert(tk.END, f"{o[0]} | {o[1]} | Phòng {o[2]} | {o[3]}")
    conn.close()

def update_status(status):
    if current_user["role"] != "admin":
        messagebox.showerror("Từ chối", "Chỉ ADMIN mới có quyền")
        return

    selected = listbox.curselection()
    if not selected:
        return

    order_id = listbox.get(selected).split(" | ")[0]
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE orders SET status=? WHERE id=?",
        (status, order_id)
    )
    conn.commit()
    conn.close()
    load_orders()

# ================== GUI ==================
init_db()
root = tk.Tk()
root.title("Quản lý duyệt phòng")

# ---- Login Frame ----
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(login_frame, text="Username").grid(row=0, column=0)
entry_user = tk.Entry(login_frame)
entry_user.grid(row=0, column=1)

tk.Label(login_frame, text="Password").grid(row=1, column=0)
entry_pass = tk.Entry(login_frame, show="*")
entry_pass.grid(row=1, column=1)

tk.Button(login_frame, text="Đăng nhập", command=login).grid(row=2, columnspan=2)

# ---- Main Frame ----
main_frame = tk.Frame(root)

listbox = tk.Listbox(main_frame, width=50)
listbox.pack(pady=10)

tk.Button(main_frame, text="Duyệt phòng",
          command=lambda: update_status("Đã duyệt")).pack(side=tk.LEFT, padx=5)

tk.Button(main_frame, text="Từ chối phòng",
          command=lambda: update_status("Từ chối")).pack(side=tk.LEFT, padx=5)

root.mainloop()
