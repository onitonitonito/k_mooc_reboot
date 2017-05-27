def choice():
	shape = int(input("type in shape(rectangle = 1, triangle = 2, circle = 3)"))
	if shape == 1:
		weight = int(input("\ntype in Rectangle Weight:"))
		height = int(input("type in Rectangle Height :"))
		return print(("Rectangle area is %d") %(weight*height))
	elif shape == 2:
		weight = int(input("\ntype in Triangle Weight:"))
		height = int(input("type in Triangle Height :"))
		return print(("Triangle area is %d") %(weight*height/2))
	elif shape == 3:
		diameter = int(input("\ntype in Circle diameter:"))
		return print(("Circle area is %d") %(diameter*diameter*3.14))
	else:
		print("Wrong number")
		choice()
