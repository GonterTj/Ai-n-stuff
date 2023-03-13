import gymnasium as gym
import matplotlib.pyplot as plt

env = gym.make('MountainCar-v0', render_mode="human")

# Observation and action space
obs_space = env.observation_space
action_space = env.action_space
print("The observation space: {}".format(obs_space))
print("The action space: {}".format(action_space))

# reset the environment and see the initial observation
obs = env.reset()
print("The initial observation {}".format(obs))

for _ in range(10):
    env.render()
    # Sample a random action from the entire action space
    random_action = env.action_space.sample()

    # # Take the action and get the new observation space
    new_obs, reward, done, truncated, info = env.step(random_action)
    print("The new observation {}".format(new_obs))


    

print("Upper Bound for Env Observation", env.observation_space.high)
print("Lower Bound for Env Observation", env.observation_space.low)

