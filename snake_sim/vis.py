#visualize after training
import numpy as np
from env import SnakeEnv
from stable_baselines3 import PPO
import time
from render import render

env = SnakeEnv()
model = PPO.load("ppo_traffic_model_50000")  # load trained model

obs, _ = env.reset()
done = False
truncated = False

# Keep track of positions for visualization if needed
agent_positions = []

while not done and not truncated:
    action, _ = model.predict(obs, deterministic=False)  # deterministic = best action
    obs, reward, done, truncated, _ = env.step(action)
    agent_positions.append(env.world.agent_pos.copy())
    render(env.world)
    time.sleep(0.05)
