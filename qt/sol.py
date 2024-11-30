word = input()
min_ = word
max_ = word
while word != "стоп":
    if len(word) < len(min_):
        min_ = word
    elif len(word) > len(max_):
        max_ = word
    word = input()

flag = True
for char in min_:
    if char not in max_:
        print("НЕТ")
        flag = False
        break
if flag is True:
    print("ДА")