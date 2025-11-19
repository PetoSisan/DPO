from pathlib import Path
import subprocess
from shutil import copy, move
from datetime import datetime
import argparse
import os
from sys import exit


def parse_args():
    """Parses arguments from cmd.

    Args:
        None
    
    Returns:
        Namespace: Namespace with --dir arg.
    """

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

All = int
Successfull = int
def process_dir(source_dir: Path,
                target_dir: Path = Path.cwd(),
                script_name: str = "main.py",
                target_name: str = "šišan.xml",
                file_type: str = "xml",
                exe_name: str = "main.exe") -> tuple[All, Successfull]:
    """Process files in 'source_dir' using 'script'.
    
    Args:
        source_dir (Path): Path to directory with files which will be processed using 'script'
        target_dir (Path): Path to directory for locating 'script', 'exe' and 'target'
        script_name (str): Name of the script which will run
        target_name (str): Name of the file, which will serve as an input for script (everything relevant from 'source_dir'
              is step by step copied here. For more info regarding choice of default value of this arg see README.md)
        file_type (str): type of processed files
        exe_name (str): Name to .exe file which serves as a substitute to 'script' in deployment app. (TODO)

    Returns:
        None
    
    Raises:
        ValueError: if 'source_dir' is not a directory
        potentially other types of error based on the 'script'
    """
    if not source_dir.is_dir() or not target_dir.is_dir():
        raise ValueError(str(source_dir))
    
    target = Path(target_dir / target_name)
    script = Path(target_dir / script_name)
    exe = Path(target_dir / exe_name)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    tmp = Path(target_dir / f"šišan_{timestamp}.{file_type}")

    if target.exists():
        move(target, tmp)

    all = 0
    error = 0

    for file in source_dir.rglob(f"*.{file_type}"):
        try:
            all += 1
            error += run(file, target, script)
        except Exception as e:
            print(f"Pri spracovani subora \"{file}\" vznikla neocakavana chyba :(.")
            print(f"Vyhodená chyba: {e}")
            error += 1
        
    if tmp.exists():
        move(tmp, target)
    
    return (all, all - error)

def run(source: Path, data: Path, script: Path):
    """ Runs 'script' with data from 'source'.

    Args:
        source (str): Path to input file with data
        data (str): Path to file where data are copied
    """
    print(f"Running case: \"{source}\"")    
    os.link(source, data)
    
    completed_process: subprocess.CompletedProcess \
        = subprocess.run(["python", str(script)]) # subprocess.run([exe_path])
    
    data.unlink()
    print(" ")
    return completed_process.returncode

def main():
    args = parse_args()
    data_dir = Path(args.dir)

    try:
        files_count, successfull = process_dir(data_dir)
    
    except ValueError as e:
        print(f"\"{data_dir}\" nie je priečinok. Skontrolujte prosím vstupný parameter a skúste znovu prosím.")
        print(f"Vyhodená chyba: \n {str(e)}")

    except Exception as e:
        print("Pri behu programu vznikla neočakávaná chyba: ")
        print(f"Vyhodená chyba: \n {str(e)}")
    
    print(f"Program úspešne spracoval z priečinka \"{str(data_dir)}\" {successfull} z {files_count} súborov.")
    input("Press Enter to exit...")

    return 0 if successfull == files_count else 1


if __name__ == "__main__":
    main()
