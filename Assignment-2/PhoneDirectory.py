contacts = {}

while True:
    print("1.Add 2.Add Number 3.Update 4.Delete 5.Search 6.Reports 7.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Name: ")
        p = input("Phone: ")

        used = any(p in d["phones"] for d in contacts.values())

        if len(p) == 10 and p.isdigit() and not used:
            contacts[name] = {
                "phones": [p],
                "email": input("Email: "),
                "city": input("City: ")
            }
        else:
            print("Invalid or Duplicate Number")

    elif ch == 2:
        name = input("Name: ")
        p = input("Phone: ")

        used = any(p in d["phones"] for d in contacts.values())

        if name in contacts and len(p) == 10 and p.isdigit() and not used:
            contacts[name]["phones"].append(p)
        else:
            print("Invalid Number or Contact")

    elif ch == 3:
        name = input("Name: ")
        if name in contacts:
            contacts[name]["email"] = input("Email: ")
            contacts[name]["city"] = input("City: ")

    elif ch == 4:
        name = input("Name: ")
        contacts.pop(name, None)

    elif ch == 5:
        s = input("Search: ").lower()
        for name, d in contacts.items():
            if s in name.lower():
                print(name, d)

    elif ch == 6:
        reverse = {p: n for n, d in contacts.items() for p in d["phones"]}
        print(reverse)

        city = {}
        for n, d in contacts.items():
            city.setdefault(d["city"], []).append(n)

        print(city)

        for n, d in contacts.items():
            if len(d["phones"]) > 1:
                print(n, d["phones"])

        for n in sorted(contacts):
            print(n, contacts[n])

    elif ch == 7:
        break