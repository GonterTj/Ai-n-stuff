
from stable_baselines3 import PPO, a2c
import numpy as np
import gym
import matplotlib as plt
import os
import time

models_dir = f"models/PPO-{int(time.time())}"
logdir = f"logs/PPO-{int(time.time())}"

if not os.path.exists(models_dir):
   os.makedirs(models_dir)

if not os.path.exists(logdir):
   os.makedirs(logdir)

env = gym.make("MountainCar-v0")
env.reset

model = PPO("MlpPolicy" , env, env, verbose=1, tensorboard_log=logdir)

TIMESTEPS = 10000
for i in range(1,100):
   model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
   model.save(f"{models_dir}/{TIMESTEPS=i}")

#model.save("ppo_mountaincart")  # saving the model to ppo_cartpole.zip
model = PPO.load("ppo_mountaincart")  # loading the model from ppo_cartpole.zip

obs = env.reset()
for i in range(1000):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()