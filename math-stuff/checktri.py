# a simple program to check if the triangle is possible to draw
sides = [1, 1, 1]
if sides[0] + sides[1] > sides[2] and sides[0] - sides[1] < sides[2]:
  print("Triangle is possible")
else:
  print("Triangle is not possible")
