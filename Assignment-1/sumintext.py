import re
hand=open("regex_sum_1283766.txt")
sum=0

for line in hand:
    line = line.rstrip()
    x=re.findall("[0-9]+",line)
    for i in x:
        sum += int(i)
print(sum)

