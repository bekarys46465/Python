import math

def degree_to_radian(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees_input = 15
radian_output = degree_to_radian(degrees_input)
print("Input degree:", degrees_input)
print("Output radian:", radian_output)
