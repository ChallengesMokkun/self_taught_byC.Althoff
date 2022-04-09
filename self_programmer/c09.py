# 4
import csv
eiga = [
    ["トップガン","リスキービジネス","マイノリティーレポート"],
    ["タイタニック","レベナント","インセプション"],
    ["トレーニングの日々","火のついた男","航空"]
    ]
with open("eiga.csv","w",encoding="utf-8",newline="") as f:
    w = csv.writer(f,delimiter=",")
    for show in eiga:
        w.writerow(show)

# 3
import csv
list = [
    ["Top Gun","Risky Business","Minority Report"],
    ["Titanic","The Revenant","Inception"],
    ["Training Day","Man on Fire","Flight"]
    ]
with open("shows.csv","w",newline="") as f:
    w = csv.writer(f,delimiter=",")
    for show in list:
        w.writerow(show)

# 1
import os
file = os.path.join("/Users","(username)","(folder)","(file)")
with open(file,"r") as f:
    print(f.read())
# 2
q1 = input("May I have your name?")
q2 = input("How old are you?")
q3 = input("What is your favorite color?")
q4 = input("Have you ever been here?")
customer = [q1,q2,q3,q4]
with open("customer_list.txt","w") as f:
    for i, que in enumerate(customer,1):
        f.write(str(i)+": "+que+"\n")
