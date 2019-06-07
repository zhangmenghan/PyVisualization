#_*_  coding:utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt

# 球员能力表
plt.style.use('ggplot')

# font = FontProperties(fname='', size=20)

ability_size = 6
ability_label = ['Attack', 'Defend', 'Dribbling', 'Speed', 'Power', 'Shooting']

ax1 = plt.subplot(221, projection='polar')
ax2 = plt.subplot(222, projection='polar')
ax3 = plt.subplot(223, projection='polar')
ax4 = plt.subplot(224, projection='polar')

player = {
    'M': np.random.randint(size=ability_size, low=60, high=99),
    'H': np.random.randint(size=ability_size, low=60, high=99),
    'P': np.random.randint(size=ability_size, low=60, high=99),
    'Q': np.random.randint(size=ability_size, low=60, high=99)
}

theta = np.linspace(0, 2*np.pi, 6, endpoint=False)
theta = np.append(theta, theta[0])

player['M'] = np.append(player['M'], player['M'][0])
ax1.plot(theta, player['M'], color='r')
ax1.fill(theta, player['M'], color='r', alpha=0.3)
ax1.set_xticks(theta)
ax1.set_yticks([20, 40, 60, 80, 100])
ax1.set_xticklabels(ability_label)
ax1.set_title('Player1', position=(0.5, 1), color='r')

player['H'] = np.append(player['H'], player['H'][0])
ax2.plot(theta, player['H'], color='g')
ax2.fill(theta, player['H'], color='g', alpha=0.3)
ax2.set_xticks(theta)
ax2.set_yticks([20, 40, 60, 80, 100])
ax2.set_xticklabels(ability_label)
ax2.set_title('Player2', position=(0.5, 1), color='g')

player['P'] = np.append(player['P'], player['P'][0])
ax3.plot(theta, player['P'], color='b')
ax3.fill(theta, player['P'], color='b', alpha=0.3)
ax3.set_xticks(theta)
ax3.set_yticks([20, 40, 60, 80, 100])
ax3.set_xticklabels(ability_label)
ax3.set_title('Player3', position=(0.5, 1), color='b')

player['Q'] = np.append(player['Q'], player['Q'][0])
ax4.plot(theta, player['Q'], color='y')
ax4.fill(theta, player['Q'], color='y', alpha=0.3)
ax4.set_xticks(theta)
ax4.set_yticks([20, 40, 60, 80, 100])
ax4.set_xticklabels(ability_label)
ax4.set_title('Player4', position=(0.5, 1), color='y')

plt.show()