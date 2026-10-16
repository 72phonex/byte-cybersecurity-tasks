import struct, zlib, sys, os
src = sys.argv[1] if len(sys.argv) > 1 else "challenge.png"
d = bytearray(open(src, "rb").read())
FAKE = b"\x00\x00\x00\x00IEND\xaeB`\x82"
while d.find(FAKE) != d.rfind(FAKE):
    pos = d.find(FAKE)
    print(f"Removed fake IEND at byte {pos}")
    del d[pos:pos + len(FAKE)]
ihdr = bytes(d[16:29])
stored = struct.unpack(">I", d[29:33])[0]
w0, h0 = struct.unpack(">II", ihdr[:8])
print(f"IHDR says {w0}x{h0}, CRC ok: {zlib.crc32(b'IHDR' + ihdr) & 0xffffffff == stored}")
if zlib.crc32(b"IHDR" + ihdr) & 0xffffffff != stored:
    for h in range(1, 5000):
        body = b"IHDR" + struct.pack(">II", w0, h) + ihdr[8:]
        if zlib.crc32(body) & 0xffffffff == stored:
            print(f"CRC matches with height = {h}")
            d[20:24] = struct.pack(">I", h)
            break
open("fixed.png", "wb").write(d)
print("Wrote fixed.png")
os.startfile("fixed.png")
