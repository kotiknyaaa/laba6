import random
while True:
    n=input("Введите длину списка в виде натурального числа:")
    if n.isdigit():
        if int(n)!=0:
            n=int(n)
            break

if n==1:
    print("Частный случай. Произведение эл-ов списка после макс. эл-а и сумма эл-ов списка между отрицательными эл-ами равно 0")
else:
    sp=[]
    summa=0
    proizv=0
    pos=" "
    posotric1=" "
    posotric2=" "
    mx=-1
    for _ in range(n):
        sp.append(random.randint(-10,10))
    print('Список:', sp, sep=" ")


    for i in range(n):
        if mx<abs(sp[i]):
            mx=abs(sp[i])
            pos=i
        if sp[i]<0 and posotric1==" ":
            posotric1=i
        if sp[i]<0:
            posotric2=i

    if pos+1!=n:
        proizv=sp[pos+1]
        for j in range(pos+2,n):
            proizv=proizv*sp[j]

    for k in range(posotric1+1,posotric2):
        summa+=sp[k]
    print(mx)
    print(pos)
    print(posotric1)
    print(posotric2)
    print("Произведение эл-ов списка после макс. эл-а:", proizv,sep=" ")
    print("Сумма эл-ов списка между отрицательными эл-ами:", summa,sep=" ")