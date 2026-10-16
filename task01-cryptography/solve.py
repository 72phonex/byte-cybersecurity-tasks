import base64
challenge = "QkFJTntiQTczX1E4Ul9BcmhIQ19YNHlHY0R9"
layer1 = base64.b64decode(challenge).decode()
print("Layer 1:", layer1)
def beaufort(text, key):
    out, i = [], 0
    for ch in text:
        if ch.isalpha():
            k = ord(key[i % len(key)].upper()) - 65
            c = ord(ch.upper()) - 65
            p = chr((k - c) % 26 + 65)
            out.append(p if ch.isupper() else p.lower())
            i += 1
        else:
            out.append(ch)
    return "".join(out)
key = "".join(chr((ord(p) + ord(c) - 130) % 26 + 65) for p, c in zip("BYTE", "BAIN"))
print("Key:", key)
print("Flag:", beaufort(layer1, key))