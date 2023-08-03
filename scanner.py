import sys


def scan(str):
    # checking if the string is null
    if str:
        token = []
        # creating a token list for all the characters
        for letter in str:
            if letter.isalpha():
                token.append(0)
            elif letter.isnumeric() or letter == "_":
                token.append(1)
            else:
                token.append(2)
        
        # table that we found from converting NFA to DFA and minimization
        table = [[2, 1, 1],
                 [1, 1, 1],
                 [2, 2, 1]]

        # initial phase is 0
        p = 0
        # changing state according to input and the given table
        for i in token:
            if table[p][i] == 1:
                return "Reject"
            else:
                p = table[p][i]
                res = p

        if res == 2:
            return "Accept"

    else:
        return "Reject"


def main(argv):
    if len(argv) < 2:
      print(scan(""))
    print(scan(argv[1]))


if __name__ == '__main__':
    main(sys.argv)