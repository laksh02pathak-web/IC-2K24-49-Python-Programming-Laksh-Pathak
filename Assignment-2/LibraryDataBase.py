books = {}

while True:
    print("1.Add 2.Issue 3.Return 4.Search 5.Reports 6.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        b = input("ISBN: ")
        if b in books:
            books[b]["copies"] += int(input("Copies: "))
        else:
            books[b] = {
                "title": input("Title: "),
                "author": input("Author: "),
                "copies": int(input("Copies: ")),
                "issued_to": []
            }

    elif ch == 2:
        b = input("ISBN: ")
        m = input("Member: ")

        if b in books:
            total = sum(m in x["issued_to"] for x in books.values())
            if m in books[b]["issued_to"]:
                print("Already Issued")
            elif total >= 2:
                print("Limit Reached")
            elif books[b]["copies"] > 0:
                books[b]["copies"] -= 1
                books[b]["issued_to"].append(m)
            else:
                print("No Copies")

    elif ch == 3:
        b = input("ISBN: ")
        m = input("Member: ")
        if b in books and m in books[b]["issued_to"]:
            books[b]["issued_to"].remove(m)
            books[b]["copies"] += 1
        else:
            print("Invalid Return")

    elif ch == 4:
        b = input("ISBN: ")
        print(books.get(b, "Not Found"))

    elif ch == 5:
        author = input("Author: ")
        print([x["title"] for x in books.values() if x["author"].lower() == author.lower()])

        members = {}
        for b, x in books.items():
            for m in x["issued_to"]:
                members.setdefault(m, []).append(x["title"])

        print(members)
        print([m for m in members if len(members[m]) > 1])
        print([x["title"] for x in books.values() if x["copies"] == 0])
        print([x["title"] for x in books.values() if not x["issued_to"]])

    elif ch == 6:
        break