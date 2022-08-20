import utils
from course import Course
from database import Database


def prompt_course() -> Course:
    '''
    prompts user to enter info of a course

    returns:
        Course object with the info inputter by user
    '''
    name = ""
    cred = 0
    grade = .0
    _type = 'mandatory'
    name = input("名（串）：")
    print("学分（整）：")
    cred = utils.promptint()
    while True:
        grade = input("绩点（字母）：").upper()
        if utils.isgrade(grade):
            break
    while True:
        inp = input("类（必选：0，限选：1，任选：2）：")
        if inp == '0' or inp == 'mandatory' or inp == '必修':
            _type = '必修'
        elif inp == '1' or inp == 'limited' or inp == '限选':
            _type = '限选'
        elif inp == '2' or inp == 'free' or inp == '任选':
            _type = '任选'
        else:
            continue  # 重新请求输入
        break
    return Course(name=name, credit=cred, grade=grade, _type=_type)


def main_menu():
    db = Database()

    while True:
        print("""< 请输入指令 >
load： 载入数据
gpa：  显示 GPA 信息
show： 显示所有课程
graph：显示 GPA 随学期的变化
cred： 显示学分
exit： 退出

< 以下 3 个指令不建议使用 >
save： 保存
new：  新建
add：  添加""")
        cmd = input(">>> ")
        if cmd == 'add':
            course = prompt_course()
            print('获得', course)
            print("确定添加? [y/n]（或者[s/b]）")
            confirm = utils.promptyesno()
            if confirm:
                db.add_course(course)
        elif cmd == 'new':
            db.clear()
        elif cmd == 'gpa':
            db.print_gpa()
        elif cmd == 'gpanew':
            print("GPA (new):", db.get_gpa(new_method=True))
        elif cmd == 'show':
            if len(cmd) == 1:
                db.show_all()
            elif cmd[1] == 'renxuan':
                db.show_renxuan()
            elif cmd[1] == 'bixian':
                db.show_bixian()
        elif cmd == 'save':
            fname = input("文件名（略去格式）：")
            path = "./data/{}.csv".format(fname)
            db.save(path)
        elif cmd == 'load':
            fname = input("文件名（略去格式）：")
            path = "./data/{}.tsv".format(fname)
            db.load(path)
        elif cmd == 'graph':
            db.graph()
        elif cmd == 'cred':
            db.print_cred()
        elif cmd == 'exit':  # 退出程序
            break


if __name__ == '__main__':
    main_menu()