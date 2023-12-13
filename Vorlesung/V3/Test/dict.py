# datei = open("RaisingHell.txt", "r")
# text = datei.read()
# text = text.lower()

# for ch in '.!?"/':
#     text = text.replace(ch, ' ')
# worte = text.split()

# anz = {}
# for w in worte:
#     anz[w] = anz.get(w, 0) + 1

passwd = {}
file = open("passwords.txt", "r")
for line in file:
    print(line)
    print(line.split())
    user, pw = line.split()
    # print(user)
    # passwd[user] = pw

print(passwd)


