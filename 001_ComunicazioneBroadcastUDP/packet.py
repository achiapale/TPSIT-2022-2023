class Packet:
    def __init__ (self, buffer):
        self.buffer = buffer

    def to_bytes(self):
        bufferBytes = b''
        buf_bytes = self.buffer.encode('utf8')

        bufferBytes = len(buf_bytes).to_bytes(1, 'big')
        bufferBytes = bufferBytes + buf_bytes

        return bufferBytes    

    @staticmethod
    def from_bytes(bufferBytes):
        buf_bytes = int.from_bytes(bufferBytes[0:1], 'big')
        buf_bytes = bufferBytes[1: buf_bytes + 1].decode('utf8')

        return Packet(bufferbytes)

def run_tests():
    pkt0 = Packet("buffer")
    pkt1 = Packet.from_bytes(pkt0.to_bytes())
    assert(pkt0.buffer == pkt1.buffer)




if __name__ == "__main__":
    run_tests()     