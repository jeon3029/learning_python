from itertools import permutations


def one_pair(list):
    count = 0
    for x in range(0, len(list)):
        for y in range(x+1, len(list)):
            first = list[x]
            second = list[y]
            for z in shape:
                if z in first:
                    t1 = first.replace(z, "")
                if z in second:
                    t2 = second.replace(z, "")
            if t1 == t2:
                count = count+1
                if count > 2:
                    break
    if count == 2:
        return True
    else:
        return False


list = ['1', '2', '3', '4', '5', '6']  # ,'7', '8', '9', 'K', 'Q', 'J', 'A'
# too many decks so I shortened it to number 6
shape = ['Spade', 'Diamond', 'Heart', 'Clova']
deck = []


def main():
    for x in shape:
        for y in list:
            deck.append(x+y)
    hand = permutations(deck, 5)
    for x in hand:
        if one_pair(x):
            print(x)


# main starts
if __name__ == "__main__":
    main()
