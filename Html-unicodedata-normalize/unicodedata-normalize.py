
# How to remove unicodedata to normalize

# Example : Country of origin:&nbsp;South Korea.


user_text = input("Please enter your text here : ")
from html import unescape

s = unescape(user_text)
import unicodedata
s = unicodedata.normalize('NFKC', s)
print(s)
