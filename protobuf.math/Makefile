HOST = localhost
PORT = 10001

all: compile

compile:
	protoc --python_out=. math.proto

clean:
	$(RM) *_pb2* *~
	$(RM) -rf __pycache__
