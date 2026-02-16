a=input("Enter your Email id: ")
y=a.find("@")
n=y-3
print(a[0:3] + n * "*"  + a[y::])