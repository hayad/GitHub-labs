import pandas as pd

foo = {
	'id': 111,
	'status': 'green',
	'weight': 0.6
}

bar = {
	'id': 222,
	'status': 'red',
	'weight': 0.7
}

data = {
	'foo': foo,
	'bar': bar,
}

df = pd.DataFrame.from_dict(data)
print(df)
print(data)
