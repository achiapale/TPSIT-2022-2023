class Packet:
    def __init__ (self, username, message):
       self.username = username
       self.message = message

    def to_bytes(self):
        bufferBytes = b''

        buf_bytes = self.buffer.encode('utf8')
        bufferBytes = len(buf_bytes).to_bytes(1, 'big')         # big--> cifra più significativa come prima
        buffer = buffer + bufferBytes + buf_bytes

        return buffer

    @staticmethod
    def from_bytes(buffer):
        username_size = int.from_bytes(buffer[0:1], 'big')
        username = buffer[1: buf_bytes + 1].decode('utf8')

        message_size = int.from_bytes(buffer[username_size+1:username_size+3], 'big')
        message = buffer[username_size+3:username_size+3+message_size+1].decode('utf-8')

        return Packet(username, message)

    def run_tests():
        pkt0 = Packet("username", "message")
        pkt1 = Packet.from_bytes(pkt0.to_bytes())
        # genera errori se non sono true
        assert(pkt0.message == pkt1.message)
        assert(pkt0.username == pkt1.username)    




if __name__ == "__main__":
    run_tests()     