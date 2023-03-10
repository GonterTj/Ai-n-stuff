import gymnasium as gym
import matplotlib.pyplot as plt
#import stable_baselines3 as stable_baselines3
#from stable_baselines3 import PPO
#from stable_baselines3.common.vec_env import DummyVecEnv
#from stable_baselines3.common.evaluation import evalute_policy
import numpy as np
env = gym.make("CartPole-v1", render_mode="human")
#observation, info = env.reset()
env.action_space.sample()

for episode in range(1, 11):
    score = 0
    state = env.reset()
    done = False

    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, done, info = env.step(action)
        score += reward

    print ('Episode:', episode, 'score:', score)

#env.close()


    #action = env.action_space.sample()  # agent policy that uses the observation and info
    #observation, reward, terminated, truncated, info = env.step(action)

    #if terminated or truncated:
        #observation, info = env.reset()

    #np.array ([-0.03294653,  0.01153272, -0.04511934, -0.04448458])
    

    #env.render()

    #observation = env.reset()
    #print(observation)


env.close()

plt.scatter(observation, observation)
plt.show()