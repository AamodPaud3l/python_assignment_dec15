#Program to solve a y = mx + c having various values of x
x_values = [1, 2.3, 5.6, 7, 78]

def solve_for_y(values):
    m = 45
    c = 0.5
    for x in values:
        y = m * x + c
        print("For x={0}, y= {1:.2f}".format(x,y))
solve_for_y(x_values)
