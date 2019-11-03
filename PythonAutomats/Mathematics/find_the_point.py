"""Find point of rotation """
import math


def find_point(px, py, qx, qy, theta=180):
    xr = math.cos(theta) * (px - qx) - math.sin(theta) * (py - qy) + qx
    yr = math.sin(theta) * (px - qx) + math.cos(theta) * (py - qy) + qy
    return xr, yr


def find_point2(px, py, qx, qy):
    xr =(2* qx) -px
    yr =(2* qy) -py
    return [xr,yr]

print(find_point2(1,1,2,2))
print(find_point2(4,3,5,2))
print(find_point2(2,4,5,6))
print(find_point2(1,2,2,2))
print(find_point2(1,1,1,1))
print(find_point2(1,2,2,1))
print(find_point2(1,8,7,8))
print(find_point2(9,1,1,1))
print(find_point2(8,4,3,2))
print(find_point2(7,8,9,1))