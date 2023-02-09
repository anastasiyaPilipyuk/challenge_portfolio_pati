import unittest
from unittest import TestLoader, TestSuite, makeSuite

from test_cases.check_add_player_page import TestAddPlayerPage
from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage


def full_suite():
    loader = TestLoader()
    test_suite = loader.loadTestsFromTestCase(TestLoginPage)
    test_suite.addTests(loader.loadTestsFromTestCase(TestAddPlayerPage))
    test_suite.addTests(loader.loadTestsFromTestCase(Test))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
