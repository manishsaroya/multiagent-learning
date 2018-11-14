import numpy as np 
import pickle
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 4))

print("loading DDPG")
with open("DDPG_rewards.txt", "rb") as fp:   # Unpickling
    ddpg_ = pickle.load(fp)
plt.plot(ddpg_,label='DDPG')

print("loading MADDPG")
with open("MADDPG_rewards.txt","rb") as fp:
    maddpg_ = pickle.load(fp)
plt.plot(maddpg_,label='MADDPG')

plt.ylabel('Global Reward')
plt.xlabel('No. of Episodes')
plt.legend()
plt.show()

