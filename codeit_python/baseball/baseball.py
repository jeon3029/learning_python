from random import randint


def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        gen = randint(1, 9)
        if gen not in numbers:
            numbers.append(gen)
    # 코드를 작성하세요.

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers
# l = generate_numbers()
# print(l)


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    cnt=1
    while cnt<=3:
        guess = int(input("{}번째 숫자를 입력하세요: ".format(cnt)))
        if guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        elif guess>=10 or guess<1:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(guess)
            cnt+=1
    return new_guess
# print(take_guess())


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    for i,val in enumerate(guess):
        if guess[i] == solution[i]:
            strike_count+=1
        elif val in solution:
            ball_count+=1


    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요.
l = generate_numbers()
while True:
    g = take_guess()
    s,b = get_score(g,l)
    print("{}S {}B".format(s,b))
    tries+=1
    if s==3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
