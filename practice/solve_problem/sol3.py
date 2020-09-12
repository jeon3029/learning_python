
def surjective(list1, list2):
    check = [False]*len(list2)
    for x in list1:


def main():
    m = int(input("m개의 원소 함수1 : "))
    n = int(input("n개의 우너소 함수2 : "))
    if(m < n):
        print("ERROE : m의 개수가 n의 개수보다 많거나 같아야 합니다.")
    else:
        print("함수1에서 함수2로의 전사함수 : ")
        func1 = range(0, m)
        func2 = range(0, n)
        surjective(func1, func2)


if __name__ == "__main__":
    main()
