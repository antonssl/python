import pandas as pd

json_data = {
	"name": {
		"first": "John",
		"last": "Smith"
	},
	"location": {
		"city": "Albuquerque",
		"state": "New Mexico",
		"country": "USA"
	},
	"cars": {
		"car1":"Ford",
		"car2":"BMW",
		"car3":"Fiat"
	}
}
print(json_data)

df = pd.io.json.json_normalize(json_data)
print(df)

df.to_csv('data.csv', encoding='utf-8', index=False)


