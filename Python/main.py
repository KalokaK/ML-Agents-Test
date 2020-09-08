from helpers import *
import parameters

parameters = parameters.parameters
scenario = parameters["SCENARIO"]

for file in os.listdir(scenario + 'unity'):
    if file.endswith('.x86_64'):
        env_name = file

try:
    env_name
except NameError:
    print("env name not defined something broken about unity binary or this code")

env = UnityEnvironment(file_name=scenario + 'unity/' + env_name,
                       worker_id=1,
                       seed=1,
                       side_channels=[],
                       no_graphics=False)
env.reset()
behaviour_names = list(env.behavior_specs)

behaviour_groups: Dict[str, BehaviourGroup] = {}

for key in list(env.behavior_specs):
    spec = env.behavior_specs[key]
    decision_steps, terminal_steps = env.get_steps(key)
    behaviour_groups[key] = BehaviourGroup(spec, key, decision_steps, scenario)
    print('behaviour name: ', key)
    print('number of observations: ', len(spec.observation_shapes))
    behaviour_groups[key].vis_obs = vis_obs = any(len(shape) == 3 for shape in spec.observation_shapes)
    print('is visual: ', vis_obs, '\n')
    print('continuous action space: ', spec.is_action_continuous(),
          ', discrete action space: ', spec.is_action_discrete())

env.reset()
step = 0
while True:
    time_step = time.time_ns()
    for group in behaviour_groups:  # group is the spec ID
        t0 = time.time_ns()
        decision_steps, terminal_steps = env.get_steps(group)
        t1 = time.time_ns()
        actions = behaviour_groups[group].process_steps(decision_steps, terminal_steps)
        t2 = time.time_ns()
        env.set_actions(group, actions)
        t3 = time.time_ns()
        if step % 600 == 0:
            print(f'time for group {group} in ms, total: {(t3-t0)/10e6}, get steps: {(t1-t0)/10e6}, get actions: {(t2-t1)/10e6}, set actions: {(t3-t2)/10e6}')
    time_bef_step = time.time_ns()
    env.step()
    time_post_step = time.time_ns()
    total = time_post_step - time_step
    for_python = time_bef_step - time_step
    for_unity = time_post_step - time_bef_step
    if step % 600 == 0:
        print(f'step took {total/10e6} ms, for python: {for_python/10e6}, for unity: {for_unity/10e6}, percent python: {100*for_python/total}, percent unity: {100*for_unity/total} \n')
    step += 1

env.close()

