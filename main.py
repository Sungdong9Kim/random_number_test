import random

random_number = random.randint(1,20)
for i in range(1, 5):
    ask = int(input(f'기회가 {5-i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: '))
    print(f'{random_number}, {ask}')
    if i < 4:
        if (ask - random_number) == 0:
            print(f'축하합니다. {i}번 만에 숫자를 맞히셨습니다.')
            break
        elif (random_number - ask) > 0:
            print("Up")
        else:
            print("Down")
    else:
        if (ask - random_number) == 0:
            print(f'축하합니다. {i}번 만에 숫자를 맞히셨습니다.')
            break
        else:
            print(f'아쉽습니다. 정답은 {random_number}입니다.')
