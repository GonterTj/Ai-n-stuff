import gym
import time
import tensorflow as tensor
import math

env = gym.make('CartPole-v1', render_mode="human")

policy = lambda obs: 0

for _ in range(1):
    obs = env.reset()
    for _ in range(80):
        actions = policy(obs)
        obs, reward, terminated, truncated, info = env.step(actions)
        env.render()
       # time.sleep(0.05)

n_bins = ( 6 , 12 )
lower_bounds = [ env.observation_space.low[2], -math.radians(50) ]
upper_bounds = [ env.observation_space.high[2], math.radians(50) ]


env.close

reward