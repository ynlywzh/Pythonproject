import os

class Student:
    def __init__(self, id, name, age, gender, score):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.filepath = 'students.txt'
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    data = line.strip().split(',')
                    student = Student(data[0], data[1], data[2], data[3], data[4])
                    self.students.append(student)
        else:
            with open(self.filepath, 'w') as f:
                f.write('')
# 定义注册方法
    def register(self):
        id = input('请输入学号：')
        name = input('请输入姓名：')
        age = input('请输入年龄：')
        gender = input('请输入性别：')
        score = input('请输入成绩：')
        student = Student(id, name, age, gender, score)
        self.students.append(student)
        with open(self.filepath, 'a') as f:
            f.write(f'{id},{name},{age},{gender},{score}\n')
# 定义登录方法
    def login(self):
        id = input('请输入学号：')
        for student in self.students:
            if student.id == id:
                print(f'欢迎登录，{student.name}！')
                return student
        print('学号不存在！')
        return None


# 定义删除方法
    def delete(self):
        id = input('请输入要删除的学号：')
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                with open(self.filepath, 'w') as f:
                    for s in self.students:
                        f.write(f'{s.id},{s.name},{s.age},{s.gender},{s.score}\n')
                print(f'学号为{id}的学生删除成功！')
                return
        print('学号不存在！')



# 定义修改方法

    def modify(self):
        id = input('请输入要修改的学号：')
        for student in self.students:
            if student.id == id:
                name = input(f'请输入新姓名（原姓名为：{student.name}）：')
                age = input(f'请输入新年龄（原年龄为：{student.age}）：')
                gender = input(f'请输入新性别（原性别为：{student.gender}）：')
                score = input(f'请输入新成绩（原成绩为：{student.score}）：')
                student.name = name
                student.age = age
                student.gender = gender
                student.score = score
                with open(self.filepath, 'w') as f:
                    for s in self.students:
                        f.write(f'{s.id},{s.name},{s.age},{s.gender},{s.score}\n')
                print(f'学号为{id}的学生修改成功！')
                return
        print('学号不存在！')

    def view(self):
        if len(self.students) == 0:
            print('无可查看用户')
        else:
            for student in self.students:
                print(f'学号：{student.id}，姓名：{student.name}，年龄：{student.age}，性别：{student.gender}，成绩：{student.score}')

    def run(self):
        while True:
            print('欢迎使用学生信息管理系统！')
            print('1. 注册')
            print('2. 登录')
            print('3. 删除')
            print('4. 修改')
            print('5. 查看')
            print('6. 退出')
            choice = input('请选择功能：')
            if choice == '1.注册':
                self.register()
            elif choice == '2.登录':
                self.login()
            elif choice == '3.删除':
                self.delete()
            elif choice == '4.修改':
                self.modify()
            elif choice == '5.查看':
                self.view()
            elif choice == '6.退出':
                print('欢迎下次再来！')
                break
            else:
                print('请选择正确的功能！')

if __name__ == '__main__':
    sms = StudentManagementSystem()
    sms.run()