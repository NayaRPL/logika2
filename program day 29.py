print("angka yang paling besar di antar 3 angka")
a=int(input("masukkan a:"))
b=int(input("masukkan b:"))
c=int(input("masukkan c:"))
if a >b and a>c:
    print("nilai a paling besar")
elif a<b and b>c:
    print("nilai b pling besar ")
elif a<c and c>b:
    print("nilai c yang paling besar")
else :
    print("nilai yang anda masukkan sama ")

print("angka yang paling kecil di antar 3 angka")
c=int(input("masukkan c:"))
d=int(input("masukkan d:"))
e=int(input("masukkan e:"))
if c<d and c<e:
    print("nilai a paling kecil")
elif c>d and d<e:
    print("nilai b yang paling kecil")
elif c>e and d>e:
    print("nilai c yang paling kecil")
else:
    print("nilai yang anda masukkan nilainya sama")

print("mencari nili yang berada di tengah")

a1=int(input("masukkan a1:"))
b1=int(input("masukkan b1:"))
c1=int(input("masukkan c1:"))
if (b1>a1>c1) or (c1>a1>b1):
    print("nili a1")
elif (a1>b1>c1) or (c1>b1>a1):
    print("nilai b1")
else :
    print("nilai c")

    

