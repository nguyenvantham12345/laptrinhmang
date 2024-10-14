<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Nhận mã chứng khoán từ client
    $stock_code = $_POST['stock_code'];
    
    // Tạo URL cho request (giả sử sử dụng một API công khai để lấy dữ liệu chứng khoán)
    $url = "https://api.example.com/stock/$stock_code";
    
    // Khởi tạo cURL
    $ch = curl_init();
    
    // Thiết lập các tuỳ chọn cho cURL
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
    // Thực hiện yêu cầu
    $response = curl_exec($ch);
    
    // Kiểm tra lỗi
    if (curl_errno($ch)) {
        echo 'Lỗi cURL: ' . curl_error($ch);
    } else {
        // Xử lý và gửi lại kết quả cho client
        $data = json_decode($response, true);
        
        if (isset($data['current_price'])) {
            echo json_encode([
                'success' => true,
                'stock_code' => $stock_code,
                'current_price' => $data['current_price']
            ]);
        } else {
            echo json_encode(['success' => false, 'message' => 'Không tìm thấy dữ liệu']);
        }
    }
    
    // Đóng cURL
    curl_close($ch);
} else {
    echo json_encode(['success' => false, 'message' => 'Chỉ chấp nhận POST request']);
}
