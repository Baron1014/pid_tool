import math
import argparse

def main(pre_y,  y, pre_u, u, learning_rate=None): 
    if learning_rate:
        return round(2.6*y - 1.2*pre_y + u + 1.2*pre_u + learning_rate*y*math.sin(u+pre_u+y+pre_y), 4)
    else:
        return round(2.6*y - 1.2*pre_y + u + 1.2*pre_u, 4)



if __name__ == "__main__":
    # print(main(0, -2, 1.23, 4.56, 0.6))

    parser = argparse.ArgumentParser()

    parser.add_argument('pre_y',
                        type=float,
                        nargs='?',
                        help='The y value from the previous run.')
    
    parser.add_argument('y',
                        type=float,
                        nargs='?',
                        help='The y value obtained by run.')

    parser.add_argument('pre_u',
                        type=float,
                        nargs='?',
                        help='The u value from the previous run.')
    
    parser.add_argument('u',
                        type=float,
                        nargs='?',
                        help='The u value obtained by run.')

    parser.add_argument('-lr',
                        type=float,
                        nargs='?',
                        help='Learning Rate.')

    args = parser.parse_args()

    if args.lr:
        print(main(args.pre_y, args.y, args.pre_u, args.u, args.lr))
    else:
        print(main(args.pre_y, args.y, args.pre_u, args.u))