with open('text.txt', 'r') as f:
    text = f.readlines()
f.close()

normal_text = [line.rstrip() for line in text]

for i in normal_text:
    fine_text = i
