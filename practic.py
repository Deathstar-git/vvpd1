import math
import argparse


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('count', choices=['Enter', 'enter'])

    return p


def main():
    x = input("Введите значение x:")
    if x.isdigit():
        x = int(x)
        if math.cos(2 * int(x)) != 0 and ((2 * x) + math.sin(math.fabs(3 * int(x)))) / math.cos(2 * int(x)) > 0:
            y = math.sqrt(((2 * x) + math.sin(math.fabs(3 * int(x)))) / math.cos(2 * int(x)))
            print("Значение y равно:" + str(y))
        else:
            print("Не удалось посчитать выражение!")

    try:
        int(x)
    except ValueError:
        print("Введено неверное значение!")


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    main()
