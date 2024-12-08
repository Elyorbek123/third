#num=int(input("SON kiriting: "))

count=[[10,20,30], [5,15,25],[0,12,18]]

hold=[]


for i in range(len(count)):
   hold.append(max(count[i]))


hold = tuple(hold)

print(hold, type(hold))









