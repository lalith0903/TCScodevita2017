meter_list = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}
dmp_list = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":4, "G":3, "H":2, "I":1, "J":0}
n = int(input())
string = input().split()
amount = int(input())
li = []
#COMPLETE THE PROGRAM TCS CODEVITA 2017 ROUND 2 
for meter in string:
    add = 0
    for i in range(len(meter)):
        if i < len(meter) - 1:
            if meter[i] == "J" and meter[i+1] == "A":
                add = dmp_list[meter[i]] + 10 * add
            elif meter[i] == "I" and meter[i+1] == "B":
                add = dmp_list[meter[i]] + 10 * add
            elif meter[i] == "H" and meter[i+1] == "C":
                add = dmp_list[meter[i]] + 10 * add
            elif meter[i] == "G" and meter[i+1] == "D":
                add = dmp_list[meter[i]] + 10 * add
            elif meter[i] == "F" and meter[i+1] == "E":
                add = dmp_list[meter[i]] + 10 * add
            else:
                add = meter_list[meter[i]] + 10 * add
        else:
            add = meter_list[meter[i]] + 10 * add
    li.append(add)

amt = sum(li)
#print(amt)
if amt > amount:
    print("GREEDY")
    print(amt - amount)
else:
    print("INNOCENT")


