import os
import sys
import json
import shutil

path = sys.argv[1] if len(sys.argv) >=2 else "/Users/rohith/Downloads"

with open(
    r"config.json", "r",
) as config:
    config = json.load(config)

extension_category_mapper = {}

for dir in config.keys():
    for ext in config[dir]:
        extension_category_mapper[ext.lower()] = dir

files = [_ for _ in os.listdir(path) if os.path.isfile(os.path.join(path, _))]

categories = [
    (
        extension_category_mapper[file.split(".")[-1]]
        if file.split(".")[-1].lower() in extension_category_mapper.keys()
        else "_other"
    )
    for file in files
]

for category in categories:
    folderpath = os.path.join(path, category)
    os.mkdir(os.path.join(path, category)) if not os.path.exists(folderpath) else None


if not files:
    sys.exit(0)


for file in files:
    extension = file.split(".")[-1]
    src = os.path.join(path, file)
    if extension.lower() in extension_category_mapper:
        dst = os.path.join(path, extension_category_mapper[extension], file)
    else:
        dst = os.path.join(path, "_other", file)

    try:
        shutil.move(src=src, dst=dst)
    except:
        pass
