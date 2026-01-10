import numpy as np

def step(world, action):
    """
    Simulate one step in the traffic world.
    action: np.array([dy]) for agent movement along vertical lane
    """
    # Move agent vertically
    dy = float(np.clip(action[0], -1.0, 1.0))
    agent = world.agent
    agent.position[1] += dy * agent.speed  # move along vertical lane
    agent.position[1] = np.clip(agent.position[1], -1, 1)

    # Move cars in horizontal lanes
    for lane in world.lanes:
        if lane.direction == "horizontal":
            for car in lane.cars:
                car.position[0] += car.speed
                # Wrap around screen edges
                if car.position[0] > 1:
                    car.position[0] = -1
