#!/usr/bin/env python
# coding: utf-8

# In[13]:


#! python3
# - estimates the constant PI
import random
import math


def estimate_pi(number_of_points_in_square):
    number_of_points_in_circle = 0
    area_of_square = 4 

    for i in range(number_of_points_in_square):
        x_coordinate = random.uniform(-1, 1)
        y_coordinate = random.uniform(-1, 1)
        distance_point_to_origin = math.sqrt(x_coordinate ** 2 + y_coordinate ** 2)
        if (distance_point_to_origin <= 1):
            number_of_points_in_circle += 1
        # - else: do nothing; you understand!

    PI = (area_of_square * number_of_points_in_circle) / number_of_points_in_square
    PI = round(PI, 4)
    
    return PI


def Main():
    n = int(input('Number of Random values: '))
    print('PI estimate = ' + str(estimate_pi(n)))


Main()


# In[ ]:




