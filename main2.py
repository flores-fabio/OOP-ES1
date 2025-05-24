from rettangolo import Rettangolo

r1 = Rettangolo(4, 3, "giallo")
r2 = Rettangolo(5, 8, "verde")
r3 = Rettangolo(6, 2, "blu")

media_r = (r1.area()+r2.area()+r3.area())/3

print("Area del rettangolo: ", r1.area())
print("Area del rettangolo: ", r2.area())
print("Area del rettangolo: ", r3.area())
print("Media delle aree dei rettangoli: ", media_r)