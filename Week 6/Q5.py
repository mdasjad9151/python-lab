# Write a program to get roll numbers, names, and marks of students and store these details in a file called "Marks. data".

def store_student_data(filename="Marks.data"):
    num_students = int(input("How many students do you want to enter? "))
    with open(filename, "w") as file:
        for _ in range(num_students):
            roll_no = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = input("Enter marks: ")
            file.write(f"{roll_no}, {name}, {marks}\n")
    print(f"Student data saved to {filename}")


store_student_data()
