from  redis import StrictRedis


class TestString(object):

    def __init__(self):
        self.r = StrictRedis(host='localhost',port=6379,db=0)

    def test_set(self):
        rest = self.r.set('user3','Logan')
        print(rest)
        return rest

    def test_get(self):
        rest = self.r.get('user2')
        print(rest)
        return rest



def main():
    str_obj = TestString()
    # str_obj.test_set()
    str_obj.test_get()


if __name__ == '__main__':
    main()