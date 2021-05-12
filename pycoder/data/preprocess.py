import os
import json
import shutil
from tqdm import tqdm
from pathlib import Path
from typing import List, Union

import pycoder.config as cfg
from pycoder.utils import formatter


def walk_clean(root_dir: Union[Path, str], keep_extensions: List = ["py"]):
    dir_walk = tqdm(os.walk(root_dir, topdown=False))

    empty_dirs = set()
    total_files = removed_files = 0

    print(f"Walking in the root directory {str(root_dir)}...")

    for root, dirs, files in dir_walk:
        is_file = False

        for file in files:
            if os.path.splitext(file)[1][1:] not in keep_extensions:
                (Path(root) / file).unlink()
                removed_files += 1

            else:
                is_file = True

            total_files += 1

        if not is_file:
            is_subdir = False

            for dir in dirs:
                if len(os.listdir(Path(root) / dir)) > 0:
                    is_subdir = True

            if not is_subdir:
                empty_dirs.add(Path(root).absolute())

        dir_walk.update()

    print("Removing empty directories...")
    for empty_dir in tqdm(empty_dirs):
        try:
            shutil.rmtree(empty_dir)

        except:
            continue

    print(
        f"Total {formatter((total_files-removed_files), color='g', bold=True)}/{formatter(total_files, color='g', bold=True)} belong to {keep_extensions} extensions."
    )


def index_files(root_dir: Union[Path, str], extensions: List[str] = ["py"]) -> None:
    dir_walk = tqdm(os.walk(Path(root_dir), topdown=False))
    files_to_index = []

    for root, _, files in dir_walk:
        for file in files:
            if os.path.splitext(file)[1][1:] in extensions:
                files_to_index.append(
                    {
                        "name": file,
                        "path": str(Path(root) / file),
                        "category": Path(root_dir).name,
                    }
                )
            dir_walk.update()

    print(
        formatter(
            f"Indexed files for {formatter(Path(root_dir).name, color='g', bold=True)} ",
            tick=True,
        )
    )

    return files_to_index


def index_files_from_root(root_dir: Union[Path, str], save_path: Union[Path, str]):

    files_to_index = []

    for keyword in cfg.KEYWORDS:
        files_to_index += index_files(Path(root_dir) / keyword)

    # in case the directory to store the index file doesn't exist
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)

    with open(save_path, "w") as fl:
        json.dump(files_to_index, fl)

    print(
        formatter(
            f"Saved the file successfully to {formatter(save_path, color='g', bold=True)}",
            tick=True,
        )
    )
