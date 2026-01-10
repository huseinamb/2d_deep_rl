import gymnasium as gym
from gymnasium import spaces
import numpy as np
from world import World
from simulate import step as simulate_step  # our fixed simulate_step

class TrafficEnv(gym.Env):
    """Custom Gym environment for traffic simulation."""

    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super().__init__()

        # Initialize the world
        self.world = World()

        # Agent can move vertically: dy ∈ [-1, 1]
        self.action_space = spaces.Box(
            low=-1.0, high=1.0, shape=(1,), dtype=np.float32
        )

        # Observation space:
        # - agent position (x, y)
        # - goal position (x, y)
        # - positions of nearest 3 cars in same lane (y offsets)
        # Shape = 2 + 2 + 3 = 7
        low = np.array([-1.0] * 7, dtype=np.float32)
        high = np.array([1.0] * 7, dtype=np.float32)
        self.observation_space = spaces.Box(low=low, high=high, dtype=np.float32)

        self.max_steps = 200
        self.steps = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.world.reset()  # resets agent, traffic cars, lanes
        self.steps = 0
        return self._get_obs(), {}

    def _get_obs(self):
        """Build observation vector for the agent."""
        agent_pos = self.world.agent.position
        goal_pos = self.world.goal

        # get y offsets of nearest 3 cars in the agent's lane
        agent_lane = self.world.agent_lane_index
        cars = self.world.lanes[agent_lane].cars
        car_offsets = []
        for car in cars[:3]:
            car_offsets.append(car.position[1] - agent_pos[1])
        while len(car_offsets) < 3:
            car_offsets.append(1.0)  # far away
        obs = np.concatenate([agent_pos, goal_pos, np.array(car_offsets)])
        return obs.astype(np.float32)

    def step(self, action):
        self.steps += 1

        # Clip action
        action = np.clip(action, -1.0, 1.0)

        # Update world
        simulate_step(self.world, action)

        # Compute reward
        dist_to_goal = np.linalg.norm(self.world.agent.position - self.world.goal)
        reward = 1.0 - dist_to_goal  # closer to goal = higher reward

        # Collision penalty
        done = False
        if self.world.check_collision():
            reward -= 0.5  # small negative reward
            done = True

        # Max steps reached
        if self.steps >= self.max_steps:
            done = True

        obs = self._get_obs()
        truncated = False  # not using truncated for now

        return obs, reward, done, truncated, {}

    def render(self, mode="human"):
        from render import render
        render(self.world)
