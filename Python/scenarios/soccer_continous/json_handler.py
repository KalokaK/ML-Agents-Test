import json

with open('Parameters.json') as j:
    parameters = json.load(j)
    print('\nparameters:\n '
          '----------------------------- \n',
          parameters,
          '-----------------------------')

