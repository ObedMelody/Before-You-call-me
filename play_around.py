import time
from termcolor import colored
"""
    All works and no play makes Obed a mean young man
"""
hi = 'hello'
print(colored("hey {}".format(hi), 'blue'))
print('Loading\n________\n+++++++++')
time.sleep(2)
print(colored('Should you call or text me?', 'yellow'))
quest = input('Are you my baby?: ').lower()
if quest == 'no':
    urg = input('How urgent is the matter?: ').lower()
    if urg == 'very urgent':
        dying = input('Are you dying?: ').lower()
        if dying == 'yes':
            save = input('Can i save you?: ').lower()
            if save == 'yes':
                print('Fine You Can Call')
            else:
                print('Text')
        else:
            print('Text')
    elif urg == 'not very urgent':
        print('Text')
    else:
        print('Invalid input')
elif quest == 'yes':
    print('Call me whenever you want')
else:
    print('Invalid input')
