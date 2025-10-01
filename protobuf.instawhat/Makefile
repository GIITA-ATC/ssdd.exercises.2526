HOST = localhost
PORT = 10001

all: compile

compile:
	protoc --python_out=. instawhat.proto

clean:
	$(RM) *_pb2* *~
	$(RM) -rf __pycache__

run_server:
	python3 server.py $(PORT)

rate_photo:
	python3 client.py $(HOST) $(PORT) rate_photo Jane.Doe "http://example.com/photo.jpg" 5
