import unittest
import sys

from setuptools import setup, find_packages, Command

class RunTests(Command):
    description = "run all tests for array-slicer"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        tests = unittest.TestLoader().discover('./tests')
        runner = unittest.TextTestRunner()
        results = runner.run(tests)
        sys.exit(not results.wasSuccessful())

setup(
    name='array_slicer',
    version='0.1.0',
    description='',
    long_description=open('README.md').read(),
    license='unlicence',
    author='Ken McLennan',
    url='https://github.com/kenmclennan/array-slicer',
    cmdclass={'test': RunTests},
    packages=find_packages(),
)