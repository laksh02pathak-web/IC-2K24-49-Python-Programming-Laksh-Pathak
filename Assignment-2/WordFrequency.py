text = input("Enter paragraph: ").lower()

clean = ""
for ch in text:
    if ch.isalnum() or ch.isspace():
        clean += ch

words = clean.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print("Frequency:", freq)

if words:
    n = int(input("Enter N: "))
    print(sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n])

    print([w for w in freq if freq[w] == 1])

    inv = {}
    for w, c in freq.items():
        inv.setdefault(c, []).append(w)
    print(inv)

    length = {}
    for w in freq:
        length.setdefault(len(w), []).append(w)
    print(length)

    s = input("Search word: ").lower()
    print(freq.get(s, "Not Found"))
else:
    print("Empty String")