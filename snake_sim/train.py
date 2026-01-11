#traffic_sim/
#  world.py        # data structures
#  simulate.py     # physics & rules
#  render.py       # pygame drawing
#  env.py          # Gym wrapper
#  train.py        # PPO training
from stable_baselines3 import PPO
from env import SnakeEnv  # your Gym wrapper

# Create environment
env = SnakeEnv()

# Create PPO agent
model = PPO("MlpPolicy", env, verbose=1)

# Train for n timesteps
n_steps = 50_000
model.learn(total_timesteps=n_steps)

# Save the trained model
model.save("ppo_traffic_model_50000")
