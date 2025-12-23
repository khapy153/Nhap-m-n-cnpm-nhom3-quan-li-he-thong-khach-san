<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Hủy đơn</title>
</head>
<body>

<button onclick="xacNhanHuy('DK01')">Hủy đăng ký</button>

<script>
function xacNhanHuy(maDon) {
    if (confirm("Bạn có chắc chắn muốn hủy đơn " + maDon + " không?")) {
        // Gửi yêu cầu hủy (giả lập)
        alert("Đã hủy đơn " + maDon + " thành công");
        // window.location.href = "/huy-don?ma=" + maDon;
    }
}
</script>

</body>
</html>
