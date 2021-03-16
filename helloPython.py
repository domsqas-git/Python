print("Hello world")

hours = input("Enter Hours:")
h = float(hours)
pph = input("Enter Rate:")
r = float(pph)

if h<= 40 :
    print(h * r)
else :
    print(((h-40)*1.5*r) + (40*r))
