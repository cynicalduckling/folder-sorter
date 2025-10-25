import os
import sys
import json
import shutil
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

path: str = sys.argv[1] if len(sys.argv) >= 2 else os.getcwd()

with open(
    r"config.json",
    "r",
) as config:
    config: dict[str | list] = json.load(config)

extension_category_mapper: dict = {}

for dir in config.keys():
    for ext in config[dir]:
        extension_category_mapper[ext.lower()] = dir

files: list[str] = [
    _ for _ in os.listdir(path) if os.path.isfile(os.path.join(path, _))
]

categories: list[str] = [
    (
        extension_category_mapper[file.split(".")[-1]]
        if file.split(".")[-1].lower() in extension_category_mapper.keys()
        else "_other"
    )
    for file in files
]

for category in categories:
    folderpath: str = os.path.join(path, category)
    os.mkdir(os.path.join(path, category)) if not os.path.exists(folderpath) else None


if not files:
    sys.exit(0)


for file in files:
    extension: str = file.split(".")[-1]
    src: str = os.path.join(path, file)
    if extension.lower() in extension_category_mapper:
        dst: str = os.path.join(path, extension_category_mapper[extension], file)
    else:
        dst: str = os.path.join(path, "_other", file)

    try:
        shutil.move(src=src, dst=dst)
    except Exception as error:
        logging.error(f"Error moving file {file}: {error}")