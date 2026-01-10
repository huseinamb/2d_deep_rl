# world.py
import numpy as np

class Lane:
    def __init__(self, position, direction="horizontal"):
        self.direction = direction  # "horizontal" or "vertical"
        if direction == "horizontal":
            self.y_pos = position
        else:
            self.x_pos = position
        self.cars = []

class Car:
    def __init__(self, position, speed=0.01, direction="horizontal"):
        self.position = np.array(position, dtype=np.float32)
        self.speed = speed
        self.direction = direction

class World:
    def __init__(self):
        # your existing initialization
        self.lanes = [
            Lane(-0.6, "horizontal"),
            Lane(-0.2, "horizontal"),
            Lane(0.2, "horizontal"),
            Lane(0.0, "vertical"),  # agent lane
        ]
        self.agent_lane_index = 3  # assuming 0-based index, last lane is vertical


        # save initial positions to reset later
        self.init_lane_positions = []
        for lane in self.lanes:
            if lane.direction == "horizontal":
                positions = [[-1 + i * 0.6, lane.y_pos] for i in range(3)]
                self.init_lane_positions.append(positions)
                for pos in positions:
                    lane.cars.append(Car(pos, speed=0.01, direction="horizontal"))

        # Place agent in vertical lane
        self.agent = Car([0.0, -1.0], speed=0.02, direction="vertical")
        self.init_agent_pos = np.array([0.0, -1.0], dtype=np.float32)

        # Goal at top of vertical lane
        self.goal = np.array([0.0, 1.0], dtype=np.float32)
        self.init_goal_pos = self.goal.copy()

    def reset(self):
        """Reset world for new episode."""
        # reset horizontal lane cars
        for lane, positions in zip(self.lanes, self.init_lane_positions):
            lane.cars = []
            for pos in positions:
                lane.cars.append(Car(pos.copy(), speed=0.01, direction="horizontal"))

        # reset agent
        self.agent.pos = self.init_agent_pos.copy()

        # reset goal
        self.goal = self.init_goal_pos.copy()
    def check_collision(self):
        """
        Returns True if the agent collides with any horizontal lane car.
        """
        #agent_x, agent_y = self.agent.pos
        agent_x, agent_y = self.agent.position

        for lane in self.lanes:
            if lane.direction == "horizontal":
                for car in lane.cars:
                   # car_x, car_y = car.pos
                    car_x, car_y = car.position

                    # Simple collision check: if distance < threshold
                    if abs(agent_x - car_x) < 0.05 and abs(agent_y - car_y) < 0.05:
                        return True
        return False

