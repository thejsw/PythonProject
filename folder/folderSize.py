import json
from pathlib import Path
from folderSetting import OUT_DIR
from folderFunction import get_total_filesize
from folderList import load_dirnames

OUT_SIZE = OUT_DIR / f"{Path(__file__).stem}.json"

def dump_filesize_from_dirnames():
    dirs = load_dirnames()
    result = {}
    for path_str in dirs:
        path = Path(path_str)
        filesize = get_total_filesize(path, pattern="**/*")
        result[path.as_posix()] = filesize
    with open(OUT_DIR, "w", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent=2)

def load_filesize_per_dir() -> dict[str, int]:
    if OUT_SIZE.is_file():
        with open(OUT_SIZE, encoding="utf-8") as fp:
            return json.load(fp)
    return {}

if __name__ == "__main__":
    dump_filesize_from_dirnames()