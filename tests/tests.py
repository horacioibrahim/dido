"""
Lot of tests dido data integration done.
"""

import unittest

# Preparing for tests...
import sys
import os

pkg_dir = os.path.abspath(os.path.pardir)
sys.path.append(pkg_dir)

from dido import (Extraction, Transform, Loader, 
        Metadata, didotypes, exceptions)


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


class TestMetadata(unittest.TestCase):
    """
    Tests metadata objects
    """
    def test_instance_of_metadata(self):
        meta = Metadata()
        self.assertIsInstance(meta, Metadata)

    def test_setter_metadata(self):
        meta = Metadata()
        meta.metadata = dict(col1='str', col2='int')
        self.assertIsInstance(meta.metadata, dict)

    def test_to_json(self):
        pass

    def test_validate_metadata(self):
        pass

class TestDidoTypes(unittest.TestCase):

    def test_validate(self):
        z = didotypes.ZipCodeBR()
        self.assertEqual(z.validate('7058-070'), None)
        self.assertEqual(z.validate('70258070'), None)

    def test_validate_exception(self):
        z = didotypes.ZipCodeBR()
        self.assertRaises(exceptions.InvalidDidoType, z.validate, '7025z800')
    
    def test_validate_integer(self):
        z = didotypes.ZipCodeBR()
        self.assertEqual(z.validate(70258010), None)



if __name__ == '__main__':
    unittest.main()
