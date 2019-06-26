# Create a dictionary and take input from the user and return the meaning of the
# word from the dictionary

# Creating  Dictionary
dict = {"ignore":"refuse to take notice of or acknowledge", "abandon":"cease to support or look after",
        "exaggerate":"enlarged or altered beyond normal proportions", "prejudice":"preconceived opinion that is not based on reason or actual experience"}

#Getting input from user
user_input = input('Enter your word to find out the Meaning :  ').lower()

#Getting output
print(user_input, 'means', dict[user_input])
