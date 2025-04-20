import java.io.*;
import java.net.*;

class TCPClient {
    public static void main(String argv[]) throws Exception {
        String sentence;              // Biến lưu chuỗi nhập từ người dùng
        String modifiedSentence;      // Biến lưu chuỗi phản hồi từ server

        // Tạo bộ đọc dữ liệu từ bàn phím
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));

        // Tạo socket client, kết nối đến server tại địa chỉ IP 127.0.0.1, cổng 6789
        Socket clientSocket = new Socket("127.0.0.1", 6789);

        // Tạo luồng gửi dữ liệu tới server
        DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());

        // Tạo luồng nhận dữ liệu từ server
        BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

        // Yêu cầu người dùng nhập chuỗi để gửi đến server
        System.out.print("Enter string to send to server: ");
        sentence = inFromUser.readLine(); // Đọc chuỗi người dùng nhập từ bàn phím

        // Gửi chuỗi tới server, kèm theo ký tự xuống dòng '\n' để server biết đã hết dòng
        outToServer.writeBytes(sentence + '\n');

        // Nhận phản hồi từ server
        modifiedSentence = inFromServer.readLine();

        // In chuỗi phản hồi từ server ra màn hình
        System.out.println("FROM SERVER: " + modifiedSentence);

        // Đóng kết nối socket
        clientSocket.close();
    }
}
