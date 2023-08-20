import socket

# 서버 호스트와 포트 번호
host = 'localhost'  # 또는 원하는 IP 주소
port = 12345

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 소켓 바인딩
server_socket.bind((host, port))

# 클라이언트 연결 대기
server_socket.listen(1)
print("서버가 클라이언트 연결을 대기 중입니다.")

# 클라이언트 연결 수락
client_socket, client_address = server_socket.accept()
print("클라이언트가 연결되었습니다:", client_address)

# 클라이언트로부터 메시지 수신 및 출력
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print("수신한 메시지:", data)

    # 클라이언트에게 응답 보내기
    response = "서버에서 보내는 응답: 메시지를 받았습니다."
    client_socket.send(response.encode())
pyth
# 연결 종료
client_socket.close()
server_socket.close()