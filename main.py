import os

root_dir = input("Enter current directory: ")

files = [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, f))]

dirs_list = dict()

for f in files:
    key = f.split(".")[-1]
    try:
        dirs_list[key].append(f)
    except KeyError:
        dirs_list[key] = [f]

for folder, files in dirs_list.items():
    current_folder = os.path.join(root_dir, folder)
    if not os.path.exists(current_folder):
        os.mkdir(os.path.join(root_dir, folder))
    for file in files:
        os.replace(os.path.join(root_dir, file), os.path.join(current_folder, file))


print(dirs_list)

