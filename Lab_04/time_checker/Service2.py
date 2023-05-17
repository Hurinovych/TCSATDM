import time
import os

while True:
    directory = './times'
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as f:
                file_content = f.read()
            print('Log name:', filename)
            print('Log content:\n', file_content, '\n')
        #os.remove(file_path)
    time.sleep(10)