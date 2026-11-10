students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Show Student")
    print("5. Reports")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        roll = input("Enter roll number: ")

        if roll in students:
            print("Duplicate roll number!")
        else:
            name = input("Enter name: ")
            marks = {}

            n = int(input("Enter number of subjects: "))

            for i in range(n):
                sub = input("Enter subject: ")
                m = int(input("Enter marks: "))

                if 0 <= m <= 100:
                    marks[sub] = m
                else:
                    print("Invalid marks!")

            students[roll] = {
                "name": name,
                "marks": marks
            }

            print("Student added successfully!")

    elif ch == 2:
        roll = input("Enter roll number: ")

        if roll in students:
            sub = input("Enter subject: ")
            m = int(input("Enter new marks: "))

            if 0 <= m <= 100:
                students[roll]["marks"][sub] = m
                print("Marks updated!")
            else:
                print("Invalid marks!")
        else:
            print("Student not found!")

    elif ch == 3:
        roll = input("Enter roll number: ")

        if roll in students:
            del students[roll]
            print("Student deleted!")
        else:
            print("Student not found!")

    elif ch == 4:
        roll = input("Enter roll number: ")

        if roll in students:
            print(students[roll])
        else:
            print("Student not found!")

    elif ch == 5:
        if not students:
            print("No student records!")
            continue

        averages = {}

        for roll, data in students.items():
            marks = data["marks"]

            if marks:
                avg = sum(marks.values()) / len(marks)
                averages[roll] = round(avg, 2)
                print(data["name"], "Average:", averages[roll])
            else:
                print(data["name"], "No marks available")

        if averages:
            topper = max(averages, key=averages.get)
            print("Topper:", students[topper]["name"])

        # Highest marks in each subject
        subjects = {}

        for roll, data in students.items():
            for sub, mark in data["marks"].items():
                if sub not in subjects or mark > subjects[sub][1]:
                    subjects[sub] = (data["name"], mark)

        print("Highest in each subject:", subjects)

        # Students scoring below 40
        print("Below 40:")
        for roll, data in students.items():
            for sub, mark in data["marks"].items():
                if mark < 40:
                    print(data["name"], sub, mark)
                    break

        # Grade-wise grouping
        grades = {"A": [], "B": [], "C": [], "D": [], "F": []}

        for roll, avg in averages.items():
            name = students[roll]["name"]

            if avg >= 90:
                grades["A"].append(name)
            elif avg >= 75:
                grades["B"].append(name)
            elif avg >= 60:
                grades["C"].append(name)
            elif avg >= 40:
                grades["D"].append(name)
            else:
                grades["F"].append(name)

        print("Grade-wise:", grades)

    elif ch == 6:
        print("Program ended!")
        break

    else:
        print("Invalid choice!")
