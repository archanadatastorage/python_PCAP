import pytest


def myfunc():
	return 3


def test_SecondProgram():
	msg = "hello"
	assert msg=="hi","strings not matching"

def test_myfun():
	assert myfunc() == 6," test is failed"