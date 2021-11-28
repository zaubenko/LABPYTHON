#Напишите программу в которой обьявите короткое целое со значением  12345 и определите путем  выполнения битовых операций установлены
# ли в нем 1, 7 и 10 биты.
def bit(k):
    number=12345
    m=1<<k
    tmp=(number&m)>>k
    print(tmp)
x=int(input("input bit-1,7 or 10: "))
if x ==1:
    if bit(x)==0:
        print("bit 1 not ")
    else:
        print("ok")
elif x==7:
    if bit(x)==0:
        print("bit 7 not")
    else:
        print("ok")
elif x==10:
    if bit(x)==0:
        print("bit 10 not")
    else:
        print("ok")