import random, json

# Question set:
questions = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
}

wrong_dict = {}

#Check if it is the user first time playing and ask for name to make an individual file for them.
user = input("What is your name: ")
played = input("Is this your first time? Or if you want to reset your data type 'yes'. Type 'yes' or 'no' : ")
if played == 'no':
    with open(f"{user}.json", "r") as f:
        data = json.load(f)
        questions = data
    f.close()

wrong_dict = questions

#Start while loop for questions
while len(wrong_dict) != 0: 

    #Shuffle the questions
    shuffled = list(questions.items())
    random.shuffle(shuffled)
    questions = dict(shuffled) 

    for state, capital in questions.items():

        answer = input(f"What is the capital of {state}: ")

        #check if correct
        if answer == capital:
            del wrong_dict[state]
            print("""Correct
----------------""")
        
        else:
            print(f"""Wrong, the correct answer is: {capital}
----------------""")
        
        #store data
        f = open(f"{user}.json","w")
        f.write(f"{json.dumps(wrong_dict)}")
        f.close()

    if len(wrong_dict) == 0:
        break

    answer = input(f"Would you like to continue and learn more, so far you learned {50 - len(wrong_dict)} out of 50. Type 'y' to continue, type 'n' to exit: ")
    
    if answer == 'n':
        print("Now exiting")
        break

    else:
        questions = wrong_dict.copy()

print("All correct, now exiting")