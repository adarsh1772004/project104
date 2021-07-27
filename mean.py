import csv
f=open("SOCR-HeightWeight.csv")
reader=csv.reader(f)
data=list(reader)
data.pop(0)
add=0
height=[]
for  i in range(len(data)):
    add=add+float(data[i][1])
    height.append(float(data[i][1]))

mean=add/len(height)
print(mean)

