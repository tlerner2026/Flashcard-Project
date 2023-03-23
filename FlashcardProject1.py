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

#Use user to find previous data about them.
correct_dict = {}
wrong_dict = {}

user = input("What is your name, so that you keep your progress for the future: ")

with open("text.txt", "r") as f:
    lines = f.readlines()

previous_info = "".join(lines)

if previous_info.find(user) != -1:
    print("User is somewhere in the file")
    for line in lines:
        if line.find(user) != -1:
            user_index = previous_info.find(user)
            print("Found user!")   
            correct_index = previous_info.find('Correct: ',user_index)+9
            correct_index_end = previous_info.find("}",correct_index)+1
            correct_dict = json.loads(previous_info[correct_index:correct_index_end])
            wrong_index = previous_info.find('Wrong: ',user_index)+7
            wrong_index_end = previous_info.find("}",wrong_index)+1
            wrong_dict = json.loads(previous_info[wrong_index:wrong_index_end])
            #Add code to get delete of a prevoius user, so it can be overwritten.
f.close()

while len(questions) != 0: 

    #Shuffle the questions
    shuffled = list(questions.items())
    random.shuffle(shuffled)
    questions = dict(shuffled) 

    for state, capital in questions.items():

        answer = input(f"What is the capital of {state}: ")

        if answer == capital:
            correct_dict[state] = capital
            print("Correct")
        
        else:
            print(f"Wrong, the correct answer is: {capital}")
            wrong_dict[state] = capital
        
        f = open("text.txt","w")
        f.write(f"{previous_info}\n{user}\n Correct: {json.dumps(correct_dict)}\n Wrong: {json.dumps(wrong_dict)}")
        f.close()

    if len(questions) == 0:
        print("All correct, now exiting")
        break

    answer = input(f"Would you like to continue with the ones you got wrong, you scored {50 - len(wrong_dict)} out of 50. Type 'y' to continue, type 'n' to exit: ")
    
    if answer == 'n':
        print("Now exiting")
        break

    else:
        questions = wrong_dict.copy()
        wrong_dict.clear()