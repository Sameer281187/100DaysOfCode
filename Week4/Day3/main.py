# import csv
# # with open("weather_data.csv") as weather_data:
# #     data = weather_data.readlines()
# # print(data)
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
print(type(data))

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list)/len(temp_list)
# print(round(avg_temp, 2))
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
print(monday_temp * 9 / 5 + 32)

