num = int(input("Enter the No Of Test Cases:- "))
for i in range(num):
   count = 0
   """num,k = list(map(int,input().split()))"""
   num = int(input("Total number of players between them:- "))
   k = int(input("Height of Ali & Gi-Hun:- "))
   heights = list(map(int,input(f"Enter the {num}'s players heights:- ").split()))
   for i in heights:
       if i > k:
           count+=1
   print(count)
