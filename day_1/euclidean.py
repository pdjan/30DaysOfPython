# task from 30DaysOfPython Challenge - day 1

import math

def euclidean_distance(x1, y1, x2, y2):
    # Calculate the distance using the Euclidean distance formula
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Example usage
x1, y1 = 1, 2
x2, y2 = 4, 6

distance = euclidean_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")
