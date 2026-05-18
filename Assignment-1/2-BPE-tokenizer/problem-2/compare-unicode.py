test_string = "hello!"
test_string_2 = "こんにちは!"

def compare_unicode(test_string):
    utf8 = test_string.encode("utf-8")
    utf16 = test_string.encode("utf-16")
    utf32 = test_string.encode("utf-32")
    print("utf-8: ", utf8)
    print(list(utf8))
    print("utf-16: ", utf16)
    print(list(utf16))
    print("utf-32: ", utf32)
    print(list(utf32))
    print("utf-8 length: ", len(utf8))
    print("utf-16 length: ", len(utf16))
    print("utf-32 length: ", len(utf32))

compare_unicode(test_string)
print("--------------------------------")
compare_unicode(test_string_2)