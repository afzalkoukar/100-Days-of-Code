import math

def paint_calc(height, width, cover):
    return (height*width)/cover



test_h = int(input("Height of the wall: \n"))
test_w = int(input("Width of the wall: \n"))

coverage = 5

total_cans = math.ceil(paint_calc(test_h, test_w, coverage))

print(f"total no of cans required are {total_cans}")


