import math
import argparse
parser = argparse.ArgumentParser(description="Calculate area and circumference of a circle")
parser.add_argument('radius', type=float, help="Radius of the circle")
args = parser.parse_args()
radius = args.radius
area = math.pi * radius**2
circumference = 2 * math.pi * radius
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
