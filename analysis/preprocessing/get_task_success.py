#! /bin/python3

"""
This script looks at all .zipfiles with results and writes the task's
success to a given .csv-File with task-metadata.
"""

import os

import pandas as pd
import zipfile

CUTOFF_SUCCESS = 3
CUTOFF_PARTIAL = 1

path = "data/raw_data/survey_data/"
n_users = 20
n_tasks = 8

metadata_path = "data/raw_data/task_data.csv"

if __name__ == '__main__':

    metadata = pd.read_csv(metadata_path, sep=",")
    metadata.set_index("index")
    cols = metadata.columns
    cols = list(map(lambda x: x.strip(), cols))
    metadata.columns = cols

    for i in range(n_users):
        # for each user
        for j in range(n_tasks):
            # for each task of user
            tasks_path = os.path.join(path, f"User{i+1}", f"task{j+1}")
            print(tasks_path)
            # collect all files in results-folder of current user
            try:
                files = os.listdir(tasks_path)
            except FileNotFoundError:
                print(tasks_path + ' not found')
                continue
            if len(files) != 1:
                # there's no clear candidate for the results file
                continue
            zip_file = os.path.join(tasks_path, files[0])

            # User i+1 has results of task j+1 in file zip_file
            with zipfile.ZipFile(zip_file) as z:
                n_files = len(z.infolist())
                print(n_files)
                if n_files >= CUTOFF_SUCCESS:
                    success = 2
                elif n_files >= CUTOFF_PARTIAL:
                    success = 1
                else:
                    success = 0

                user_id = i+1
                task_id = j+1

                metadata.loc[(metadata.user == user_id) & (
                    metadata.task == task_id), "success"] = success
    print(metadata)
    metadata.to_csv(metadata_path, sep=",", index=False)
