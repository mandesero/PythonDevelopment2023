import cowsay
import sys
import argparse


def main():
    '''
    cowsay [-e eye_string] [-f cowfile] [-h] [-l] [-n] [-T tongue_string] [-W column] [-bdgpstwy]

    def cowsay(message, cow='default',
    preset=None, eyes=Option.eyes, tongue=Option.tongue, width=40, wrap_text=True, cowfile=None) -> str
    '''
    parser = argparse.ArgumentParser()

    # Positional
    parser.add_argument("message", type=str)

    # Optional 
    parser.add_argument("-e", "--eye", default="oo", help="A custom eye string")
    parser.add_argument("-l", default="default", help="The name of the cow (valid names from list_cows)")
    parser.add_argument("-T", "--tongue", default="", help="A custom tongue string")
    parser.add_argument("-W", "--width", default=40, type=int, help="The width of the text bubble")
    parser.add_argument("-f", "--cowfile", default=None, help="A custom string representing a cow")

    # Other
    # parser.add_argument("-b", default="")
    # parser.add_argument("-d", default="")
    # parser.add_argument("-g", default="")
    # parser.add_argument("-p", default="")
    # parser.add_argument("-s", default="")
    # parser.add_argument("-t", default="")
    # parser.add_argument("-w", default="")
    # parser.add_argument("-y", default="")

    args = parser.parse_args()

    if args.l != "default":
        print(cowsay.list_cows())
    else:
        if args.cowfile is None:
            cow = cowsay.cowsay(
                message=args.message,
                eyes=args.eye,
                tongue=args.tongue,
                width=args.width
            )
        else:
            try:
                with open(args.cowfile, "r") as cowfile:
                    cow_string = cowfile.read()
                cow = cowsay.cowsay(
                    message=args.message,
                    eyes=args.eye,
                    tongue=args.tongue,
                    width=args.width,
                    cowfile=cow_string
                )
            except FileNotFoundError:
                print("No such file or directory")
                sys.exit()
        print(cow)


if __name__ == "__main__":
    main()
