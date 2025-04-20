from socket import *  # Import tất cả các thành phần từ thư viện socket

serverPort = 1200  # Cổng mà server sẽ lắng nghe kết nối

# Tạo socket TCP cho server (AF_INET: dùng IPv4, SOCK_STREAM: giao thức TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Gán socket với địa chỉ IP ('' nghĩa là tất cả các IP trên máy) và cổng chỉ định
serverSocket.bind(('', serverPort))

# Server bắt đầu lắng nghe kết nối, tối đa 1 kết nối đang chờ
serverSocket.listen(1)

print('The server is ready to receive')  # In ra thông báo khi server sẵn sàng

# Vòng lặp vô hạn để server luôn sẵn sàng xử lý client
while True:
    # Chấp nhận kết nối từ client, trả về socket kết nối và địa chỉ client
    connectionSocket, addr = serverSocket.accept()

    # Nhận dữ liệu từ client (tối đa 1024 byte), sau đó giải mã từ byte về chuỗi
    sentence = connectionSocket.recv(1024).decode()

    # Chuyển toàn bộ chuỗi thành chữ in hoa
    capitalizedSentence = sentence.upper()

    # Gửi chuỗi đã xử lý (chữ in hoa) lại cho client (mã hoá thành byte)
    connectionSocket.send(capitalizedSentence.encode())

    # Đóng kết nối với client hiện tại
    connectionSocket.close()
