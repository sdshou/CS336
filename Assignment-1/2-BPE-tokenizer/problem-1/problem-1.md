# Problem 1: Understanding Unicode

(a) What Unicode character does chr(0) return?
'\u0000'

(b) How does this character’s string representation (__repr__()) differ from its printed
representation?
the repr of this char is '\x00'

(c) What happens when this character occurs in text?
It prints out nothing, like an empty string