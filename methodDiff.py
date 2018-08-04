class A(object):

    #self和cls的区别不是强制的，只是PEP8中一种编程风格，
    # slef通常用作实例方法的第一参数，
    # cls通常用作类方法的第一参数。
    # 即通常用self来传递当前类对象的实例，cls传递当前类对象

    #普通的类方法fun()需要通过self参数隐式的传递当前类对象的实例
    def fun(self,x):
        print('executing fun (%s %s)' % (self,x))
        print('self:',self)

    #@classmethod修饰的方法class_fun()需要通过cls参数传递当前类对象
    @classmethod
    def class_fun(cls,x):
        print('executing class_fun (%s,%s)' % (cls,x))

    #@staticmethod修饰的方法定义与普通函数是一样的。
    @staticmethod
    def static_fun(x):
        print('executing static_fun (%s)'% x)


if __name__ == '__main__':
    a=A()
    print(a.fun)
    print(a.class_fun)
    print(a.static_fun)

    #fun可通过实例a调用，类对像A直接调用会参数错误。
    a.fun(1)
    #class_fun通过类对象或对象实例调用。
    A.class_fun(1)
    a.class_fun(1)
    #static_fun通过类对象或对象实例调用。
    A.static_fun(1)
    a.static_fun(1)
