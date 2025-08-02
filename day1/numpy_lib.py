import numpy as np
m= np.array([1,2,4,5])
print(m)
#mean
o=m.mean()
#standard deviation
e=m.std(m)
print(o)
print(e)
print(m.min()) #min
print(m.max()) #max
n= m[1:3]
print(n)
f= m[1::]
print(f)
u=np.random.random(10) #shows 10 radom umbers etween 0 & 1

u= np.random.randint(1,23)# shows a random int between given integers
print(u)
u= np.random.randint(1,10,9) # shows (start, end, no.of required element) 
print(u)
u=u.reshape(3,3) 
d=np.arange(0,6,2) #shows (start, ed, step)
g=np.linspace(1,6,5) #shows(start, ed, equal parts)
print(u)
print(d)
print(g)
