from random import randint


def generate_numbers(n):
    # 코드를 작성하세요.
    l = []
    while len(l) < n:
        gen = randint(1, 45)
        if gen not in l:
            l.append(gen)
    return l
#print(generate_numbers(6))


def draw_winning_numbers():
    ll = sorted(generate_numbers(6))
    while True:
        bonus = randint(1,45)
        if bonus not in ll:
            ll.append(bonus)
            break
    return ll
# print(draw_winning_numbers())


def count_matching_numbers(list_1, list_2):
    cnt = 0
    for val in list_1:
        if val in list_2:
            cnt+=1
    return cnt 


def check(numbers, winning_numbers):
    cnt1 = count_matching_numbers(numbers,winning_numbers[:6])
    cnt2 = count_matching_numbers(numbers,winning_numbers[-1:])
    if cnt1==6:
        return 1000000000
    elif cnt1==5 and cnt2==1:
        return 50000000
    elif cnt1==5:
        return 1000000
    elif cnt1==4:
        return 50000
    elif cnt1==3:
        return 5000
    else:
        return 0