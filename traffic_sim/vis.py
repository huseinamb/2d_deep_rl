#visualize after training
import numpy as np
from env import TrafficEnv
from stable_baselines3 import PPO
import time
from render import render

env = TrafficEnv()
model = PPO.load("ppo_traffic_model_100000")  # load trained model

obs, _ = env.reset()
done = False
truncated = False

# Keep track of positions for visualization if needed
agent_positions = []

while not done and not truncated:
    action, _ = model.predict(obs, deterministic=True)  # deterministic = best action
    obs, reward, done, truncated, _ = env.step(action)
    agent_positions.append(env.world.agent.position.copy())
    render(env.world)
    time.sleep(0.05)
