# coordinates_9_13.py
# python3 no longer takes tuples as function parameters
def coordinateline(x1,y1,x2,y2,x):
    m = (y2-y1)/(x2-x1)
    y = m*(x-x1) + y1
    return y