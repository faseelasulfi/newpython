def factorial():
  n=int(input("enter a number"))
  fact=1
  for i in range(1,n+1):
       fact=i*fact
  print(fact)
# factorial()

# def lcm():
#     a=int(input("enter a number"))
#     b=int(input("enter another number"))
#     hcf=1
#     for i in range(a,b):
#         if a%i==0 and b%i==0:
            
#             print()

# def prime():
#     a=int(input("enter a number"))
#     if a>1:
#      for i in range(2,a):
#          if a%i==0:
#           print(a,"is not prime")
#           break
#     else:
#      print(a,"is prime")
# # prime()        

def squarerroot():
   n=int(input("enter a number"))
   for i in range(n):
      if i*i==n:
       print(i)
      else:
         print("no squareroot")
# squarerroot()      

# def triangle_area():
#    a=int(input("enter a side"))   
#    b=int(input("enter second side"))   
#    c=int(input("enter third side"))   
#    while s!=0:
#       s=(a+b+c)/2
#       area=s*
   

def multi_table():
      n=int(input("enter a number"))
      for i in range(1,11):
         m=i*n
         print(i,"*",n,"=",m)
# multi_table()