import os, json, shutil

with open(
    r"C:\Users\rohit\Documents\personal-projects\folder-sorter\config.json", "r"
) as config:
    config = json.load(config)

path = config["path"]

cat_mapper = {}

for dir in config["categories"].keys():
    for ext in config["categories"][dir]:
        cat_mapper[ext] = dir

files = [_ for _ in os.listdir(path) if os.path.isfile(os.path.join(path, _))]

categories = [
    (
        cat_mapper[file.split(".")[-1]]
        if file.split(".")[-1] in cat_mapper.keys()
        else "_other"
    )
    for file in files
]

for category in categories:
    folderpath = os.path.join(path, category)
    os.mkdir(os.path.join(path, category)) if not os.path.exists(folderpath) else None

for file in files:
    extension = file.split(".")[-1].lower()
    src = os.path.join(path, file)
    if extension in cat_mapper:
        dst = os.path.join(path, cat_mapper[extension], file)
    else:
        dst = os.path.join(path, "_other", file)

    try:
        shutil.move(src=src, dst=dst)
    except:
        pass
