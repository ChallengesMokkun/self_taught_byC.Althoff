# 1
shows = ["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for show in shows:
    print(show)
print("\n")

# 2
for i in range(25,51):
    print(i)
print("\n")

# 3
for i, show in enumerate(shows):
    print(str(i)+":"+show)
print("\n")

# 4
numbers = ["1","3","5","6","7","11","13","15","16","21","23","24"]
while True:
    a = input("数当てゲーム！！　qを押すと終了するよ　　 (ヒント：1〜30の整数を入れてみて！)")
    if a == "q":
        break
    if a in numbers:
        print("正解")
    elif a.isdigit() == True:
        print("不正解")
    else:
        print("数字を入力するか、qで終了します")
print("\n")

# 5
x = [8,19,148,4]
y = [9,1,33,83]
z = []

for i in x:
    for j in y:
        z.append(i * j)
print(z)

