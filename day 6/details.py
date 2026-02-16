def data(**info):
    print("\nStudent Details")
    for key, value in info.items():
        print(key, ":", value)
def det():

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")
    sem = input("Enter Semester: ")
    data(name=name, age=age, branch=branch, sem=sem)

