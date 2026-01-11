# test.py
import pygame
from world import World
from render import render
import random

world = World(size=50)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    action = random.randint(0, 3)
    world.move_agent(action)
    render(world)
