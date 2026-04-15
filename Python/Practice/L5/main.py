def area_sum(rectangles):
    area = 0
    for height in rectangles:
        area += height["height"] *height["width"]
    return area
"""
Assignment
Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

{
  "height": 5,
  "width": 6
}

It should calculate the area of each rectangle and return the sum of all the areas.
"""