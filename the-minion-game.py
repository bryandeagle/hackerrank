def minion_game(string):
    scores = {'Kevin': 0, 'Stuart': 0}
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            scores['Kevin'] += len(string) - i
        else:
            scores['Stuart'] += len(string) - i
    
    if scores['Stuart'] == scores['Kevin']:
        print('Draw')
    elif scores['Stuart'] > scores['Kevin']:
        print("Stuart {}".format(scores['Stuart']))
    else:
        print('Kevin {}'.format(scores['Kevin']))
