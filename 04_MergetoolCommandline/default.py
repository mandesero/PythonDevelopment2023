import cowsay

COWSAY_DEF_ARGS = {
    "-c": ["default", str],
    "-e": [cowsay.Option.eyes, str],
    "-T": [cowsay.Option.tongue, str],
}

MAKE_BUBBLE_DEF_ARGS = {"-b": ["cowsay", str], "-d": [40, int], "-w": [True, bool]}


COMPLETE = {
    "cowsay": {
        "-e": ["00", "^^", "oo", "@@", "--", "00", "..", "**"],
        "-c": cowsay.list_cows(),
        "-T": ["U ", "u ", "||", "L", "V"],
    },
    "cowthink": {
        "-e": ["00", "^^", "oo", "@@", "--", "00", "..", "**"],
        "-c": cowsay.list_cows(),
        "-T": ["U ", "u ", "||", "L", "V"],
    },
    "make_bubble": {"-b": ["cowsay", "cowthink"], "-d": [], "-w": ["True", "False"]},
}
