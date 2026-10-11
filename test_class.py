from my_class import MyClass
import pytest

class TestMyClass:

    @pytest.fixture
    def data(self):
        return [1,2,3,4,5]

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

    def test_data(self, data):
        assert 1 in data
        assert 6 in data
