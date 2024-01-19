from random import randint
random_num = randint(1,100)
list = [0]
while True:
    guess = int(input('Enter guess from 1 to 100: '))
    if guess < 1 or guess > 100:
        print('Out of Bounds')
        continue
    list.append(guess)

    if guess == random_num:
        print('You guesed it.')
        print(list)
        print(f'Total guesses you have taken is: {len(list)}')
        break
    
    if list[-2]:
        if abs(random_num - guess) < abs(random_num - list[-2]):
            print('Warmer')
        else:
            print('Colder')
    else:        
        if abs(random_num - guess) <= 10:
            print('Warm')
        else:
            print('Cold')


