import csv
from course import Course
from formatter import Formatter
import utils


class Database():
    def __init__(self):
        self.courses = []

    def get_courses_bixian(self):
        _courses = []
        for c in self.courses:
            if c._type == '必修' or c._type == '限选':
                _courses.append(c)
        return _courses
    
    def get_courses_renxuan(self):
        _courses = []
        for c in self.courses:
            if c._type == '任选':
                _courses.append(c)
        return _courses

    def show_all(self):
        Database.print_courses(self.courses)

    def print_gpa(self):
        '''
        输出各种 GPA
        '''
        gpa_all = (self.get_gpa(), self.get_gpa(new_method=True))
        gpa_bixian = (self.get_gpa_bixian(), self.get_gpa_bixian(new_method=True))
        gpa_renxuan = (self.get_gpa_renxuan(), self.get_gpa_renxuan(new_method=True))
        s = f'''      旧算法  新算法
所有  {gpa_all[0]    :.4f}  {gpa_all[1]    :.4f}
必限  {gpa_bixian[0] :.4f}  {gpa_bixian[1] :.4f}
任选  {gpa_renxuan[0]:.4f}  {gpa_renxuan[1]:.4f}'''
        print(s)

    def get_gpa(self, new_method=False) -> float:
        return Database.calc_gpa(self.courses, new_method=new_method)

    def get_gpa_bixian(self, new_method=False) -> float:
        _c = self.get_courses_bixian()
        return Database.calc_gpa(_c, new_method=new_method)

    def get_gpa_renxuan(self, new_method=False) -> float:
        _c = self.get_courses_renxuan()
        return Database.calc_gpa(_c, new_method=new_method)

    def show_course_of_type(self, _type):
        _c = []
        for c in self.courses:
            if c._type == _type:
                _c.append(c)
        Database.print_courses(_c)

    def add_course(self, course: Course):
        course.id = len(self.courses)    # O(1)
        self.courses.append(course)

    def save(self, path: str):
        print("saving...")
        with open(path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            for c in self.courses:
                lis = c.to_list()
                print(lis)
                writer.writerow(lis)
        print("done saving")

    def load(self, path: str):
        print("reading...")
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.courses = []
            for row in reader:
                print(row)
                course = Course()
                course.from_list(row)
                self.courses.append(course)
        print("done reading")

    def clear(self):
        self.courses = []
        print('清空课程信息完毕')

    @staticmethod
    def print_courses(courses: list):
        if len(courses) == 0:
            print("空")
            return
        print(Formatter.header_row())
        for c in courses:
            print(c)

    @staticmethod
    def calc_gpa(courses: list, new_method=False) -> float:
        if len(courses) == 0:
            return 0.0
        s = 0.0
        cntCred = 0
        for c in courses:
            if utils.isgrade(c.grade) and c.grade != 'P' and c.grade != 'F':
                s += utils.grade_to_float(c.grade, new_method=new_method) * c.credit
                cntCred += c.credit
        return s / cntCred
