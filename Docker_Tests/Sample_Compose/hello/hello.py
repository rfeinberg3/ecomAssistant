import socket

def send_message(msg):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("goodbye", 5001))
	sock.send(msg.encode())
	sock.close()

if __name__ == '__main__':
	print(f"Hello_World! Sending This  Message to Service 2: \"Hello, I\'m Service 1!\"")
	send_message("Hello, I\'m Service 1!")
