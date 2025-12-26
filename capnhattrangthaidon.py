import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    room TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()
def update_order_status(order_id, new_status):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE orders SET status = ? WHERE id = ?",
        (new_status, order_id)
    )

    conn.commit()
    conn.close()
# duyệt đơn ID = 1
update_order_status(1, "Đã duyệt")

# từ chối đơn ID = 2
update_order_status(2, "Từ chối")
conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM orders")
for order in cursor.fetchall():
    print(order)

conn.close()
