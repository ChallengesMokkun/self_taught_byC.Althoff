numbers = [1,3,5,6,7,11,13,15,16,21,23,24]
while True:
    a = input("数字を当ててね！qで終わるよ")
    if a == "q":
        break
    try:
        a = int(a)
        if a in numbers:
            print("正解")
        else:
            print("不正解")
    except ValueError:
        print("数字を入力するか、qで終了します")
