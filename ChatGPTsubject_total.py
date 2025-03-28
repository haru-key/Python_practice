total = 0
while True:
    n = input("数字を入力してください（終了するには「stop」と入力）:")
    if n == "stop":
        break
    elif n.isdecimal() == False: #数字以外の文字列、負の整数、小数が入力されたときにエラー文を返す
        print("無効な入力です。正の整数を入力してください。")
    else:
        n = int(n)
        total += n

print("合計: "+ str(total))
#ふと思ったけど0って正の整数ではないから弾くべき？