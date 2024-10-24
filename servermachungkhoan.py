from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Giả sử có API của iBoard để lấy thông tin giá trị chứng khoán
API_URL = 'https://iboard.ssi.com.vn/api/stockPrice/'


@app.route('/getStockPrice', methods=['POST'])
def get_stock_price():
    data = request.get_json()
    stock_code = data.get('stockCode')

    if not stock_code:
        return jsonify({'error': 'Stock code is required'}), 400

    try:
        # Thực hiện yêu cầu đến API của iBoard SSI
        response = requests.get(f'{API_URL}{stock_code}')

        # Kiểm tra xem có nhận được dữ liệu từ API hay không
        if response.status_code == 200:
            stock_data = response.json()

            # Trả về dữ liệu giá trị chứng khoán
            return jsonify({
                'stockCode': stock_code,
                'price': stock_data.get('price')  # Giả sử trường giá trị là 'price'
            })
        else:
            return jsonify({'error': 'Stock data not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
