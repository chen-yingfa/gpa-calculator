import csv
from matplotlib import pyplot as plt
from course import Course
from formatter import Formatter
import utils


class Database():
    def __init__(self):
        self.courses = []

    def get_courses_bixian(self):
        _courses = []
        for c in self.courses:
            if c.is_bixian():
                _courses.append(c)
        return _courses

    def get_courses_renxuan(self):
        _courses = []
        for c in self.courses:
            if c.is_renxuan():
                _courses.append(c)
        return _courses

    def show_all(self):
        Database.print_courses(self.courses)

    def get_cred_bixian(self, pf_or_w):
        cred = 0
        for c in self.courses:
            if c.is_bixian() and c.is_pf_or_w() == pf_or_w:
                cred += c.credit
        return cred

    def get_cred_renxuan(self, pf_or_w):
        cred = 0
        for c in self.courses:
            if c.is_renxuan() and c.is_pf_or_w() == pf_or_w:
                cred += c.credit
        return cred

    def get_cred(self, pf_or_w) -> tuple:
        # 返回总学分
        bixian_cred = self.get_cred_bixian(pf_or_w)
        renxuan_cred = self.get_cred_renxuan(pf_or_w)
        return bixian_cred, renxuan_cred

    def print_cred(self):
        bixian, renxuan = self.get_cred(False)
        bixian_pfw, renxuan_pfw = self.get_cred(True)
        cred = bixian + renxuan, bixian_pfw + renxuan_pfw
        s = f'''
           总  等级  P/F
  总学分：{    cred[0] + cred[1]:>3}   {cred[0]:>3}  {    cred[1]:>3}
必限学分：{  bixian + bixian_pfw:>3}   { bixian:>3}  { bixian_pfw:>3}
任选学分：{renxuan + renxuan_pfw:>3}   {renxuan:>3}  {renxuan_pfw:>3}
'''
        print(s)

    def print_gpa_each_sem(self):
        sem_to_gpa = self.get_gpa_all_sem()
        sem_to_gpa_new = self.get_gpa_all_sem(new_method=True)
        print("       学期  旧算法  新算法")
        for sem in sem_to_gpa.keys():
            print(f"{sem}  {sem_to_gpa[sem]:.4f}  {sem_to_gpa_new[sem]:.4f}")

    def print_gpa(self):
        '''
        输出各种 GPA
        '''
        self.print_cred()
        self.print_gpa_each_sem()
        gpa_all = (self.get_gpa(), self.get_gpa(new_method=True))
        gpa_bixian = (self.get_gpa_bixian(), self.get_gpa_bixian(new_method=True))
        gpa_renxuan = (self.get_gpa_renxuan(), self.get_gpa_renxuan(new_method=True))

        s = f'''
      旧算法  新算法
所有  {gpa_all[0]    :.4f}  {gpa_all[1]    :.4f}
必限  {gpa_bixian[0] :.4f}  {gpa_bixian[1] :.4f}
任选  {gpa_renxuan[0]:.4f}  {gpa_renxuan[1]:.4f}
'''
        print(s)

    def graph(self):
        sem_to_gpa = self.get_gpa_all_sem()
        sem_to_gpa_new = self.get_gpa_all_sem(new_method=True)
        gpa = list(sem_to_gpa.values())
        gpa_new = list(sem_to_gpa_new.values())
        plt.plot(gpa[1:], label="Old GPA")
        plt.plot(gpa_new[1:], label="New GPA")
        plt.legend()
        plt.ylabel("GPA")
        plt.xlabel("Semester")
        plt.savefig("gpa_to_sem.png")
        plt.show()

    def get_gpa(self, new_method=False) -> float:
        return Database.calc_gpa(self.courses, new_method=new_method)

    def get_gpa_bixian(self, new_method=False) -> float:
        _c = self.get_courses_bixian()
        return Database.calc_gpa(_c, new_method=new_method)

    def get_gpa_renxuan(self, new_method=False) -> float:
        _c = self.get_courses_renxuan()
        return Database.calc_gpa(_c, new_method=new_method)

    def show_renxuan(self):
        _c = [c for c in self.courses if c.is_renxuan()]
        Database.print_courses(_c)

    def show_bixian(self):
        _c = [c for c in self.courses if c.is_bixian()]
        Database.print_courses(_c)

    def show_course_of_type(self, _type):
        _c = [c for c in self.courses if c._type == _type]
        Database.print_courses(_c)

    def get_gpa_sem(self, sem: str, new_method=False) -> float:
        _c = [c for c in self.courses if c.sem == sem]
        return Database.calc_gpa(_c, new_method=new_method)

    def get_gpa_all_sem(self, new_method=False) -> dict:
        '''
        return: dict of all with semester as key, and gpa as value
        '''
        sem_to_courses = {}
        for c in self.courses:
            if c.sem not in sem_to_courses:
                sem_to_courses[c.sem] = []
            sem_to_courses[c.sem].append(c)
        sem_to_gpa = {}
        for sem, courses in sem_to_courses.items():
            sem_to_gpa[sem] = Database.calc_gpa(courses, new_method=new_method)
        return sem_to_gpa

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
        try:
            with open(path, 'r', encoding='utf-8') as f:
                print("reading...")
                reader = csv.reader(f)
                self.courses = []
                for row in reader:
                    print(row)
                    course = Course()
                    course.from_list(row)
                    self.courses.append(course)
                print("done reading")
        except FileNotFoundError:
            print(f"< 找不到文件：\"{path}\" >")

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
        if cntCred == 0:
            return 0
        return s / cntCred
