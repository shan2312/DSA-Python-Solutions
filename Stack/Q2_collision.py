def asteroidCollision(asteroids):
    stack = []
    i = 0
    
    while i < len(asteroids):
        
        asteroid_size = asteroids[i]
        
        if stack:
            nearest_asteroid_size = stack[-1]
            
        if not stack or nearest_asteroid_size < 0 or asteroid_size > 0:
            stack.append(asteroid_size)
            i += 1
            continue
            
        if abs(asteroid_size) < abs(nearest_asteroid_size):
            i += 1
            continue
            
        if abs(asteroid_size) == abs(nearest_asteroid_size):
            stack.pop()
            i += 1
            continue
            
        if abs(asteroid_size) > abs(nearest_asteroid_size):
            stack.pop()
            
    return stack
        
        
            
if __name__ == '__main__':
    print(asteroidCollision([1,5,10,-12,22,-2]))
    print(asteroidCollision([5,10,-5]))      
        
            
            
    