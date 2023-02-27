main_array = [
    [1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0]
]


def paint_fill(arr, x, y, new_value, prev_value=None):
    # Tag the target value
    current_value = arr[y][x]
    new_x = 0
    new_y = 0

    # Set the target value for the next recursion
    if prev_value is None:
        prev_value = current_value

    # Set the middle
    arr[y][x] = new_value

    # Set the Top
    new_x = x
    if y - 1 > -1:
        new_y = y - 1
        if arr[new_y][new_x] == prev_value:
            arr = paint_fill(arr, new_x, new_y, new_value, prev_value)

    # Set the Bottom
    if y + 1 < len(arr):
        new_y = y + 1
        if arr[new_y][new_x] == prev_value:
            arr = paint_fill(arr, new_x, new_y, new_value, prev_value)

    # Set the left
    new_y = y
    if x - 1 > -1:
        new_x = x - 1
        if arr[new_y][new_x] == prev_value:
            arr = paint_fill(arr, new_x, new_y, new_value, prev_value)

    # Set the Right
    if x + 1 < len(arr[0]):
        new_x = x + 1
        if arr[new_y][new_x] == prev_value:
            arr = paint_fill(arr, new_x, new_y, new_value, prev_value)

    return arr

def start_main():
    # Use a breakpoint in the code line below to debug your script
    x = 2
    y = 5
    newValue = 7
    modified_array = []

    print('Original array')
    for row in main_array:
        print(row)

    print()

    modified_array = paint_fill(main_array, x, y, newValue)

    print('Painted array')
    for row in modified_array:
        print(row)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_main()

