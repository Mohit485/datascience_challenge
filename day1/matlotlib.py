import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[2,5,8,3,4]
y=[5,3,9,3,2]
r=plt.plot(x,y, 'r', label= 'constant', linestyle='--', marker= 'o', markeredgecolor='green', linewidth='3', markersize='20' )#legend
x1= np.arange(1,8,2)
#print(x1)
q=plt.plot(x1, x1**2, label= 'x^2')

#plt.show(r)
#add title and labels
plt.title('example plot of line chart', fontdict= {'fontname': 'Comic Sans MS', 'fontsize': 14})
plt.xlabel('x-->')
plt.ylabel('y-->')
plt.legend()
plt.show(r)
plt.show(q)
plt.savefig('myfig1.png', dpi=500)

# BAR GRAPH
labels= ['sdf', 'jkl', 'ert']
values= [7,2,4]
i=plt.bar(labels, values, )
pat= ['/', 'o', '*']
for bar in i:
    bar.set_hatch(pat.pop(0))
plt.show()
