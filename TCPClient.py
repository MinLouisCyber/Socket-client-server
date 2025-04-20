from socket import *  # Import tất cả các thành phần từ thư viện socket

serverName = "127.0.0.1"  # Địa chỉ IP của server (localhost)
serverPort = 1200         # Cổng mà server đang lắng nghe

# Tạo socket TCP cho client (AF_INET: dùng IPv4, SOCK_STREAM: giao thức TCP)
clientSocket = socket(AF_INET, SOCK_STREAM)

# Kết nối đến server qua địa chỉ IP và cổng đã chỉ định
clientSocket.connect((serverName, serverPort))

# Nhập một chuỗi từ bàn phím (giả sử là chữ thường)
sentence = input("Input lowercase sentence: ")

# Gửi chuỗi đã nhập tới server (mã hoá thành byte trước khi gửi)
clientSocket.send(sentence.encode())

# Nhận phản hồi từ server (giải mã từ byte về chuỗi)
modifiedSentence = clientSocket.recv(1024).decode()

# In ra kết quả nhận được từ server
print("From Server:", modifiedSentence)

# Đóng kết nối socket
clientSocket.close()
