
parameters = {
    "EPISODES": 10000,
    "N_TRAJECTORIES": 32,
    "SIGMA": 0.2,
    "GAMMA": 0.99,
    "LOAD_FROM_FILE": False,
    "LEARN_RATE": 0.00001,
    "BIAS_MU": 0.0,  # yields mu = 0 with linear activation
    "BIAS_SIG": 0.0,  # yields sig = 1 with exp activation
    "DEBUG": False,
    "CLIP": 1.0,
    "SCENARIO": "scenarios/soccer_continous/"
}


'''
with open('Parameters.json') as j:
    tmp = json.load(j)
for key in tmp:
    parameters[key] = tmp[key]
del key, tmp'''
