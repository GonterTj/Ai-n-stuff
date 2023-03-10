import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

env_name = 'CartPole-v0'
env = gym.make(env_name)
for episode in range(1, 11):
    score = 0
    state = env.reset()
    done = False

    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score += reward

    print('Episode:', episode, 'Score:', score)

env = gym.make(env_name)
env = DummyVecEnv([lambda: env])
model = PPO('MlpPolicy', env, verbose=1)

model.learn(total_timesteps=20000)

#model.save('ppo model')

#evaluate_policy(model, env, n_eval_episodes=10, render=True)

env.close()

for episode in range(1, 11):
    score = 0
    obs = env.reset()
    done = False

    while not done:
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)
        score += reward

    print('Episode:', episode, 'Score:', score)
env.close()