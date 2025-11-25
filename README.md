# Nhap-m-n-cnpm-nhom3-quan-li-he-thong-khach-san
Một ứng dụng quản lí he thong khach san đơn giản bằng Python.
from utils import calculate_sum

def run_project(): """Hàm chạy logic chính của dự án.""" a = 5 b = 10 result = calculate_sum(a, b) print(f"Kết quả của {a} + {b} là: {result}")

if name == "main": run_project() from flask import Flask, request

app = Flask(name)

@app.route("/") def welcome(): # Lấy tên khách nếu URL có ?name=... guest_name = request.args.get("name", "Quý khách")
