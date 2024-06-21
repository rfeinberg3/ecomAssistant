import socket

def receive_message():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(("", 8080))
	sock.listen(1)
	conn, addr = sock.accept()
	msg = conn.recv(1024).decode()
	conn.close()
	return msg

if __name__ == '__main__':
	print("Received Message:", f"\"{receive_message()}\"")
