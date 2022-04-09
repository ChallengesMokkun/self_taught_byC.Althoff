# 1
s1 = "カミュ"
for c in s1:
    print(c)
print(s1[0])
print(s1[1])
print(s1[2])
print("\n")

# 2
inp1 = input("何書いた？")
inp2 = input("それ誰に送った？")

print("私は昨日{}を書いて、{}に送った！".format(inp1,inp2))
print("\n")

# 3
print("aldous Huxley was born in 1894.".title())
print("\n")

# 4
s2 = "どこで？　だれが？　いつ？"
li2 = s2.split("　")
print(li2)
print("\n")

# 5
li3 = ["The","fox","jumped","over","the","fence","."]
s3 = " ".join(li3)
s3 = s3.replace(" .",".")
print(s3)
print("\n")

# 6
print("A screaming comes across the sky.".replace("s","$"))
print("\n")

# 7
print("Hemingway".index("m"))
print("\n")

# 8
print("これまで私は、愚問とは\"グッドモーニング\"の略かと思っていたが、どうやらそういう質問のことを言うらしいな。")
print("\n")

# 9
s4 = "three" * 3
print(s4)
s5 = "three" + "three" + "three"
print(s5)
print("\n")

# 10
s7 = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(s7[:10])
