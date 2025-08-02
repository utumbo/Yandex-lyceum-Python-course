initial_height = int(input())
height_mountain = int(input())
step = int(input())

heights = []

while initial_height <= height_mountain:
    heights.append(initial_height)
    initial_height += step

current_height = height_mountain
while current_height > initial_height:
    current_height -= (step + 1)
    if current_height >= initial_height:  
        heights.append(current_height)

print(" ".join(map(str, heights)))