from socket import *  # Import tất cả các thành phần từ thư viện socket
import threading  # Import thư viện để xử lý đa luồng


# Hàm xử lý client riêng biệt trên mỗi luồng
def handle_client(connectionSocket, addr):
    print(f"Connected by {addr}")  # In ra địa chỉ IP của client khi kết nối thành công
    try:
        # Nhận dữ liệu từ client và giải mã
        sentence = connectionSocket.recv(1024).decode()

        # Xử lý: chuyển chuỗi sang chữ in hoa
        capitalizedSentence = sentence.upper()

        # Gửi lại dữ liệu đã xử lý cho client
        connectionSocket.send(capitalizedSentence.encode())
    except Exception as e:
        # In ra lỗi nếu có sự cố khi xử lý client
        print(f"Error handling client {addr}: {e}")
    finally:
        # Đảm bảo luôn đóng kết nối sau khi xử lý xong
        connectionSocket.close()
        print(f"Connection with {addr} closed")


# Thiết lập server socket
serverPort = 1200  # Cổng server lắng nghe
serverSocket = socket(AF_INET, SOCK_STREAM)  # Tạo socket TCP
serverSocket.bind(('', serverPort))  # Gán socket với IP và cổng
serverSocket.listen(1)  # Bắt đầu lắng nghe kết nối, tối đa 1 kết nối đang chờ

print('The server is ready to receive')  # Thông báo server đã sẵn sàng

# Vòng lặp vô hạn để server luôn chờ kết nối mới
while True:
    # Chấp nhận kết nối mới từ client
    connectionSocket, addr = serverSocket.accept()

    # Tạo và khởi động một luồng mới để xử lý client
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()
