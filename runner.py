from pathlib import Path
from subprocess import run
from shutil import copy, move
from datetime import datetime


def main():
    cwd = Path.cwd()
    script = Path(cwd / "main.py")
    test_dir = Path(cwd / "XML")
    data = Path(cwd / "šišan.xml")
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    tmp = Path(cwd / f"šišan_{timestamp}.xml")

    if data.exists():
        move(data, tmp)

    for file in test_dir.rglob("*.xml"):
        print(f"Running test case: {file}")
         
        copy(file, data)
        run(["python", str(script)]) # subprocess.run([exe_path])
        data.unlink()

        print(" ")    
    if tmp.exists():
        move(tmp, data)


if __name__ == "__main__":
    main()
