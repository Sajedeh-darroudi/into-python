import math
def Area(A, B, C, D, E):
    if D == 0:
        p = (A + B + C)/2
        Triangle_Area = math.sqrt(p * (p-A) * (p-B) * (p-C))
        return Triangle_Area
    elif (A!=0) and (B!=0) and (C!=0) and (D!=0) and (E!=0):
         p1 = (A + D + E)/2
         p2 = (B + C + E)/2
         quadrilateral_Area_1 = math.sqrt(p1 * (p1-A) * (p1-D) * (p1-E))
         quadrilateral_Area_2 = math.sqrt(p2 * (p2-B) * (p2-C) * (p2-E))
         quadrilateral_Area = quadrilateral_Area_1 + quadrilateral_Area_2
         return quadrilateral_Area
        
       
print(Area(4, 6, 8, 0, 0))         
print(Area(3, 6, 4, 5, 7))
