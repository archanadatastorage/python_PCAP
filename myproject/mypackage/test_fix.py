import pytest

@pytest.fixture
def setup():
	print(" I will be called in the beginning")
	yield
	print(" I will be called in the end")

@pytest.mark.usefixtures("setup")
class TestExample:
	def test_fixturedemo(self):
		print(" demo will be executed after setup")

	def test_fixturedemo1(self):
		print(" demo1 will be executed after setup")