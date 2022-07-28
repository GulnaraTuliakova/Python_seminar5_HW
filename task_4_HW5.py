# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.
path = r'HW_5__task__04.txt'
with open(path, 'r') as n:
    data = n.read()
    data_n = []
    for i in data:
        data_n.append(i)
  
with open(path, 'a') as n:
    data_new = [data_n[0]]
    count = 0
    n.write(str())
    for i in range(len(data_n)):
        if data_n[i] == data_new[-1]:
            count += 1
        if data_n[i] != data_new[-1]:
            data_new.append(data_n[i])
            n.write(str(count))
            n.write(data_n[i-1])
            count = 1