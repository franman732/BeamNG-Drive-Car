import socket
import struct

HOST = "127.0.0.1"
PORT = 4444
STRUCT_FORMAT = "<4s21f"
PACKET_SIZE = struct.calcsize(STRUCT_FORMAT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    packet, address = sock.recvfrom(1024)

    if len(packet) == PACKET_SIZE:
        unpacked = struct.unpack(STRUCT_FORMAT, packet)

        header = unpacked[0].decode("ascii", errors="ignore")

        if header != "BNG1":
            continue

        # Map the remaining 21 floats to variables
        (
            posX, posY, posZ,
            velX, velY, velZ,
            accX, accY, accZ,
            upX, upY, upZ,
            rollPos, pitchPos, yawPos,
            rollVel, pitchVel, yawVel,
            rollAcc, pitchAcc, yawAcc
        ) = unpacked[1:]

        print(f"Pos: ({posX:.2f}, {posY:.2f}, {posZ:.2f}) | Roll/Pitch/Yaw: ({rollPos:.2f}, {pitchPos:.2f}, {yawPos:.2f})")