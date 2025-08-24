# Question: Calculate sum of areas of two triangles
# This code calculates the areas of two triangles using their base and height,
# sums the areas, and prints the total area of the two triangles.
def area_triangle(base,height):
    return base*height/2

area_a=area_triangle(5,4)
area_b = area_triangle(7,6)
sum_1 = area_a + area_b
print("The sum of two triangle areas is: " +str(sum_1)) 

'''
Created on Jul 17, 2023

@author: APisal
'''