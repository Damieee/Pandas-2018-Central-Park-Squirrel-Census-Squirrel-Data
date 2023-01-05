import pandas

data=pandas.read_csv("227 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_squirrel_count=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"]=="Black"])

data_dict={"Squirrel Color": ["Black", "Cinnamon", "Gray"], "Number": [black_squirrel_count, cinnamon_squirrel_count, gray_squirrel_count]}

squirrel_data=pandas.DataFrame(data_dict)
print(squirrel_data)