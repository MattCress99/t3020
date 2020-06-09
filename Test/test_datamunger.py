import unittest
import datamunger
import os

this_dir = os.path.dirname(__file__)

class TestExclude(unittest.TestCase):
	
	def test_Calc_Total_Fail(self):
		ListNum = [432, 1, 14, 28, 35, 47, 63, 75, 84, 90]
		Check_Res = datamunger.calc_total(ListNum)
		self.assertNotEqual(Check_Res, ListNum[0])
	
	def test_Calc_Total_Pass(self):
		ListNum = [342, 1, 14, 28, 35, 47, 58, 75, 84, 90]
		Check_Res = datamunger.calc_total(ListNum)
		self.assertEqual(Check_Res, ListNum[0])
	
	def test_Check_Row_Pass(self):
		listCurrent = "342, 1, 14, 28, 35, 47, 58, 75, 84, 90"
		ThisList = listCurrent.split(",")
		prev = [0,10,20,30,40,50,60,70,80,90,100]
		result = datamunger.check_row(1, prev, ThisList)
		self.assertTrue(result)

	def test_Check_Row_Fail(self):
		listCurrent = "342, , 14, 28, 35, 47, 58, 75, 84, 90"
		ThisList = listCurrent.split(",")
		prev = [0,10,20,30,40,50,60,70,80,90,100]
		result = datamunger.check_row(1, prev, ThisList)
		self.assertFalse(result)
	

if __name__ == '__main__':
	unittest.main()
