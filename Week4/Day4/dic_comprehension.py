sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split()

result = {item:len(item) for item in word_list}
print(result)