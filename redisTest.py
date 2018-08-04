from  redis import StrictRedis

class Base(object):
    def __init__(self):
        self.r = StrictRedis(host='localhost',port=6379,db=0)

class TestString(Base):

    def test_set(self):
        rest = self.r.set('user3','Logan')
        print(rest)
        return rest

    def test_get(self):
        rest = self.r.get('user2')
        print(rest)
        return rest

class TestSet(Base):
    def test_sadd(self):
        li=['Cat','Dog']
        result=self.r.sadd('zoo2',*li)
        print(result)

        result = self.r.smembers('zoo2')
        print(result)

    def test_srem(self):
        result = self.r.srem('zoo2','Cat')
        print(result)
        result = self.r.smembers('zoo2')
        print(result)


def main():
    # str_obj = TestString()
    # str_obj.test_set()
    # str_obj.test_get()

    set_obj = TestSet()
    set_obj.test_srem()
    # set_obj.test_sadd()



if __name__ == '__main__':
    main()