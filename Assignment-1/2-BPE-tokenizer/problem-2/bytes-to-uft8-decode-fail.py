string = bytes([0xe3, 0x81, 0x82])
# this prints 'ぁ'
print(string.decode("utf-8"))

string = bytes([0x80, 0x80])
# this throws error: 
#   UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
print(string.decode("utf-8"))