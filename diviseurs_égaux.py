#Program that displays two numbers whose divisor sums are equal
n=int(input("Veuillez entrer un entier : "))
m=int(input("Veuillez entrer un deuxième entier : "))
d1=0
d2=0
for i in range(2,n+1):
    if(n % i ==0):
        d1=d1+1
for i in range(2,m+1):
    if(n % i ==0):
        d2=d2+1
print(f"Les diviseurs de {n} est : {d1}")
print(f"Les diviseurs de {m} est : {d2}")
if(d1==d2):
    print(f"Les deux entietrs {n} et {m} sont amis")
else:
    print(f"Les deux entietrs {n} et {m} ne sont pas amis")
