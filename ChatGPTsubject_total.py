total = 0
while True:
    n = input("数字を入力してください（終了するには「stop」と入力）:")
    if n == "stop":
        break
    elif n.isdecimal() == False:
        print("無効な入力です。正の整数を入力してください。")
    else:
        n = int(n)
        total += n

total = round(total)
print("合計: "+ str(total))