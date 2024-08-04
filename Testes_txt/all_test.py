import glob
import unittest

def load_tests(loader, tests, pattern):
    test_files = glob.glob('test_*.py')
    modules = [f[:-3] for f in test_files]  # Remove the .py extension
    suites = [loader.loadTestsFromName(module) for module in modules]
    return unittest.TestSuite(suites)

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = load_tests(loader, None, None)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\nResults Summary:")
    print(f"Ran {result.testsRun} tests.")
    print(f"Errors: {len(result.errors)}")
    for test, err in result.errors:
        print(f"Error in {test.id()}:\n{err}")
    print(f"Failures: {len(result.failures)}")
    for test, fail in result.failures:
        print(f"Failure in {test.id()}:\n{fail}")
