import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def check( x1, y1,x2, y2, x3,  y3, x4, y4, x, y):
    A = area(x1, y1, x2, y2, x3, y3) + area(x1, y1, x4, y4, x3, y3)
    A1 = area(x, y, x1, y1, x2, y2)
    A2 = area(x, y, x2, y2, x3, y3)
    A3 = area(x, y, x3, y3, x4, y4)
    A4 = area(x, y, x1, y1, x4, y4)

    if (A == A1 + A2 + A3 + A4):
        return True
    else:
        return False





def area( x1,  y1, x2, y2,  x3,  y3):

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) +
                x3 * (y1 - y2)) / 2.0)


cities=pd.read_csv('cities.csv', delimiter = ',',skiprows=1,names=['city','top-left x','top-left y','bottom-right x','bottom-right y'])
# pr (cities['top-left x'])
x=[]
y=[]

for i in range(len(cities['top-left x'])):
    x.append(cities['top-left x'][i])
    x.append(cities['top-left x'][i])
    x.append(cities['bottom-right x'][i])
    x.append(cities['bottom-right x'][i])

for i in range(len(cities['top-left y'])):
    y.append(cities['top-left y'][i])
    y.append(cities['bottom-right y'][i])
    y.append(cities['bottom-right y'][i])
    y.append(cities['top-left y'][i])








inputs=pd.read_csv('points.csv', delimiter = ',',skiprows=1,names=['ID','x','y'])


output=""

counter=0
for j in range(0,len(x),4):
      counter+=1
      for k in range(len(inputs)):
        shape_X = x[j:j+4]
        shape_y = y[j:j+4]

        result=check(x[j],y[j],x[j+1],y[j+1],x[j+2],y[j+2],x[j+3],y[j+3],inputs['x'][k],inputs['y'][k])

        if(result==True):
            output+=str(inputs['ID'][k])+","+str(inputs['x'][k])+","+str(inputs['y'][k])+","+str(cities['city'][j%3])+'\n'
            print(output)
        else:
            output += str(inputs['ID'][k]) + "," + str(inputs['x'][k]) + "," + str(inputs['y'][k]) + "," +"None"+'\n'
            print(output)

            file = open('oputput.csv', 'w')
            file.write(output)
            file.close()















for i in range(0, len(x),4 ):
    plt.plot(x[i:i+4], y[i:i+4], 'ro-')

for k in range(len(inputs)):
    # pr (inputs['x'][k] ,"__",inputs['y'][k]
    plt.plot(inputs['x'][k], inputs['y'][k], '+')
plt.show()
