import random

#1
spisok1 = []
spisok2 = []
spisok3 = []
for i in range(30):
    ran1 = random.randint(0,100)
    ran2 = random.randint(0,100)
    spisok1.append(ran1)
    spisok2.append(ran2)
print(spisok1)
print(spisok2)

for i in range(len(spisok1)):
    if spisok2[i] % 2 == 0:
        spisok3.append(spisok2[i])
    elif spisok1[i] % 2 != 0:
        spisok3.append(spisok1[i])
print(spisok3)

#2
a1 = 10
for i in range(1,a1+1):
    print(*range(i, i*a1+1, i), sep ="\t")

#3
old = open('1.txt')
lines = old.readlines()
pashamozhet = open("2.txt", "w+")
five = lines[4]
lines.remove(five)
for i in lines:
    pashamozhet.write(str(i))
pashamozhet.close()
old.close

#4
mops = open('3.txt', 'r')
for i, line in enumerate(mops):
    if i == 3:
        print(line)

#5

itachi = 0
n = int(input("какое число: "))
if n == 0:
    n = int(input("какое число(но не 0): "))
for i in range(1, n + 1):
    itachi += i
print(itachi)

#6
array = [235, 21436, 1346, 1436, 1346, 679, 234, 457, 231, 745, 3453]
for i in reversed(array):
    print(i)

#7
down = int(input("ну типо нижний предел: "))
up = int(input("ну типо верхний предел: "))
print("Простые числа этого диапозона: ")
for num in range(down, up +1):
    if num > 1:
        for i in range(2, num):
            if (num % 1) == 0:
                break
        else:
            print(num)