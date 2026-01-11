# world.py
import random

EMPTY = 0
AGENT = 1
GOAL = 2

class World:
    def __init__(self, size=50):
        self.size = size
        self.reset()

    def reset(self):
        self.grid = [[EMPTY for _ in range(self.size)] for _ in range(self.size)]

        self.agent_pos = self._random_empty_cell()
        self.goal_pos = self._random_empty_cell(exclude=[self.agent_pos])

        self._update_grid()

    def _random_empty_cell(self, exclude=None):
        if exclude is None:
            exclude = []

        while True:
            y = random.randint(0, self.size - 1)
            x = random.randint(0, self.size - 1)
            if (y, x) not in exclude:
                return [y, x]

    def _update_grid(self):
        for y in range(self.size):
            for x in range(self.size):
                self.grid[y][x] = EMPTY

        ay, ax = self.agent_pos
        gy, gx = self.goal_pos

        self.grid[ay][ax] = AGENT
        self.grid[gy][gx] = GOAL

    def move_agent(self, action):
        """
        action:
        0 = up
        1 = down
        2 = left
        3 = right
        """
        y, x = self.agent_pos

        if action == 0: y -= 1
        elif action == 1: y += 1
        elif action == 2: x -= 1
        elif action == 3: x += 1

        # clip to world bounds
        y = max(0, min(self.size - 1, y))
        x = max(0, min(self.size - 1, x))

        self.agent_pos = [y, x]

        reward = 0
        if self.agent_pos == self.goal_pos:
            reward = 1
            self.goal_pos = self._random_empty_cell(exclude=[self.agent_pos])

        self._update_grid()
        return reward
