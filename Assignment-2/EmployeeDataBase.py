employees = {}

while True:
    print("1.Add 2.Update 3.Delete 4.Search 5.Reports 6.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        e = input("ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        salary = int(input("Salary: "))
        employees[e] = {"name": name, "dept": dept, "salary": salary}

    elif ch == 2:
        e = input("ID: ")
        if e in employees:
            employees[e]["salary"] = int(input("Salary: "))

    elif ch == 3:
        e = input("ID: ")
        employees.pop(e, None)

    elif ch == 4:
        e = input("ID: ")
        print(employees.get(e, "Not Found"))

    elif ch == 5:
        payroll = {}
        count = {}

        for e, d in employees.items():
            dept = d["dept"]
            payroll[dept] = payroll.get(dept, 0) + d["salary"]
            count[dept] = count.get(dept, 0) + 1

        print(payroll, count)

        highest = {}
        for e, d in employees.items():
            dept = d["dept"]
            if dept not in highest or d["salary"] > highest[dept][1]:
                highest[dept] = (d["name"], d["salary"])

        print(highest)

        print(sorted(employees.items(), key=lambda x: x[1]["salary"], reverse=True))

        new_salary = {e: d["salary"]*1.1 if d["salary"] < 50000 else d["salary"] for e, d in employees.items()}
        print(new_salary)

        avg = {d: payroll[d]/count[d] for d in payroll}
        if avg:
            print(max(avg, key=avg.get))

    elif ch == 6:
        break