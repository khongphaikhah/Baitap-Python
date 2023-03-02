import math
def luuFile():
    file=open('input.txt', 'w', encoding='utf-8')
    file.writelines("1 2 3 5 6\n")
    file.writelines("15 16 17 18\n")
    file.writelines("17 18 15 16\n")
    file.writelines("89 98 34 26\n")
    file.writelines("79 45 54 65\n")
    file.writelines("11 15 17 18\n")
    file.writelines("19 16 19 19\n")
    file.writelines("56 19 15 19\n")
    file.writelines("88 12 19 20\n")
    file.close()


def docFile():
    file = open('input.txt', 'r', encoding='utf-8')
    a = []
    for line in file:
        for so in line.split():
            a.append(int(so.strip())) 
    file.close()
    return a

def soNT(n):
    snt = 1
    if n < 2:
        return 0
    for s in range(2, round(math.sqrt(n))):
        if n % s == 0:
            snt = 0
            break
        return snt
snt =0
sochan =0
sole=0
arr = docFile()
solaplai=arr[0]
solanlap=0
for n in arr:
    if n % 2 == 0:
        sochan+=1
    else:
        sole+=1
    if arr.count(n) > solanlap:
        solaplai = n
        solanlap = arr.count(n)
    if soNT(n) ==1:
        snt+=1

print('Co %d so chan' %sochan)
print('Co %d so le' %sole)
print('Co %d so nguyen to' %snt)
print('So {a} lap lai {al} lan'.format(a = solaplai , al = solanlap))       
        
        

