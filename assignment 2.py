num = int(input())
for i in range(num):
   count = 0
   num,k = list(map(int,input().split()))
   heights = list(map(int,input().split()))
   for i in heights:
       if i > k:
           count+=1
   print(count)