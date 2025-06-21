import pandas

data = pandas.read_csv("Squirrel_Data.csv")
squirrel_color_data = data["Primary Fur Color"]

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# not_identified_count = len(data[data["Primary Fur Color"] == " "])
# print(not_identified_count)

squirrel_count_dict = {
    "Primary Fur Color" : ["Gray", "Cinnamon", "Black"],
    "count" : [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

pandas.DataFrame(squirrel_count_dict).to_csv("squirrel_count_by_color.csv")
