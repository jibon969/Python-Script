string_nonASCII = input("Enter your test what ever you want : ")
string_encode = string_nonASCII.encode("ascii", "ignore")
string_decode = string_encode.decode()
print(string_decode)