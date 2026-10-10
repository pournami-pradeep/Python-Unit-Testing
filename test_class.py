from my_class import MyClass


class TestMyClass:

    def test_add(self):
        cls = MyClass()
        res = cls.addition(3,4)
        assert res == 7

    def test_sub(self):
        cls = MyClass()
        res = cls.subtraction(3,4)
        assert res == 1
