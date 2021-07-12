import unittest
from task import *

class TestConfig(unittest.TestCase):
	"""docstring for TestConfig"""

	def test1(self):
		c = test(5,'peru','2020-04-19 00:00:00+00:00','2020-04-19 00:00:00+00:00',2,'frequent_segment')
		self.assertEqual(c,'2640.0')

	def test2(self):
		c = test(112,'peru','2020-04-19 00:00:00+00:00','2020-04-19 00:00:00+00:00',11,'recency_segment')
		self.assertEqual(c,'2640.0')

	def test3(self):
		c = test(5,'peru','2020-04-19 00:00:00+00:00','2020-04-19 00:00:00+00:00',2,'')
		self.assertEqual(c,'no values')

	def test4(self):
		c = test('','peru','2020-04-19 00:00:00+00:00','2020-04-19 00:00:00+00:00',2,'frequent_segment')
		self.assertEqual(c,'')




if __name__ == '__main__':
	unittest.main()



