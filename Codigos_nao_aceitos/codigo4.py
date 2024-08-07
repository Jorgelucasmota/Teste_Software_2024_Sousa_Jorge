from unittest import TestLoader, TextTestRunner, TestSuite
from uclid.test.test_symbols import test_symbols
from uclid.test.test_patterns import TestPatterns

if __name__ == "__main__":

    loader = TestLoader()
    tests = [
        loader.loadTestsFromTestCase(test)
        for test in (TestSymbols, TestPatterns)
    ]
    suite = TestSuite(tests)

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)