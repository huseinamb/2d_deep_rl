import numpy as np
from env import TrafficEnv
import time

env = TrafficEnv()
obs, _ = env.reset()

for _ in range(200):
    action = np.random.uniform(-1, 1, size=(1,))
    obs, reward, done, truncated, _ = env.step(action)
    env.render()
    time.sleep(0.05)
    if done:
        obs, _ = env.reset()
