import random, matplotlib.pyplot as plt
result = []
height = 20                             # number of pin rows in the board
balls = 100000                          # number of balls to drop

for i in range(balls):
    position = 0                        # start in top middle of grid
    for j in range(height):
        direc = random.randint(0, 1)
        if direc == 1: position += 1    # ball bounces off pin to the right
        elif direc == 0: position -= 1  # ball bounces off pin to the left
    result.append(position)

plt.hist(result, bins=range(1-height,height,2))
plt.show()
