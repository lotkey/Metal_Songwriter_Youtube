from test import generate
import random

scale = [[0, 2, 3, 5, 7, 8, 10],
         [24, 26, 67, 69, 48, 43]]

for i in range(0, len(scale[0])):
    scale[0][i] += 40 + random.randint(0, 8)

num = int(input("How many songs do you want to generate? "))
for i in range(0, num):
    generate(scale)
