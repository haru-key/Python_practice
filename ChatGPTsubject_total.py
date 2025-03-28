#try-exceptは学習前のため一度保留

total = 0
while True:
    n = input("数字を入力してください（終了するには「stop」と入力）:")
    if n == "stop":
        break
    elif n.isdecimal() == False: #数字以外が入力されたときにエラー文を返す
        print("無効な入力です。正の整数を入力してください。")
    elif int(n) < 0: #負の数が入力されたときにエラー文を返す←この工程があるのなら小数が入力されたときの条件式も必要では……？
        print("無効な入力です。正の整数を入力してください。")
    else:
        n = int(n)
        total += n

#total = round(total)
#ChatGPTくんに「int型なら丸めなくていいよ」と言われていたが、問題を解いている最中に小数を弾くためfloat型で試みた痕跡
#戒めとしてコメントで残しつつ消した

print("合計: "+ str(total))