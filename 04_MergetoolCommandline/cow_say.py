import cmd
import readline
import shlex

from default import *


def parse_args(args):
    return shlex.split(args)


def get_opt_args(args, dct):
    dct = dct.copy()
    try:
        for key in dct:
            if key in args:
                dct[key][0] = dct[key][1](args[args.index(key) + 1])

        return dct
    except IndexError:
        print("Invalid Input")


def complete(text, line, begidx, endidx):
    args = shlex.split(line)
    if begidx == endidx:
        key, command = args[-1]
    else:
        key, command = args[-2], args[0]
    return [s for s in COMPLETE[command][key] if s.startswith(text)]


class CmdLine(cmd.Cmd):
    def do_list_cows(self, args):
        """
        Печатает всех имеющихся коров.
        """
        print(cowsay.list_cows())

    def do_make_bubble(self, args):
        """
        Оборачивает введенный текст в пузырь.
        make_bubble text [-b cowsay | cowthink] [-d width] [-w wrap_text]

        Параметры:
            text    :  выводимое коровой сообщение;
            -b      :  cowsay или cowthink
            -d      :  width
            -w      :  wrap_text
        """
        try:
            text, *opt_args = parse_args(args)
            args_t = get_opt_args(opt_args, MAKE_BUBBLE_DEF_ARGS)
            print(
                cowsay.make_bubble(
                    text=text,
                    brackets=args_t["-b"][0],
                    width=args_t["-d"][0],
                    wrap_text=args_t["-w"][0],
                )
            )
        except ValueError:
            print("makebubble need a text!")

    def do_cowsay(self, args):
        """
        Заставляет корову разговаривать.
        cowsay message [-c cow] [-e eye_string] [-T tongue_string]

        Параметры:
            message :  выводимое коровой сообщение;
            -c      :  имя коровы (смотри list_cows);
            -e      :  строка - глаза коровы;
            -T      :  строка - язык коровы;
        """
        try:
            message, *opt_args = parse_args(args)
            args_t = get_opt_args(opt_args, COWSAY_DEF_ARGS)
            args_t["message"] = message
            print(args_t)
            print(
                cowsay.cowsay(
                    message=args_t["message"],
                    cow=args_t["-c"][0],
                    eyes=args_t["-e"][0],
                    tongue=args_t["-T"][0],
                )
            )
        except ValueError:
            print("cow need a message!")

    def do_cowthink(self, args):
        """
        Аналогична команде cowsay (см. help cowsay).
        """
        self.do_cowsay(args)

    def complete_cowsay(self, text, line, begidx, endidx):
        return complete(text, line, begidx, endidx)

    def complete_make_bubble(self, text, line, begidx, endidx):
        return complete(text, line, begidx, endidx)

    def complete_сowthink(self, text, line, begidx, endidx):
        return complete(text, line, begidx, endidx)

    def do_exit(self, args):
        """
        Завершает работу коммандной строки.
        """
        return 1


if __name__ == "__main__":
    CmdLine().cmdloop()
