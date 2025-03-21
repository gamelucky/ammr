def chuso(s):
    return sum(1 for ch in s if '0' <= ch <= '9')
def tanh(s):
    return sum(1 for ch in s if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'))
s = input("Nhập một xâu ký tự: ")
print("Tổng số ký tự là chữ số:", chuso(s))
print("Tổng số ký tự là chữ cái tiếng Anh:", tanh(s))
