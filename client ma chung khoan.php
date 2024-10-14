<!DOCTYPE html>
<html>
<head>
    <title>Ứng dụng lấy giá chứng khoán</title>
</head>
<body>
    <h1>Nhập mã chứng khoán để lấy giá hiện tại</h1>
    <form method="POST" action="server.php">
        <label for="stock_code">Mã chứng khoán:</label>
        <input type="text" id="stock_code" name="stock_code" required>
        <button type="submit">Lấy giá</button>
    </form>
</body>
</html>
