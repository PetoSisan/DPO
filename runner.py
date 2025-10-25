from pathlib import Path
import subprocess
from shutil import copy, move
from datetime import datetime
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Optional --dir folder with .xml files serving as an data input")

     # Add optional argument
    parser.add_argument(
        "--dir", 
        type=str, 
        help="Path to the directory with .xml files.", 
        default="./XML"
    )
    
    args = parser.parse_args()
    return args


def run(data_dir: Path, dir: Path = Path.cwd()) -> None:

    script = Path(dir / "main.py")
    exe_path = Path(dir / "main.exe")
    data = Path(dir / "šišan.xml")

    if not data_dir.is_dir():
        raise ValueError()

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    tmp = Path(dir / f"šišan_{timestamp}.xml")

    if data.exists():
        move(data, tmp)

    for file in data_dir.rglob("*.xml"):
        print(f"Running case: \"{file}\"")
            
        copy(file, data)
        subprocess.run(["python", str(script)]) # subprocess.run([exe_path])  
        data.unlink()
        print(" ")
        
    if tmp.exists():
        move(tmp, data)
    
    return

def main():
    args = parse_args()
    data_dir = Path(args.dir)

    success = "úspešne"

    try:
        run(data_dir)
    
    except ValueError as e:
        print(f"\"{data_dir}\" nie je priečinok. Skontrolujte prosím vstupný parameter a skúste znovu prosím.")
        print(f"Vyhodená chyba: \n {str(e)}")
        success = "neúspešne"

    except Exception as e:
        print("Pri behu programu vznikla neočakávaná chyba: ")
        print(f"Vyhodená chyba: \n {str(e)}")
        success = "neúspešne"
    
    print(f"Spracovanie priečinka \"{str(data_dir)}\" bolo {success}.")
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
