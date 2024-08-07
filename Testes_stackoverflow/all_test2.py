import glob
import unittest

def load_tests(loader, tests, pattern):
    test_files = glob.glob('test_*.py')
    modules = [f[:-3] for f in test_files]  
    suites = [loader.loadTestsFromName(module) for module in modules]
    return unittest.TestSuite(suites)

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = load_tests(loader, None, None)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
