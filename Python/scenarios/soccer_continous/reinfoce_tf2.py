from mlagents_envs.environment import UnityEnvironment
import tensorflow as tf
from tensorflow import keras
import numpy as np
import datetime as dt
import json

# Set up environment
env = UnityEnvironment(file_name='unity/SoccerTwos.x86_64', worker_id=1, seed=1, side_channels=[])
env.reset()

specs = {}
for key in list(env.behavior_specs):
    specs[key] = spec = env.behavior_specs[key]
    print('behaviour name: ', key)
    print('number of observations: ', len(spec.observation_shapes))
    vis_obs = any(len(shape) == 3 for shape in spec.observation_shapes)
    print('is visual: ', vis_obs, '\n')
    print('continuous action space: ', spec.is_action_continuous(),
          ', discrete action space: ', spec.is_action_discrete())

with open('Parameters.json') as j:
    parameters = json.load(j)
    print('\nparameters:\n '
          '----------------------------- \n',
          parameters,
          '-----------------------------')


def create_network():
    return


def get_action():
    return


def train_network():
    return


def save_network():
    return


env.close()
