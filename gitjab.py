from time import sleep
sõne = input("Sõne: ")
väljastus = ""
for i in range(len(sõne)):
    väljastus+=sõne[i]
    sleep(0.05)
    print(väljastus)