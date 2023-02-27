from itertools import combinations_with_replacement
def combination_print():
    raw_inp = input()
    inp, param = raw_inp.split(" ")
    proc_inp = list(combinations_with_replacement(sorted(inp), int(param)))
    for i in proc_inp:
        for j in i:
            print(j,end='')
        print('', end='\n')

from itertools import groupby
def grouper_func():
    inp = input()
    for item, count in groupby(inp):
        print(f'({len(list(count))}, {item})', end = ' ')


from itertools import permutations, combinations


from itertools import combinations
def probability_comp():
##if __name__ == "__main__":
    target_char = 'a'
    length = int(input())
    input_str = input().split(" ")
    selected_index = int(input())

    combination_output = list(combinations(input_str, selected_index))
    counter = 0
    
    for item in combination_output:
        if target_char in item:
            counter += 1
            
    print(counter/len(combination_output))
    

def beautiful_numbers(list_size):

    base_container = []
    beautiful_counter = 0
    
    for i in range (1, list_size+1):
        base_container.append(i)

    for perm in permutations(base_container):
##        is_beautiful = True
##        for i in range (1, list_size+1):
##            if not (perm[i-1] % i == 0 or i % perm[i-1] == 0):
##                is_beautiful = False
##                break
##            
##        if is_beautiful:
##            beautiful_counter += 1

        beautiful_counter += 1

    print(f'list size {list_size}')
    print(f'Counted {beautiful_counter}')


def highestWall(wallPositions, wallHeights):
    
    max_concrete_position = wallPositions[-1]
    mud_wall_positions = []
    for wall in range(1, max_concrete_position+1):
        if not (wall in wallPositions):
            mud_wall_positions.append(f'm{wall}')
        else:
            height_idx = wallHeights[ wallPositions.index(wall) ]
            mud_wall_positions.append(f'h{height_idx}')

    new_mud_walls = mud_wall_positions.copy()
    mud_wall_count = 0
    start_idx = -1
    
    for idx, mud_wall in enumerate(mud_wall_positions):
        
        if 'm' in mud_wall:
            mud_wall_count += 1
            if start_idx == -1:
                start_idx = idx
        else:
            if mud_wall_count != 0:
                create_mud_walls(
                    mud_wall_count,
                    start_idx,
                    mud_wall_positions[start_idx-1]
                )
                start_idx = -1
                mud_wall_count = 0
        
                
    print(f'concrete walls {wallPositions}')
    print(f'concrete heights {wallHeights}')
    print(f'mud walls {mud_wall_positions}')


def create_mud_walls(count, start_idx, start_height):
    
    temp_mud_wall = []
    mud_height = int(start_height.replace('h', ''))
    
    for i in range(start_idx, start_idx + count):
        mud_height += 1
        temp_mud_wall.append(f'mw{mud_height}')
        

    print(f'temp mud walls {temp_mud_wall}')

# highestWall([1,2,7,9], [9,10,13,12])

def highestWall2(wallPositions, wallHeights):

    max_concrete_position = wallPositions[-1]
    mix_wall_heights = []
    normalized_wall_heights = []
    previous_wall_height = 0

    for wall in range(1, max_concrete_position + 1):

        if not (wall in wallPositions):
            ##Get the prev wall height
            previous_wall_height += 1
            mix_wall_heights.append(f'm{previous_wall_height}')
        else:
            previous_wall_height = wallHeights[wallPositions.index(wall)]
            mix_wall_heights.append(f'c{previous_wall_height}')

    normalized_wall_heights = mix_wall_heights[::-1].copy()

    for idx, wall in enumerate(mix_wall_heights[::-1]):
        if idx > 0:
            previous_wall_height = normalized_wall_heights[idx - 1].replace('m', '').replace('c', '')
            if int(wall.replace('m', '')) - int(previous_wall_height) > 1:
                wall = int(previous_wall_height) + 1
                normalized_wall_heights[idx] = f'm{wall}'

    print(mix_wall_heights)
    print(normalized_wall_heights)


def highestWall3(wallPositions, wallHeights):

    max_concrete_position = wallPositions[-1]
    mix_wall_heights = []
    normalized_wall_heights = []
    previous_wall_height = 0
    max_mud_wall_height = 0

    ## Create projected mud wall heights
    for wall in range(1, max_concrete_position + 1):
        if wall in wallPositions:
            height_idx = wallPositions.index(wall)
            previous_wall_height = wallHeights[height_idx]
            mix_wall_heights.append(previous_wall_height)
        else:
            previous_wall_height += 1
            mix_wall_heights.append(f'm{previous_wall_height}')

    print(mix_wall_heights)

    ##Normalize, incase theres a mud wall larger than adjacent concrete wall
    previous_wall_height = 0
    for wall in mix_wall_heights[::-1]:
        if type(wall) == str:
            if int(wall.replace('m', '')) - previous_wall_height > 1:
                previous_wall_height += 1
                normalized_wall_heights.append(f'm{previous_wall_height}')
            else:
                normalized_wall_heights.append(wall)
        else:
            previous_wall_height = wall
            normalized_wall_heights.append(previous_wall_height)

    print(normalized_wall_heights[::-1])

    ##Determine the maximum mud wall height
    for height in normalized_wall_heights:
        if type(height) == str:
            mud_wall_height = int(height.replace('m', ''))
            if mud_wall_height > max_mud_wall_height:
                max_mud_wall_height = mud_wall_height

    print(max_mud_wall_height)

# highestWall2([1,2,7,9], [9,10,13,12])
# highestWall3([1,2,4,7], [4,6,8,11])

highestWall3([1,9], [2,5])