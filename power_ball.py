import random
from operator import index

red_balls = list(range(1,34))
selected_ball = []

for _ in range(6):
    balls = random.randrange(len(red_balls))
    selected_ball.append(red_balls.pop(balls))
print(f"red balls: {str(selected_ball)}")

blue_ball = random.randrange(1,17)
print(f"blue ball: {blue_ball}")