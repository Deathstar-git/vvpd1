import math
import argparse


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('x', type=int)

    return p


def main(x):
    if math.cos(2 * int(x)) != 0 and ((2 * x) + math.sin(math.fabs(3 * int(x)))) / math.cos(2 * int(x)) > 0:
        y = math.sqrt(((2 * x) + math.sin(math.fabs(3 * int(x)))) / math.cos(2 * int(x)))
        print("Значение y равно:" + str(y))
    else:
        print("Не удалось посчитать выражение!")


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    main(namespace.x)
