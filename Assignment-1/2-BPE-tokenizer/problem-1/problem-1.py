c = chr(0) # returns the Unicode character for the null character, which is '\u0000'.
print(c)
print(c.__repr__())
print(repr(c))

# "this is a test" + chr(0) + "string"
print("this is a test" + chr(0) + "string")