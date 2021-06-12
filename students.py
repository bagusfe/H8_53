def make_students(names):
    students = {}
    for i in range(1, len(names)+1):
        students[i] = names[i-1]
    return students


bootcamp_name = "hacktiv8"
id_to_students = {
    1: "yusuf",
    2: "satya",
    3: "richard",
    4: "stefani",
    5: "timotius",
}
print("bootcamp name:", bootcamp_name)

list_names = ["john", "star", "lucifer", "python"]
print("list names:", list_names)
print("list of students with id:")
print(make_students(list_names))