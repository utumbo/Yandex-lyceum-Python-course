num_arrays = int(input())
min_height = None
min_array_num = 0

for array_num in range(1, num_arrays + 1):
    while True:
        height = int(input())
        if height == 0:
            break
        if height < 0:
            print("Ущелье!")
            exit()
        if min_height is None or height <= min_height:
            min_height = height
            min_array_num = array_num

print(f"Наименьшая высота {min_height} в(о) {min_array_num}-м массиве.")