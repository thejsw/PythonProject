import json
from pathlib import Path
from folderSetting import OUT_DIR

OUT_LIST = OUT_DIR / f"{Path(__file__).stem}.json"

def dump_dirnames(base_dir: Path) -> None:
    dirs = []
    for path in base_dir.iterdir():
        if path.is_dir():
            dirs.append(path.as_posix())
    dirs_sorted = sorted(dirs)
    with open(OUT_LIST, "w", encoding="utf-8") as fp:
        json.dump(dirs_sorted, fp, ensure_ascii=False, indent=2)

def load_dirnames() -> list[str]:
    if OUT_LIST.is_file():
        with open(OUT_LIST, encoding="utf-8") as fp:
            return json.load(fp)
    
    return []

if __name__ == "__main__":
    dump_dirnames(Path.home())