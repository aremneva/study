import hashlib
d={143:’Apple, 267:’Sun’,333:’Gold’,499:’Cat’,564:’Winter’}
k=input(“Введите кодовое слово:”)
for key,value in d.items():
    if value==k:
        print(key,”:”)
        hash=hashlib.md5(k.encode())
        print(hash.hexdigest())
