# var_list1 = [12, 16, 0, -100, "1234", True]
# cikl kotoryi prohodit po masivu obekta i beret kazhdiy cikl etot obekt k sebe v peremennuyu
# for list_element in var_list1:
#     print("element: 'spiska' ",var_list1.index(list_element), list_element, type(list_element))
#     for j in var_list1:
#         print("element: 'spiska' ", var_list1.index(j), j, type(j))


# var_int1 = 12
# while var_int1:
#     var_int1 = var_int1 + 1
#     print(var_int1)
#     if var_int1 == 500:
#         print('my doshli do 500')
# print("Cikl zavershen")

hours = 0
minutes = 0
seconds = 0
while True:
    seconds += 1
    print(hours, minutes, seconds)

index_i = 0
var_list = ['Almaty', 'Nur-Sultan', 'Tashkent', 'Taraz']
for i in var_list:
    string_city = f'{i} {index_i}'
    print(i + " " + str(var_list.index(i)+1))
    index_i += 1