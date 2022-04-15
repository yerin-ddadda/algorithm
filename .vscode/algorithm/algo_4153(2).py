import math

pita_print = []

while True:
    a,b,c = map(int, input().split())
    if math.sqrt(a**2 + b**2) == c and math.sqrt(b**2 + c**2) == a and math.sqrt(a**2 + c**2) == b:
        pita_print.append("right")


