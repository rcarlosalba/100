
def one_to_onehundred_for():
    for i in range(1, 101):
        print(i)


def one_to_onehundred_while():
    i = 1
    while i <= 100:
        print(i)
        i += 1


def one_to_onehundred_recursive():
    def print_number(n):
        if n > 100:
            return
        print(n)
        print_number(n + 1)
    print_number(1)
