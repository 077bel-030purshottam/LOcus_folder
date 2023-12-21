pi = 'outer pi variable'


def print_pi():
    pi = 'inner pi variable'

    def nested_pi():
        print(pi)

    print(pi)
    nested_pi()


print(pi)
print_pi()
