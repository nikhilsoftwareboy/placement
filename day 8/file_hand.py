
with open("hello.txt", "r") as f:
    d = f.read()
    print(d)

send_data = input("Enter the data you want in the file: ")

with open("hello.txt", "a") as f:
    f.write(send_data + "\n")

with open("hello.txt", "r") as f:
    data = f.read(5)
    print(data)

with open("hello.txt", "r") as html_file:
    for line in html_file:
        print(line.strip())

user_input=input("html data")
with open("index.html",'a') as html_file:
    html_file.write(user_input)