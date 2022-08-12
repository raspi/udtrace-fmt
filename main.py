from io import BytesIO

from lib import hexdump

if __name__ == '__main__':
    import fileinput

    packetCounter: int = 1
    for line in fileinput.input(encoding="utf-8"):
        line = line.rstrip()

        if not (
                line.find(' writev W ') > 0
                or line.find(' recv R ') > 0
                or line.find(' recvmsg R ') > 0
        ):
            continue

        # <FD> <call> <R/W> <data hex>
        # 3 writev W <data hex>
        # 3 recv R <data hex>
        # 3 recvmsg R <data hex>
        fdid, mtype, mchar, data = line.split(' ')
        fdid = int(fdid)
        data = bytes.fromhex(data)

        print("---- Packet #{0}: fd:{1} type:{2} {3}  len: {4} (0x{4:02x})"
              .format(packetCounter, fdid, mtype, mchar, len(data))
              )
        print(hexdump(BytesIO(data), 16))

        packetCounter += 1
