#201
# def f(a):
#     s=0
    
#     for i in str(a):
#         s+=int(i)
#     if s<10:
#         return s
#     else:
#         return f(s)
# a,b=input().split()
# j=f(a) 
# g=f(b)       
# print(j,g)

# #202
# def f(a):
#     s=0
#     for i in str(a):
#         s+=int(i)
#     if s<10:
#         return s
#     else :
#         return f(s)

# n=int(input())
# a=list(map(int,input().split()))
# s=0

# for i in range(n):
#     p=1
#     for j in range(i+1):
#         p*=a[j]
#     s+=p    
# print(f(s))



#206

# def gcd(a, b):
#     if a == 0 :
#         return b
     
#     return gcd(b%a, a)
# a,b=map(int,input().split())    
# print(gcd(a,b))


#208
# def gcd(a, b):
#     if a == 0 :
#         return b
     
#     return gcd(b%a, a)
# n=int(input())
# l=list(map(int,input().split()))   
# ekub=l[0]
# for i in range(1,len(l)):

#     ekub = gcd(ekub, l[i])
# print(ekub)   

#220
# n=int(input())
# l=list(map(int,input().split()))   
# j=min(l)
# z=max(l)
# for i in range(n):
#     if l[i]==j :
#         l[i]=z
#     elif l[i]==z:
#        l[i]=j
            
#     print(l[i],end=' ')

# def kub(k):
#     return k**3
# a,b,c,d,f=map(float,input().split())
# print()    




# def i(n):
#     a=str(n)        
#     j= len(a)
#     c=0
#     for i in a:
#         c+=int(i)
#     return j,c
# a,b,c=map(int,input().split())
# print(i(a),i(b),i(c))



#jarima 
# def jarima(n):
#     if n<=70:
        
#         return 0
#     elif 90>=n>70:
        
#         return 1
#     elif 110>=n>=90:
       
#         return 5
#     else:
#         return 10
# n=int(input())
# d=jarima(n)*220000
# print(d)

# def k(n):
#     if n%7==1:


#         y="Dushanba"
#         return y
#     elif n%7==2:
#         y="seshanba"
#         return y
#     elif n%7==3:
#         y="Chorsanba"
#         return y
#     elif n%7==4:
#         y="Payshanba"
#         return y
#     elif n%7==5:
#         y="Juma"
#         return y
#     elif n%7==6:
#         y="Shanba"
#         return y
#     elif n%7==0:
#         y="Yakshanba"
#         return y
# n=int(input())
# print(k(n))

# def ekub(a,b):
#     if a==0:
#         return b
#     else :
#         return ekub(b%a, a)   
# a,b=map(int,input().split()) 
# EKUK=(a*b)/ekub(a,b)
# print(int(EKUK))
# def ekub(a,b):
#     if a==0:
#         return b
    
#     else :
#         return ekub(b%a, a) 
   
# n=int(input())
# l=list(map(int,input().split()))

# for i in range(1,n+1):
#     ek=(l[i-1]*l[i])/(ekub(l[i-1],l[i]))
# print(ek)



# 215
# n=int(input())
# c=1
# for i in range(1,n):

#     if n%i==0:
#         c+=1
# print(c)

# from math import *
# a,b,c,x,y=map(float,input().split())
# j=x**(1/6)+sqrt(a*a+b*b)+log(y)/(log(x)*c**3)-abs(sin(x)+cos(y))+2/5
# print("%.3f" %j)

#217
import matrrix 
matrrix.



#214
# a,b,c=map(float,input().split())
# p=(a+b+c)/2
# s=(p*(p-a)*(p-b)*(p-c))**(1/2)
# print("%.3f" %s)




