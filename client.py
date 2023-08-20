import  socket

# 서버 호스트와 포트 번호
host = 'localhost'  # 또는 서버의 IP 주소
port = 12345

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
client_socket.connect((host, port))
print("서버에 연결되었습니다.")

# 서버로 메시지 전송
message = "안녕, 서버!"
client_socket.send(message.encode())

# 서버로부터 응답 수신 및 출력
response = client_socket.recv(1024).decode()
print("서버로부터 받은 응답:", response)

# 연결 종료
client_socket.close()