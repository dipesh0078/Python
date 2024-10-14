#18.Write a function calculate_area(shape, dimension) that calculates the
#area of a shape (circle, square, or rectangle) based on the given
#dimensions.

import math

def calculate_area(shape,*args):
    if shape.lower()=='circle':
        radius=args[0]
        return math.pi*radius**2
    elif shape.lower()=='square':
        if len(args)!=1:
            return 'Square requires 1 dimension'
        side=args[0]
        return side*side
    elif shape.lower()=='rectangle':
        if len(args)!=2:
            return 'Rectangel has length and breadth'
        length,width=args
        return length*width
    else:
        return "Invalid shape"
    
print(calculate_area('circle', 5))           
print(calculate_area('square', 4))             
print(calculate_area('rectangle', 3, 5))        
print(calculate_area('rectangle', 3))