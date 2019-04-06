import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_json(r'C:\Users\Katerina\pandas\scripts\validation_errors.json')
data.columns

docstring = {}
for i in data.columns:
    if len(data[i]['errors']) > 0:
        docstring[i] = data[i]['errors'][0][0]

err_freq = {}
for i in set(list(docstring.values())):
    err_freq[i] = list(docstring.values()).count(i)

a = [i for i in docstring.keys() if docstring[i] == 'GL08']

#data.head()


