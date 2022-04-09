# 1
print("実家に帰りたい")
print("***の講座を始めたい")
print("自分が事業者として独立する！")
print("\n")

# 2
a = 9.9
if a < 10:
    print("10より小さな数です")
else:
    print("10以上の数です")
print("\n")

# 3
b = 30
if b <= 10:
    print("10以下の数です")
elif b <= 25:
    print("10より大きく、25以下の数です")
else:
    print("25より大きい数です")
print("\n")

# 4
print(103 % 3)
print("\n")

# 5
print(103 // 3)
print("\n")

# 6
age = 93

bef = 6
ele = 12
jun = 15
hig = 18
adu = 64
gol = 80
if age <= bef:
    print("無料")
elif age <= ele:
    print("小学生料金")
elif age <= jun:
    print("中学生料金")
elif age <= hig:
    print("高校生料金")
elif age <= adu:
    print("大人料金")
elif age < gol:
    print("シルバー料金")
else:
    print("御長寿料金")
