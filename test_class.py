from my_class import MyClass
import pytest

class TestMyClass:

    def test_add(self):
        cls = MyClass()
        res = cls.addition(3,4)
        assert res == 7

    def test_sub(self):
        cls = MyClass()
        res = cls.subtraction(3,4)
        assert res == -1

    def test_divide(self):
        cls = MyClass()
        with pytest.raises(ZeroDivisionError):
            cls.divide(2,0)
