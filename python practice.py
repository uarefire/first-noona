from scapy.all import sniff, TCP, IP, get_if_list
from collections import defaultdict
from time import time

# 사용 가능한 인터페이스 목록 가져오기
interfaces = get_if_list()

# 사용자에게 인터페이스 선택하게 하기
print("Available interfaces:")
for i, iface in enumerate(interfaces):
    print(f"{i}. {iface}")

try:
    selection = int(input("Select interface by number: "))
    interface = interfaces[selection]
except (ValueError, IndexError):
    print("Invalid selection, using default interface.")
    interface = None  # None으로 설정하면 scapy가 기본 인터페이스를 사용합니다.

# 연결 시도를 추적하기 위한 자료구조
connection_attempts = defaultdict(int)
attempt_time = defaultdict(float)

# 탐지 조건 설정
MAX_ATTEMPTS = 5
TIME_WINDOW = 60

def detect_ssh(packet):
    if TCP in packet and packet[TCP].dport == 22:
        source_ip = packet[IP].src
        current_time = time()

        # 이전 연결 시도와 시간 차이 계산
        time_difference = current_time - attempt_time.get(source_ip, 0)

        # 시간 창을 벗어난 경우 카운터 초기화
        if time_difference > TIME_WINDOW:
            connection_attempts[source_ip] = 0

        # 연결 시도 카운터와 시간 업데이트
        connection_attempts[source_ip] += 1
        attempt_time[source_ip] = current_time

        # 허용된 연결 시도 횟수를 초과한 경우 경고
        if connection_attempts[source_ip] > MAX_ATTEMPTS:
            print("Potential SSH brute force attempt from {}".format(source_ip))
            connection_attempts[source_ip] = 0

# 인터페이스 및 필터 설정
filter_str = 'tcp and port 22'

# sniff 함수를 사용하여 패킷 캡쳐 시작
sniff(iface=interface, filter=filter_str, prn=detect_ssh)
