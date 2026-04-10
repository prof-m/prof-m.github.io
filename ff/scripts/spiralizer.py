import sys
import numpy as np
import math
# import matplotlib.pyplot as plt
import pyperclip
def normalize(arr):
    std = (arr - min(arr))/(max(arr) - min(arr))
    return (std - 0.5) * 2
# constants of the spiral equation, from wikipedia:
# Changing the parameter a moves the centerpoint of the spiral outward from the origin (positive a toward θ = 0 and negative a toward θ = π), while b controls the distance between loops.
a = 0
b = -2.4
# first param is a file containing the phrases (one per line)
f = open(sys.argv[1])
words = f.readlines()
# second param is optional scale factor
scale = float(sys.argv[2]) if len(sys.argv) >= 3 else 75
# third param is optional number of turns of spiral
turns = float(sys.argv[3]) if len(sys.argv) >= 4 else 2
# fourth param is optional, toggle direction of spiral
reverse = (len(sys.argv) >= 5)
# make a linspace with values for each word
T = np.linspace(0, 2 * turns * math.pi, len(words))
# calculate x and y positions of each word
X = [(a + b * t) * math.cos(t) for t in T]
Y = [(a + b * t) * math.sin(t) for t in T]
# scale
X = [int(x) for x in normalize(X) * scale]
Y = [int(y) for y in normalize(Y) * scale]
# default is spiral inwards
if not reverse:
    X = reversed(X)
    Y = reversed(Y)
# print(list(zip(X,Y)))
# plt.plot(X,Y)
# plt.show()
# convert to flipflip caption format
output = "\n".join([f"setBlinkX {x}\nsetBlinkY {y}\nblink {word}\n" for x,y,word in zip(X,Y, words)])
print(output)
# dump to clipboard
pyperclip.copy(output)