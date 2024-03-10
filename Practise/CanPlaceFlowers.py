flowerbed = [0,0,1,0,1]
# flowerbed=[0,1,0,0]
n=1
x = len(flowerbed)
if len(flowerbed)%2==0:
    print((n+flowerbed.count(1)) == x//2)
else:
    if flowerbed[0] == 1:
        print((n+flowerbed.count(1)) == (x//2)+1)
    else:
        print((n+flowerbed.count(1)) == (x//2))
        