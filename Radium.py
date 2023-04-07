import hashlib
import os
import threading
import requests

from CONSTS import TEMP_DIR, FILES_TO_DOWNLOAD, FILE_URL




def try_except(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper

class Radium:
    def __init__(self, folder_name:str, files_to_download:list, url:str):
        self.folder_name = folder_name
        self.files_to_download = files_to_download
        self.url = url
    
    @try_except
    def download_file(self, url:str, file_path:str):
        self.response = requests.get(url)
        self.head = str(self.response.headers)
        os.makedirs(self.folder_name, exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(self.head)
        return self.head

    @try_except
    def download_threading(self):
        self.threads = []
        for file_name in self.files_to_download:
            url = f'{self.url}{file_name}'
            file_path = os.path.join(self.folder_name, file_name)
            self.thread = threading.Thread(target=self.download_file, args=(url, file_path))
            self.threads.append(self.thread)
            self.thread.start()
            
    @try_except
    def stop_threading(self):
        for thread in self.threads:
            thread.join()
        

    @try_except
    def hashing(self):
        self.hashes = {}
        for file_name in self.files_to_download:
            file_path = os.path.join(self.folder_name, file_name)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
                self.hashes[file_name] = file_hash
        return self.hashes
                
    @try_except
    def print_hashes(self):
        for file_name, file_hash in self.hashes.items():
            print(f'{file_name}: {file_hash}')
    
    @try_except        
    def ipi(self):
        return "ipi"



if __name__ == '__main__':
    radium = Radium(TEMP_DIR, FILES_TO_DOWNLOAD, FILE_URL)
    radium.download_threading()
    radium.stop_threading()
    radium.hashing()
    radium.print_hashes()