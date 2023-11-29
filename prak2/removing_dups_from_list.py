name = ["siva", "vinjam", "siva", "siva", "siva"]
word = "siva"
n = 2
count = 0

for i in range(0, len(name)-1):
    if name[i] == word:
        count = count + 1
        if count == n:
            del name[i]
print(name)
