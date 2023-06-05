import unittest
from unittest.loader import TestLoader
from unittest.runner import TextTestRunner
from pathlib import Path


def run_tests(test_file_path=str(Path.cwd() / 'tests')):
    test_loader = TestLoader()
    test_suite = test_loader.discover(test_file_path, pattern='*_test.py')

    test_runner = TextTestRunner()
    test_runner.run(test_suite)
