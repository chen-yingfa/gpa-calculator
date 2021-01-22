from formatter import Formatter


class Course():
    def __init__(self, _id: int = -1, name: str = "无", credit: int = 0,
                 grade: str = 'F', _type: str = '必修', sem: str = '0000-0000-0'):
        self._id = _id
        self.name = name.strip()
        self.credit = credit
        self.grade = grade.strip().upper()
        self._type = _type.strip()
        self.sem = sem.strip()

    def __repr__(self):
        return self.formatted_str()

    def __str__(self):
        return self.__repr__()

    def to_list(self):
        return [self._id, self.name, self.credit, self.grade, self._type, self.sem]

    def from_list(self, lis: list):
        self._id = int(lis[0])
        self.name = lis[1]
        self.credit = int(lis[2])
        self.grade = lis[3]
        self._type = lis[4]
        self.sem = lis[5]

    def formatted_str(self):
        return Formatter.course_row(self._id, self.name, self.credit,
                                    self.grade, self._type, self.sem)

    def is_bixian(self) -> bool:
        return self._type == '必修' or self._type == '限选'

    def is_renxuan(self) -> bool:
        return self._type == '任选'

    def is_pf(self):
        return self.grade in ['F', 'P']

    def is_w(self):
        return self.grade == 'W'

    def is_pf_or_w(self):
        return self.is_pf() or self.is_w()
