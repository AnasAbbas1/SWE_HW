import unittest
from util_api.test_compare_versions_api import TestCompareVersionsApi
from math_api.test_math_apis import TestMathAPIs

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(TestCompareVersionsApi))
test_suite.addTest(unittest.makeSuite(TestMathAPIs))

unittest.TextTestRunner().run(test_suite)