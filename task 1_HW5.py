# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = 'привет абв какабв твои дела'
a = string.split()
b =[]

[b.append(a[i]) for i in range(len(a))  if 'абв' not in a[i] ]
print(b)
