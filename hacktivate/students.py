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