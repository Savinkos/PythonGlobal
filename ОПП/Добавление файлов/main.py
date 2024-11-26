# # f = open("newText.txt")
# # print(type(f))
# # data = f.read()
# # print(data, type(data))
# # f.close()
import os
import time

with open('newText.txt ', 'a') as f:
    f.write(f'{time.time()}')
#
with open('newText.txt', 'a') as f:
    f.write('Запись третья Запись четыре \n')

# with open('newText.txt') as f:
#     print(f.read())


file_path = os.path.join(os.getcwd(), 'newText.txt')
print(os.getcwd())

with open(file_path, 'a') as f:
    f.write(f'В директории', {file_path} f'находится клад')