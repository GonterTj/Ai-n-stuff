import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()


for _ in range(1000):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

    #np.array ([-0.03294653,  0.01153272, -0.04511934, -0.04448458])
    

    #env.render()

    #observation = env.reset()
    #print(observation)


env.close()

plt.scatter(observation, observation)
plt.show()