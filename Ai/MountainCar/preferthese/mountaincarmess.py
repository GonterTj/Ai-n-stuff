
from stable_baselines3 import PPO
import numpy as np
import gym
import matplotlib as plt

env = gym.make("MountainCar-v0")

model = PPO(policy = "MlpPolicy",env =  env, verbose=1)
model.learn(total_timesteps=25000)

#model.save("ppo_mountaincart")  # saving the model to ppo_cartpole.zip
model = PPO.load("ppo_mountaincart")  # loading the model from ppo_cartpole.zip

obs = env.reset()
for i in range(1000):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()