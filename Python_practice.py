# print("Hello World")
# my_votes = int(input("How many votes did you get in the election?"))
# total_votes = int(input("What was the total amount of votes in the election?"))
# percentage_votes = (my_votes/total_votes)*100
# print(f'I received {percentage_votes}% of the total votes')
# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
    # print("El Paso is in the list of counties.")
# else:
    # print("El Paso is not the list of counties.")
    
    
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

import datetime

now = datetime.datetime.now()

print("the time is ", now)