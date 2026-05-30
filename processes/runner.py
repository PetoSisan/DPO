from pathlib import Path
from shutil import move
from datetime import datetime
import argparse
import os

from main import main as xml_script
from typing import Callable


def parse_args():
    """Parses arguments from cmd.

    Params:
        None

    Returns:
        `Namespace`: `Namespace` with '--dir' arg.
    """

    parser = argparse.ArgumentParser(
        description="Optional --dir folder with .xml files serving as an data input"
    )

    # Add optional argument
    parser.add_argument(
        "--dir",
        type=str,
        help="Path to the directory with .xml files.",
        default="./XML",
    )

    args = parser.parse_args()
    return args


All = int
Successfull = int
FileType = str


def process_dir(
    source_dir: Path,
    file_type: str,
    scripts: dict[FileType, Callable[[], int]],
) -> tuple[All, Successfull]:
    """Process files in `source_dir` using `scripts.get(file_type)` script.

    Params:
        - `source_dir` (`Path`): Path to directory with files which will be processed using 'script'
        - `file_type` (`str`): type of processed files
        - `scripts` (`dict[FileType, Callable[[], int]]`): collection of all supported scripts
            which can be called in this function. Correct script (based on context) is chosen according
            `file_type` parameter


    Returns:
        -  `tuple[All, Successfull]` where:
            - 'All' represents number of files processed
            - 'Successfull' represents number of successfully processed files

    Raises:
        `ValueError`: if `source_dir` is not a directory or if `file_type` is not in scripts as a key with associated script
    """
    if not source_dir.is_dir():
        raise ValueError(
            f'"{source_dir}" nie je priečinok. Skontrolujte prosím vstupný parameter a skúste znovu prosím.'
        )

    script: Callable[[], int] = scripts.get(file_type)
    if script is None:
        raise ValueError(
            f'Zadaný formát súborov "{file_type}" nie podporovaný na spracovanie.'
        )

    target_dir = Path.cwd()
    target_name: str = f"šišan.{file_type}"
    target = Path(target_dir / target_name)

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
            os.link(file, target)
            error += run(script, target)
            target.unlink()

        except Exception as e:
            print(f'Pri spracovani subora "{file}" vznikla neocakavana chyba :(.')
            print(f"Vyhodená chyba: {e}")
            error += 1

    if tmp.exists():
        move(tmp, target)

    return (all, all - error)


def run(script: Callable[[], int], source: Path) -> int:
    """Runs `script` with data from `source`.

    Params:
        - `source` (`str`): Path to input file with data
        - `data` (`str`): Path to file where data are copied

    Returns:
        - `int`: return code of the script
    """
    print(f'Spracovávam súbor: "{source}"')
    rv = script()
    print(" ")
    return rv


def main() -> int:
    """Creates a 'DPOs' from files in `data_dir` with chosen file type with associated script.

    Params:
        None

    Returns:
        - `int`:
                `0` if no error occurs and all files were successfully processed
                `1` if either `data_dir` is not directory or a not supported `file_type` was chosen
                `2` if unexpected error occurs :(
                `3` if no error occures but not all files were successfully processed
    """
    args = parse_args()
    data_dir = Path(args.dir)

    SCRIPTS: dict[str, Callable[[], int]] = {"xml": xml_script}

    files_count = 0
    successfull = 0

    try:
        files_count, successfull = process_dir(data_dir, "xml", SCRIPTS)

    except ValueError as e:
        print(f"Pri spracovávaní priečinku {str(data_dir)} vznikla táto chyba: ")
        print(str(e))
        return 1

    except Exception as e:
        print("Pri behu programu vznikla neočakávaná chyba :(. ")
        print(f"Vyhodená chyba: \n {str(e)}")
        return 2

    print(
        f'Program úspešne spracoval z priečinka "{str(data_dir)}" {successfull} z {files_count} súborov.'
    )
    input("Press Enter to exit...")

    return 0 if successfull == files_count else 3


if __name__ == "__main__":
    main()
