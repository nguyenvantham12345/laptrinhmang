import requests

url = 'http://127.0.0.1:5000/getStockPrice'

# Nhập mã chứng khoán bạn muốn gửi
stock_code = input("Enter the stock code: ")

# Gửi mã chứng khoán lên server
data = {'stockCode': stock_code}

response = requests.post(url, json=data)

# In ra giá trị nhận được từ server
if response.status_code == 200:
    stock_info = response.json()
    print(f"Stock Code: {stock_info['stockCode']}, Price: {stock_info['price']}")
else:
    print(f"Error: {response.json().get('error')}")