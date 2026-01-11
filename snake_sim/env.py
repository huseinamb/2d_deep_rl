# env.py
import gymnasium as gym
from gymnasium import spaces
import numpy as np
from world import World

class SnakeEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, size=50):
        super().__init__()

        self.world = World(size=size)
        self.size = size
        self.goals_reached = 0
        self.max_goals = 3


        # 4 discrete actions
        self.action_space = spaces.Discrete(4)

        # Observation: agent (y,x), goal (y,x) normalized
        self.observation_space = spaces.Box(
            low=0.0,
            high=1.0,
            shape=(4,),
            dtype=np.float32
        )

        self.max_steps = size * size
        self.steps = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.world.reset()
        self.steps = 0
        self.goals_reached = 0

        return self._get_obs(), {}

    def _get_obs(self):
        ay, ax = self.world.agent_pos
        gy, gx = self.world.goal_pos

        return np.array([
            ay / self.size,
            ax / self.size,
            gy / self.size,
            gx / self.size
        ], dtype=np.float32)

    def step(self, action):
        self.steps += 1

        # Previous position
        prev_y, prev_x = self.world.agent_pos
        goal_y, goal_x = self.world.goal_pos

        prev_dist = abs(prev_y - goal_y) + abs(prev_x - goal_x)

        # Move agent
        ay, ax = prev_y, prev_x
        if action == 0:   # up
            ay -= 1
        elif action == 1: # down
            ay += 1
        elif action == 2: # left
            ax -= 1
        elif action == 3: # right
            ax += 1

        ay = np.clip(ay, 0, self.size - 1)
        ax = np.clip(ax, 0, self.size - 1)

        self.world.agent_pos = [ay, ax]
        self.world._update_grid()

        # Distance-based reward
        new_dist = abs(ay - goal_y) + abs(ax - goal_x)
        reward = prev_dist - new_dist   # +1 closer, -1 farther

        terminated = False

        # Goal reached
        if self.world.agent_pos == self.world.goal_pos:
            reward += 10.0
            self.goals_reached += 1

            # spawn new goal
            self.world.goal_pos = self.world._random_empty_cell(
                exclude=[self.world.agent_pos]
            )
            self.world._update_grid()

            if self.goals_reached >= self.max_goals:
                terminated = True


        truncated = self.steps >= self.max_steps

        return self._get_obs(), reward, terminated, truncated, {}


    def render(self):
        from render import render
        render(self.world)
