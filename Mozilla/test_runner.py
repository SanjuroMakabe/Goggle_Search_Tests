import unittest
import test1
import test2
import test3

BorkTestSuite = unittest.TestSuite()
BorkTestSuite.addTest(unittest.makeSuite(test1.CoffeeMachine))
BorkTestSuite.addTest(unittest.makeSuite(test2.CoffeeMachineBorkBig))
BorkTestSuite.addTest(unittest.makeSuite(test3.CoffeeMachineBork))
print("count of tests: " + str(BorkTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(BorkTestSuite)