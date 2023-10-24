import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np

def render_state(size='normal'):
    figsize=(2.5,2.5) if size=='small' else (4.5,4.5)
    plt.figure(figsize=figsize) 
    plt.axis('off')
    plt.gcf().set_facecolor("#c8e6f7")
    plt.imshow(env.render())
    plt.show()

def visualize_matrix(matrix: np.ndarray, name=''):
    fig, ax = plt.subplots(figsize=(5,5))
    plt.title(name)
    plt.yticks(np.arange(matrix.shape[0]))
    plt.xticks(np.arange(matrix.shape[1]))
    ax.imshow(matrix, cmap=plt.cm.Blues)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, np.round(matrix[i, j],1), ha="center", va="center", color="grey")

class Q_Agent():
    def __init__(self, env: gym.Env, alpha:int, gamma:int, epsilon:int, n_episodes:int, seed:int=42):
        pass

    def learn(self) -> list:
        '''Returns a list of rewards from training.'''
        pass

    def predict(self, state: np.ndarray) -> int:
        '''Returns the policy action from a state. Implements Exploration Exploitation trade-off'''
        pass
        
    def n_actions(self) -> int:
        '''Returns number of actions.'''
        pass

    def n_states(self) -> int:
        '''Returns number of states.'''
        pass


if __name__ == '__main__':
    env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False, render_mode='rgb_array')
    env.reset(seed=42)
    agent = Q_Agent(env, alpha=0.1, gamma=0.9, epsilon=0.6, n_episodes=1000)
    rewards = agent.learn()
    # TODO: implementiraj trazene zadatke iz notebook fajla