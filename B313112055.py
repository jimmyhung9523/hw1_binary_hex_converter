#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input('請輸入介於0到255之間的數'))
a = n-(2**7)
一=""
二=""
三=""
四=""
五=""
六=""
七=""
八=""
X=""
Y=""
A=""
B=""
C=""
D=""
E=""
F=""
if(a>=0):
  一=1
  b=a-(2**6)
else:
  一=0
  b=n-(2**6)
if(b>=0):
    二=1
    c=b-(2**5)
elif(a>=0 and b<0):
    二=0
    c=a-(2**5)
else:
    二=0
    c=n-(2**5)
if(c>=0):
      三=1
      d=c-(2**4)
elif(b>=0 and c<0):
      三=0
      d=b-(2**4)
else:
      三=0
      d=n-(2**4)
if(d>=0):
        四=1
        e=d-(2**3)
elif(c>=0 and d<0):
        四=0
        e=c-(2**3)
else:
        四=0
        e=n-(2**3)
if(e>=0):
          五=1
          f=e-(2**2)
elif(d>=0 and e<0):
          五=0
          f=d-(2**2)
else:
          五=0
          f=n-(2**2)
          print(五)
if(f>=0):
            六=1
            g=f-(2**1)
            print(六)
elif(e>=0 and f<0):
            六=0
            g=e-(2**1)
else:
            六=0
            g=n-(2**1)
if(g>=0):
              七=1
              h=g-(2**0)
elif(h>=0 and g<0):
              七=0
              h=f-(2**0)
else:
              七=0
              h=n-(2**0)
if(h>=0):
                八=1
elif(g==0 and h==0):
                八=0
else:
                八=0
x = 2**3*一+2**2*二+2**1*三+2**0*四
if(x<10):
                    X=x
else:
  if x-10==0:
    X="A"
  if x-10==1:
    X="B"
  if x-10==2:
    X="C"
  if x-10==3:
    X="D"
  if x-10==4:
    X="E"
  if x-10==5:
    X="F"
y = 2**3*五+2**2*六+2**1*七+2**0*八
if(y<10):
                    Y=y
else:
  if y-10==0:
                    Y="A"
  if y-10==1:
                    Y="B"
  if y-10==2:
                    Y="C"
  if y-10==3:
                    Y="D"
  if y-10==4:
                    Y="E"
  if y-10==5:
                    Y="F"

print("二進制為",一,二,三,四,五,六,七,八,"\n十六進制為",X,Y)


# In[ ]:




