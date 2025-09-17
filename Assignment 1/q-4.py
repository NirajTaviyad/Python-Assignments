import math

angles = [0, 30, 45, 60, 90]
print("Angle |  sin   |  cos   |  tan")
print("------------------------------------")
for a in angles:
    rad = math.radians(a)
    s = math.sin(rad)
    c = math.cos(rad)
    if abs(c) < 1e-9:
        t = "undef"
    else:
        t = round(math.tan(rad), 4)
    print(f"{a:>5}° | {round(s,4):>7} | {round(c,4):>7} | {t:>7}")
