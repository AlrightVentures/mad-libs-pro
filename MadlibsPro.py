# Tuesday night fun - MadLibsPro 

# Import librariers, modules
import random

# Define all mad lib variables by getting input from the user
adjectiveOne = input("Type an adjective: ")
adjectiveTwo = input("Type another adjective: ")
verbOne = input("Type a verb: ")
verbTwo = input("Type another verb: ")
nounOne = input("Type a noun: ")


# Generate a sentence as an f-string - version 1, random
madLib1 = f"People think Mona Lisa is amazing. She is very {adjectiveOne}. \
All she does is {verbOne}. I would rather {verbTwo} than pay for that painting. \
I guess I'm {adjectiveTwo}."

# Generate a sentence as an f-string - version 2, Lord of the Rings
madLib2 = f"Remember, Frodo. Even the {adjectiveOne} person can {verbOne} the course of the {nounOne}."

# Generate a sentence as an f-string - version 3, The Simpsons
madLib3 = f"D'Oh! It's so {adjectiveOne} to be wise… just think of something {adjectiveTwo} to say and then don't say it."

# Generate a sentence as an f-string - version 4, The Office
madLib4 = f"Michael: 'I Want You To Think About This {adjectiveOne} And {adjectiveTwo}.'\n Dwight: 'That's What She Said'"

# Generate a random digit between 1 and 4 to select one of the mad libs above 
selectedMadLib = random.randint(1, 4)

# Print the resulting mad lib for user to read
match selectedMadLib:
    case 1: 
        print(madLib1)
    case 2: 
        print(madLib2)
    case 3: 
        print(madLib3)
    case 4: 
        print(madLib4)

# Made with love.
# Check out Harry Mack on YouTube. 
# Have a great day.