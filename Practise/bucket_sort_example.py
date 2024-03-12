from collections import Counter
# def solution(s):
#     map = Counter(s)
s='ssasgqysy'
count = Counter(s)
arr =[]
for char,val in count.items():
    arr.append((char,val))
arr.sort()
print(arr)
