import os

from main import addition


def test_addition_int():
    assert addition(2,3) == 5


def test_addition_float():
    assert addition(2.4, 3.0) == 5.4

def test_file(tmpdir):
    file_path = tmpdir.join('test.txt')
    file_path.write("hello world!")
    assert file_path.read() == "hello world!"

def test_env(monkeypatch):
    monkeypatch.setenv("VAR", "pytest")
    assert os.getenv('VAR') == "pytest"