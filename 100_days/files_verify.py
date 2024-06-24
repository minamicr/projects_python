import os

path = "c:/files"
file_paths = []
outer_join_list = []
file_parent_paths = [path + '/' + fd for fd in os.listdir(path)]

for folder in file_parent_paths:
   for filename in os.listdir(folder):
       file_paths.append(os.path.join(folder, filename))

file_list_db = ['content.jar', 'wlp-javaee8-20.0.0.10.zip']

if len(file_list_db) > 0:
    for filename in file_paths:
        print('incluindo ' + filename)
        outer_join_list = file_paths

        for file_db in file_list_db:
            if file_db in filename:
                outer_join_list.remove(filename)
                print('removendo ' + filename)
                break
else:
    outer_join_list = file_paths

for file in outer_join_list:
    print(file)