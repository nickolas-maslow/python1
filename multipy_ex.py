import openpyxl

workbook = openpyxl.load_workbook("homework_dir/data.xlsx")
worksheet = workbook.active

max_row1 = worksheet.max_row + 1
max_column1 = worksheet.max_column + 1

out_list_ = []
for row in range(1, max_row1 + 1):
    in_list_ = []
    for col in range(1, max_column1 + 1):
        value = worksheet.cell(row=row, column=col).value
        if value is None:
            value = ""
        in_list_.append(value)
    out_list_.append(in_list_)
print(out_list_)

set1 = set(out_list_[1])
set1.remove("")
print(set1)
set2 = set(out_list_[3])
set2.remove("")
print(set2)
set3 = set(out_list_[5])
set3.remove("")
print(set3)

set4 = set2.intersection(set1, set3)
print(set4)

set5 = set2.difference(set1, set3)
print(set5)

set6 = set3.union(set1)
print(set6)
