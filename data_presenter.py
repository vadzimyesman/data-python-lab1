import matplotlib
from matplotlib import pyplot as plt


open_file=open("Cupcakeinvoices.csv")

for row in open_file:
    print(row)

open_file.seek(0)

for row in open_file:
    row=row.strip()
    row=row.split(",")
    print(row[2])

open_file.seek(0)

total=0

for row in open_file:
    row=row.strip()
    row=row.split(",")
    #print(row[4])
    total=float(row[4])*float(row[3])
    print(round(total,2))



open_file.seek(0)

all_total=0

for row in open_file:
    row=row.strip()
    row=row.split(",")
    all_total+=float(row[4])*float(row[3])

print(f"Total is {round(all_total,2)}")

open_file.seek(0)

strawberry=[]
vanilla=[]
chocolate=[]
s=0
v=0
c=0

for row in open_file:
    row=row.strip()
    row=row.split(",")
    if row[2]=="Chocolate":
        c=c+float(row[3])*float(row[4])
        c=round(c,2)
        chocolate.append(c)
    elif row[2]=="Vanilla":
        v=v+float(row[3])*float(row[4])
        v=round(v,2)
        vanilla.append(c)
    elif row[2]=="Strawberry":
        s=s+float(row[3])*float(row[4])
        s=round(s,2)
        strawberry.append(s)

print(strawberry)
print(vanilla)      
print(chocolate)

x1=[]
i=0
y1 = strawberry
while i<len(strawberry):
    x1.append(i+1)
    i+=1

plt.plot(x1, y1, color="red", label="strawberry")

x2=[]
j=0
y2 = vanilla
while j<len(vanilla):
    x2.append(j+1)
    j+=1

plt.plot(x2,y2, color="green", label="vanilla")

x3=[]
z=0
y3 = chocolate
while z<len(chocolate):
    x3.append(z+1)
    z+=1
plt.plot(x3,y3, color="blue", label="cocolate")

plt.title("Incomes from 3 different products")

plt.xlabel("# of customers purchased")
plt.ylabel("Income in USD")
plt.legend()
plt.show()



