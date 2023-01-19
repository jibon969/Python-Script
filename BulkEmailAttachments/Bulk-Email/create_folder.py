name = ["Jibon\n","Atiya\n", "Sakib\n", "Dhoni\n"]

new_file = open("newfile.txt", mode="a+", encoding="utf-8")
for n in name:
    new_file.write(n)
print("Tell the byte at which the file cursor is:", new_file.tell())
new_file.seek(5)
for line in new_file:
    print(line)
