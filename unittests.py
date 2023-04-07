import unittest
import os
import shutil
import hashlib
from Radium import Radium

class RadiumTestCase(unittest.TestCase):

    def setUp(self):
        self.temp_dir = 'temp'
        self.files_to_download = ['wemake-python-styleguide.cfg', 'pyproject.toml', 'requirements.txt']
        self.file_url = 'https://gitea.radium.group/radium/project-configuration/raw/HEAD/'
        self.radium = Radium(self.temp_dir, self.files_to_download, self.file_url)
        self.radium.download_threading()
        self.radium.stop_threading()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_download(self):
        for file_name in self.files_to_download:
            file_path = os.path.join(self.temp_dir, file_name)
            self.assertTrue(os.path.exists(file_path))

    def test_hashing(self):
        hashes = self.radium.hashing()
        for file_name, file_hash in hashes.items():
            file_path = os.path.join(self.temp_dir, file_name)
            with open(file_path, 'rb') as f:
                expected_hash = hashlib.sha256(f.read()).hexdigest()
                self.assertEqual(file_hash, expected_hash)

if __name__ == '__main__':
    unittest.main()
