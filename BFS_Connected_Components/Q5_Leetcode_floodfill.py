from collections import deque

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]



def is_in_bounds(colors, row, col):
    num_rows, num_cols = len(colors), len(colors[0])

    is_row_in_bounds = row >= 0 and row < num_rows 
    is_col_in_bounds = col >= 0 and col < num_cols
    is_in_bounds = is_row_in_bounds and is_col_in_bounds

    return is_in_bounds


def traverse_image_from(start_row, start_col, seen, image):
    queue = deque([(start_row, start_col)])
    seen.add((start_row, start_col))
    
    while queue:
        for level in range(len(queue)):
            current_row, current_col = queue.popleft()

            for delta_row, delta_col in directions:
                next_row, next_col = current_row + delta_row, current_col + delta_col

                if not is_in_bounds(image, next_row, next_col):continue
                is_seen = (next_row, next_col) in seen
                is_same_color = image[next_row][next_col] == image[current_row][current_col]
                
                if  not is_seen and is_same_color:
                    queue.append((next_row, next_col))
                    seen.add((next_row, next_col))
    

def floodFill(image, sr, sc, color):
    num_rows, num_cols = len(image), len(image[0])
    seen = set()

    traverse_image_from(sr, sc, seen, image)  

    for row, col in list(seen):
        image[row][col] = color
        
    return image
                
        

if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr,sc, color = 1, 1, 2
    print(floodFill(image, sr, sc, color))
                
                