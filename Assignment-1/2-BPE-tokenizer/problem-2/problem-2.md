# Problem 2: Unicode Encodings

(a) What are some reasons to prefer training our tokenizer on UTF-8 encoded bytes, rather than
UTF-16 or UTF-32? It may be helpful to compare the output of these encodings for various
input strings.

See `compare-unicode.py` and `compare-unicode-2.py`
Most files, HTTP, JSON, and logs are UTF-8. 
For English-heavy corpora, UTF-8 keeps sequences shorter, which often means fewer BPE tokens and less redundancy for the same string.

(b) Consider the following (incorrect) function, which is intended to decode a UTF-8 byte string
into a Unicode string. Why is this function incorrect? Provide an example of an input byte
string that yields incorrect results.

```
def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
    return "".join([bytes([b]).decode("utf-8") for b in bytestring])
>>> decode_utf8_bytes_to_str_wrong("hello".encode("utf-8"))
'hello'
```

See `decode-utf8-fail.py`. I tried an example with `"こんにちは!".encode("utf-8")`, and it throws error: `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe3 in position 0: unexpected end of data`.

Some charactor is consisted of 2 or more bytes, so that's why you can't decode byte by byte.

(c) Give a two-byte sequence that does not decode to any Unicode character(s).
see `bytes-to-uft8-decode-fail.py`
example:
`bytes([0xC0, 0x80])`
`bytes([0x80, 0x80])`
`bytes([0xC3, 0x28])`
`bytes([0xFF, 0xFE])`
