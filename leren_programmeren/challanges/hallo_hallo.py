double = input("2 woordige zin aub: ")
double_double = ""

for c in double:
    if c == " ":
        double_double += c
        double3 = double_double
        double_double = " "
    else:
        double_double += c

print (double3 + double + double_double)