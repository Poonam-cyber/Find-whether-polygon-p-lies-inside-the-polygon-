# Task-1 
#Question 1 : Check if the given point lies inside or outside a polygon ?
# I believe in smart work rather than hard work because already there are so many inbuilt libraries available in python so why can't just we use it.

import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def Find_p(coord,find_cord):
	point = Point(find_cord)
	polygon = Polygon(coord)
	ans=polygon.contains(point)
	return ans
coord=[]
n=int(input("input how many co-ordinates?"))
for x in range(n):
    cord_list=[]
    cor_x=int(input("Enter cordinate x"))
    cor_y=int(input("Enter cordinate y"))
    cord_list.append(cor_x)
    cord_list.append(cor_y)
    coord.append(cord_list)
coord.append(coord[0])
xs, ys = zip(*coord) 
plt.figure()
plt.plot(xs,ys)
plt.show()
find_cord=[]
find_cord.append(int(input("Enter x co-ordinate")))
find_cord.append(int(input("Enter y co-ordinate")))
check=Find_p(coord,find_cord)
print(check)