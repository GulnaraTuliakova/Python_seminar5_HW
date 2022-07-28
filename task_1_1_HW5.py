# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


string = 'привет абв какабв твои дела'
a = string.split()
b =[]
for i in range(len(a)):
    if  'абв' not in a[i]:
        b.append(a[i])

print(b)