class Formatter():
    id_len = 4
    name_len = 14
    cred_len = 3
    grade_len = 3
    type_len = 3
    sem_len = 13
    space = chr(12288)   # 全角空格

    @staticmethod
    def format_str():
        s = Formatter.space
        return f"{{:>{Formatter.id_len}}}\t{{:{s}<{Formatter.name_len}}}\t\
{{:{s}>{Formatter.cred_len}}}\t{{:{s}<{Formatter.grade_len}}}\t\
{{:{s}<{Formatter.type_len}}}\t{{:<{Formatter.sem_len}}}"

    @staticmethod
    def header_row() -> str:
        return Formatter.format_str().format('ID', '名', '学分', '成绩', '类别', '学期')

    @staticmethod
    def course_row(_id, name, cred, grade, _type, sem) -> str:
        return Formatter.format_str().format(str(_id), str(name), str(cred),
                                             str(grade), str(_type), str(sem))
