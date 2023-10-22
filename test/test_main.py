"""
Test

"""
import unittest
import os
from EtlTool.main import extract

class TestExtractFunction(unittest.TestCase):

    def test_extract(self):

        input_url = "https://raw.githubusercontent.com/nickeubank/practicaldatascience/master/Example_Data/world-small.csv"
        output_file_path = "EtlTool/data/WorldSmall.csv"

        if os.path.exists(output_file_path):
            os.remove(output_file_path)

        result = extract(url=input_url, file_path=output_file_path)
        self.assertEqual(result, output_file_path)
        self.assertTrue(os.path.exists(output_file_path))

        if os.path.exists(output_file_path):
            os.remove(output_file_path)



if __name__ == '__main__':
    unittest.main()