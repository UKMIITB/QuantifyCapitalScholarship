import pandas as pd

d = {"a": {"b": 4}, "z": {"c": {"a": 1}, "d": 1}, "y": 3}

df = pd.json_normalize(d, sep='_')


flatted_dict = df.to_dict(orient='records')[0]

for key, val in flatted_dict.items():
    print(str(key) + ": " + str(val))
