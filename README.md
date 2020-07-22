# gpa-calculator
For THU

一晚上为了计算GPA写出来的烂东西。

## 用途
计算自己的GPA，包括总GPA，必限GPA，任选课GPA，新旧算法。

## 用法
1. 根据提供的courses_template.csv模板，填写自己的课程成绩信息。
建议从info.tsinghua.edu.cn进入“全部成绩单”，拷贝到excel，手动去掉多余的列，然后导出csv文件。
2. 运行 `$ python main.py`，然后：
```
$ load
$ your_file.csv
$ show
>>> （显示你的所有课程）
$ gpa
>>> （显示你的GPA，6种计算方法）
```
注：程序提示的add可用，但不建议用
