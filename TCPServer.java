import java.io.*;
import java.net.*;

class TCPServer {

    public static void main(String argv[]) throws Exception {
        String clientSentence;         // Biến lưu chuỗi nhận từ client
        String capitalizedSentence;   // Biến lưu chuỗi đã chuyển thành chữ in hoa để gửi lại client

        // Tạo socket server lắng nghe tại cổng 6789
        ServerSocket welcomeSocket = new ServerSocket(6789);

        System.out.println("Server is running and waiting for connection...");

        while (true) {
            // Chấp nhận kết nối từ client (chặn cho đến khi có client kết nối)
            Socket connectionSocket = welcomeSocket.accept();

            // Tạo luồng để đọc dữ liệu từ client
            BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));

            // Tạo luồng để gửi dữ liệu về cho client
            DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());

            // Đọc chuỗi gửi từ client
            clientSentence = inFromClient.readLine();
            System.out.println("Received: " + clientSentence); // In chuỗi đã nhận ra màn hình

            // Chuyển chuỗi thành chữ in hoa và thêm dấu xuống dòng
            capitalizedSentence = clientSentence.toUpperCase() + '\n';

            // Gửi chuỗi đã xử lý lại cho client
            outToClient.writeBytes(capitalizedSentence);
        }
    }
}
