class Student(object):
    def __init__(self,name,score):
        # print(self)
        self.__name =name
        self.__score = score

    def print_scrore(self):
        print('%s:%s' % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_scrore(self):
        return self.__score

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        if 0<=score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'



if __name__ == '__main__':
    stu = Student('Logan',10)
    print(stu._Student__name)
    # print(  stu)
    # print(stu.name)
    # print(Student)
    stu.print_scrore()