# Adela Zarzour
# CPSC-20000
# Sprint 4
# Matchmaker 


# Constants
INTRODUCTION = '''
~ Life Partnership Evaluation Form, 2021 ~

So you've decided that you want to date me. Great!
Please complete the questionare below to determine whether you are eligible.

On a scale of 1 to 5, with 1 being 'I Disagree Completely', 3 being 'Neutral', and  5 being 
'I Agree Completely', type in your numerical response to each of the 5 questions.

'''

QUESTION = ['Cats are the true "mans best friend".',
            'Black coffee is delicious.',
            'Flowers are overrated.',
            'Raisin Bran cereal is the superior breakfast.',
            'Shared values are more important for a successful relationship than shared interests.',
]

DESIRED_RESPONSE = [
    5, # completely agree
    1, # completely disagree
    1, # completely disagree
    5, # completely disagree
    5, # completely agree
]

WEIGHT = [
    3, # very important
    1, # not important
    3, # very important
    1,# not important
    3, # very important

]


MAX_SCORE = 5 * len(QUESTION)


print(INTRODUCTION)

# Ask all questions:
response = []
compatibility = []
weight = []

for i in range(len(QUESTION)):
    userResponse = int(input(QUESTION[i]))
    response.append(userResponse)

    questionCompatibility = 5 - abs(userResponse - DESIRED_RESPONSE[i])
    compatibility.append(questionCompatibility)


    # String formatting with parameters and placeholders. 
    print('Question %d compatibility: %d\n' % (i+1, questionCompatibility))


totalCompatibility = 0
for c in compatibility:
    totalCompatibility += c

totalCompatibility += 100 / MAX_SCORE
print('Total Compatibility: %d\n\n' % (totalCompatibility))

if totalCompatibility < 20:
    print ('Not looking for anything right now!')
elif totalCompatibility < 80:
    print ('Friends?')
else:
    print ('Meet my parents?')


# userResponse1 = int(input(QUESTION[0])) # Cats question
# desiredResponse1 = 5
# compatibility1 = 5 - abs(userResponse1 - DESIRED_RESPONSE[0])
# print("Question 1 Compatibility: " + str(compatibility1))
# print("")

# userResponse2 = int(input(QUESTION[1])) # Coffee question
# desiredResponse2 = 1
# compatibility2 = 5 - abs(userResponse2 - DESIRED_RESPONSE[1])
# print("Question 2 Compatibility: " + str(compatibility2))
# print("")

# userResponse3 = int(input(QUESTION[2])) # Flowers question
# desiredResponse3 = 1
# compatibility3 = 5 - abs(userResponse3 - DESIRED_RESPONSE[2])
# print("Question 3 Compatibility: " + str(compatibility3))
# print("")
 

# userResponse4 = int(input(QUESTION[3])) # Cereal question
# desiredResponse4 = 5
# compatibility4 = 5 - abs(userResponse4 - DESIRED_RESPONSE[3])
# print("Question 4 Compatibility: " + str(compatibility4))
# print("")


# userResponse5 = int(input(QUESTION[4])) # Values question
# desiredResponse5 = 5
# compatibility5 = 5 - abs(userResponse5 - DESIRED_RESPONSE[4])
# print("Question 5 Compatibility: " + str(compatibility5))
# print("")


# totalCompatibility = (compatibility1 + compatibility2) / MAX_SCORE
# print("Total Compatibility: " + str(totalCompatibility))
# print("")