import gym
import numpy as np

env = gym.make('MountainCarContinuous-v0')
env.reset()
print(env.observation_space.high)
print(env.observation_space.low)

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

print(discrete_os_win_size)

q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space[0]]))

done = False
print(q_table.shape)

while not done:
    action = 2
    new_state, reward, done, _ = env.step(action)
    print(new_state, reward, done)
    done = False

    env.render()

env.close()