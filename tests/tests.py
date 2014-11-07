"""
Lot of tests dido data integration done.
"""

import unittest

# Preparing for tests...
import sys
import os

pkg_dir = os.path.abspath(os.path.pardir)
sys.path.append(pkg_dir)
from dido import Extraction, Transform, Loader

class TestExtraction(unittest.TestCase):
    """
    Tests as 'extraction' behaves of ETL's process
    """

    def test_instance_of_extraction(self):
        ext = Extraction()
        self.assertIsInstance(ext, Extraction)

class TestTransform(unittest.TestCase):
    """
    Tests as 'transform' behaves of ETL's process
    """

    def test_instance_of_transform(self):
        transform = Transform()
        self.assertIsInstance(transform, Transform)
        
class TestLoader(unittest.TestCase):
    """
    Tests as 'loading' behaves of ETL's process
    """
    
    def test_instance_of_loader(self):
        loader = Loader()
        self.assertIsInstance(loader, Loader)

if __name__ == '__main__':
    unittest.main()
