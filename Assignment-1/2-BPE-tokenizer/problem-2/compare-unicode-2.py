s = "hello"           # ASCII-heavy
s2 = "café"           # Latin-1 supplement
s3 = "你好"            # CJK

for label, text in [("ASCII", s), ("Latin-1+", s2), ("CJK", s3)]:
    print(label, repr(text))
    print("  UTF-8:", list(text.encode("utf-8")))
    print("  UTF-16LE:", list(text.encode("utf-16le")))
    print("  UTF-32LE:", list(text.encode("utf-32le")))