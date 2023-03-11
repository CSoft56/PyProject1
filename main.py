
def max_arg(l):
   return max(l)
res=max_arg([10,20,60,100,50])
print(res)

def dup_arg(l):
   return [set(l)]
res=dup_arg([10,20,10,50,60,100])
print(res)

d1={'a':10, 'b':20}
d2={'c':30, 'e':40}
k=d1.keys()
d3=dict(d1.items())
d3.update(d2)
print(d3)

s=[1,2,3,4,2,6,6,8]
def oddnum_arg(s):
   for a in s:
      if a%2==1:
         print(a)

oddnum_arg(s)

n=int(input('enter a number to check whether it is prime or not:'))
def primenum_arg(n):
   c=0
   for i in range(1,n+1):
      if n %i==0:
         c+=1
   if c==2:
      print('the number is prime number')
   else:
      print('the number is not prime number')
primenum_arg(n)



