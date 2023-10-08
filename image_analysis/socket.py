import socket
import threading
from datetime import datetime
import pickle
import codecs
import numpy as np
from PIL import Image, ImageSequence

class Socket:
    def __init__(self, ip, port, name=""):
        self.TCP_IP = ip
        self.TCP_PORT = port
        self.name = name
        self.buf_size = 64
        self.chunk_size = 1048576
    
    def socketClose(self):
        self.sock.close()

    def socketOpen(self):
        pass

    def recvall(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def sendLMT(self, msg):
        length = str(len(msg))
        stime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.conn.sendall(length.encode('utf-8').ljust(64))
        self.conn.send(msg.encode('utf-8'))
        self.conn.sendall(stime.encode('utf-8').ljust(64))
        
    def recLMT(self):
        length = int(self.recvall(self.conn, self.buf_size).decode('utf-8'))
        stringData = self.recvall(self.conn, length).decode('utf-8')
        stime = self.recvall(self.conn, self.buf_size).decode('utf-8')
        return (stringData, stime)

    def large_sendLMT(self, msg):
        msg_array = []
        i = 0
        while i+self.chunk_size < len(msg):
            msg_array.append(msg[i:i+self.chunk_size])
            i+=self.chunk_size
        msg_array.append(msg[i:])
        self.sendLMT(str(len(msg_array)))
        for chunk in msg_array:
            self.sendLMT(chunk)

    def large_recLMT(self):
        num_chunks, stime = self.recLMT()
        data = ""
        for i in range(int(num_chunks)):
            chunk, stime = self.recLMT()
            data+=chunk
        return data, stime

    def sendLMT_obj(self, obj):
        string_data = codecs.encode(pickle.dumps(obj, protocol=4), 'base64')
        length = str(len(string_data))
        stime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.conn.sendall(length.encode('utf-8').ljust(64))
        self.conn.sendall(string_data)
        self.conn.sendall(stime.encode('utf-8').ljust(64))

    def recLMT_obj(self):
        length = int(self.recvall(self.conn, self.buf_size).decode('utf-8'))
        stringData = self.recvall(self.conn, length)
        stime = self.recvall(self.conn, self.buf_size).decode('utf-8')
        obj = pickle.loads(codecs.decode(stringData, 'base64'))
        return (obj, stime)

    def send_file(self, file_path):
        send_file = open(file_path, "rb")
        data = send_file.read()
        print(data)
        self.sendLMT(str(len(data)))
        self.conn.send(data)
        send_file.close()

    def rec_file(self, file_path):
        write_file = open(file_path, "wb")
        data_size, stime = self.recLMT()
        data = self.recvall(self.conn, int(data_size))
        write_file.write(data)
        write_file.close()

    def send_tif_stack(self, file_path):
        img = Image.open(file_path)
        data = np.asarray(img)
        self.sendLMT(str(img.n_frames))
        for i, page in enumerate(ImageSequence.Iterator(img)):
            print(i, flush=True)
            page_data = np.asarray(page)
            self.sendLMT_obj(page_data)

    def rec_tif_stack(self):
        tif_data = []
        n_frames, stime = self.recLMT()
        for i in range(int(n_frames)):
            page, stime = self.recLMT_obj()
            tif_data.append(page)
        return (tif_data, stime)

    def send_tif_page(self, file_path, page):
        img = Image.open(file_path)
        img.seek(page)
        img_arr = np.asarray(img)
        self.sendLMT_obj(img_arr)

    def rec_tif_page(self):
        return self.recLMT_obj()

class SocketServer(Socket):
    def __init__(self, ip, port, name=""):
        super().__init__(ip, port, name)
        self.socketOpen()
        self.receiveThread = threading.Thread(target=self.receiveData, daemon=True)
        self.receiveThread.start()

    def socketClose(self):
        super().socketClose()
        print(self.name + u'HPC socket [ TCP_IP: ' + self.TCP_IP +  ', TCP_PORT: ' + str(self.TCP_PORT) + ' ] is closed', flush=True)

    def socketOpen(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.TCP_IP, self.TCP_PORT))
        self.sock.listen(1)
        print(self.name + u' server [ TCP_IP: ' + self.TCP_IP + ', TCP_PORT: ' + str(self.TCP_PORT) + ' ] is open', flush=True)
        self.conn, self.addr = self.sock.accept()
        print(self.name + u' server [ TCP_IP: ' + self.TCP_IP + ', TCP_PORT: ' + str(self.TCP_PORT) + ' ] is connected with client', flush=True)

    def dataListener(self):
        pass

    def exceptionHandler(self, e):
        print('EXCEPTION receiving data: ' + str(e), flush=True)
        self.socketClose()
        self.socketOpen()
        self.receiveThread = threading.Thread(target=self.receiveData, daemon=True)
        self.receiveThread.start()

    def receiveData(self):
        try:
            self.dataListener()
        except Exception as e:
            self.exceptionHandler(e)

class SocketClient:
    def __init__(self, ip, port):
        self.TCP_SERVER_IP = ip
        self.TCP_SERVER_PORT = port

