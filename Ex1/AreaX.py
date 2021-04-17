import math
def AreaX(A, B, C, D, E):
    if (A!=0) and (B!=0) and (C!=0) and (D!=0) and (E!=0):
        p1 = (A + D + E) / 2
        p2 = (B + C + E) / 2
        quadrilateral_Area_1 = math.sqrt(p1 * (p1 - A) * (p1 - D) * (p1 - E))
        quadrilateral_Area_2 = math.sqrt(p2 * (p2 - B) * (p2 - C) * (p2 - E))
        quadrilateral_Area = quadrilateral_Area_1 + quadrilateral_Area_2
        return quadrilateral_Area
    sides = [A, B, C, D]
    for side in sides:
        if side == 0:
            sides.remove(side)
            if len(sides) == 3:
                p = sum(sides) / 2
                Triangle_Area = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
                return Triangle_Area
                
                
print(AreaX(3, 6, 4, 5, 7))
print(AreaX(0, 6, 4, 5, 0))
