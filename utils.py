dict_grade_old = {'A+': 4.0, 'A': 4.0, 'A-': 3.7,
                  'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                  'C+': 2.3, 'C': 2.0, 'C-': 1.7,
                  'D+': 1.3, 'D': 1.0, 'F': 0.0}


lookup_course_type = {'必修': 0,
                      '限选': 1,
                      '任选': 2}


def isgrade(s: str) -> bool:
    s = s.upper()
    if s in dict_grade_old or s == 'P':
        return True
    return False


def grade_to_float(s: str, new_method: bool = False):
    ret = dict_grade_old[s]
    if new_method and ret <= 3.7:
        ret += 0.3
    return ret


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def isint(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def isyesno(val):
    if val == 'y' or val == 'n' \
        or val == 's' or val == 'b':
        return True
    return False

def promptfloat():
    inp = input()
    if isfloat(inp):
        return float(inp)
    while True:
        inp = input("Input float: ")
        if isfloat(inp):
            return float(inp)


def promptint():
    inp = input()
    if isint(inp):
        return int(inp)
    while True:
        inp = input("Input int: ")
        if isint(inp):
            return int(inp)


def toyesno(val: str):
    "must make sure val is a valid yes or no string first"
    if val == 'y' or val == 's':
        return True
    return False


def promptyesno() -> bool:
    inp = input()
    while not isyesno(inp):
        inp = input('Input [y/n] (or [s/b]): ')
    return toyesno(inp)


def promptint_range(a, b):
    n = promptint()
    while n < a or b <= n:
        print("Input must be in [a, b)")
        n = promptint()
    return n


def promptgrade() -> float:
    inp = input()
    while not isgrade(inp):
        inp = input('Input valid grade ([A-D](+/-): ')
    return grade_to_float(inp)


if __name__ == '__main__':
    pass
