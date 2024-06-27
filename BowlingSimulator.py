def main():
    username = UserInfo()
    skillcalc = ScoreInput()
    Output(username, skillcalc)

def UserInfo():
    answer = input('Do you mind telling us a bit about yourself? Yes or No? ')
    if answer == 'Yes':
        exit()
    elif answer == 'No':
        print('Great!')
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    age = input('Enter your age: ')
    return CreateUserName(first_name, last_name, age)

    
def CreateUserName(first_name, last_name, age):
    first_name = first_name.lower()
    last_name = last_name.lower()
    return first_name[0] + last_name + age
    

def ScoreInput():
    score = int(input('Enter your score: (Enter -1 to exit)'))
    score_list = []
    while score != -1:
        if (score <= 300) and (score >= 0):
            score_list.append(score)
        else:
            print(f'{score} is an invalid score. Please enter a feasible bowling score.')
            exit()
        score = int(input('Enter your score: (Enter -1 to exit)'))
    return SkillLevel(score_list)

def SkillLevel(score_list):
    average_score = sum(score_list) / len(score_list)
    if (average_score >= 0) and (average_score <= 90):
        skill = 'beginner'
    elif (average_score > 90) and (average_score <= 180):
        skill = 'intermediate'
    elif (average_score > 180) and (average_score <= 300):
        skill = 'advanced'
    max_num = max(score_list)
    min_num = min(score_list)
    return [average_score, skill, max_num, min_num]

def Output(username, skillcalc):
    print(f'Your username is {username}, your highest score was {skillcalc[2]}, your lowest score was {skillcalc[3]}, your combined average score was {skillcalc[0]}, and your skill level was {skillcalc[1]}.')
    print('Fantastic Bowling!')

main()