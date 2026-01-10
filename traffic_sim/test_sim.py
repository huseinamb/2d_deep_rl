from world import World
from simulate import step as simulate_step
from render import render
import numpy as np
import time

# Initialize world
world = World()

# No need to call spawn_car(), cars are created in the constructor
# If you want to spawn more cars, you could add a method in World

for _ in range(100):
    # example: agent moves 0.02 per step up
    simulate_step(world, action=np.array([1.0]))  
    render(world)
    time.sleep(0.05)
