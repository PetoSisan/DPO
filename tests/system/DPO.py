from glob import glob
from os import unlink
from pathlib import Path
from shutil import copy
from tempfile import NamedTemporaryFile

from main import DPO


def make_temp(path: Path) -> Path:
    original_file = Path(path)

    with NamedTemporaryFile(delete=False) as temp_file:
        temp_path = Path(temp_file.name)

    copy(original_file, temp_path)
    unlink(original_file)

    return temp_path


def clean_temp(temp_path: Path) -> None:
    original_file = Path("šišan.xml")
    copy(temp_path, original_file)
    unlink(temp_path)


DPO_FILE_PATTERN = \
    "[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9] - DPO.docx"

SUCCESSFULL_PATTERN = "DPO-log_úspešne*.txt"
UNSUCCESSFULL_PATTERN = "DPO-log_neúspešne*.txt"


def DPO_OK_test() -> None:
    retcode = DPO()
    assert retcode == 0
    pattern = SUCCESSFULL_PATTERN
    logs = glob(pattern)
    assert len(logs) == 1
    log = logs[0]

    pattern = DPO_FILE_PATTERN
    files = glob(pattern)
    assert len(files) == 1

    file = files[0]
    project_id = file.split(" ")[0]

    with open(log, "r") as f:
        searched_lines = 0
        lines = f.readlines()

        for line in lines:
            if "Záznam o priebehu spracovaní žiadosti stavby " + \
               f's ID "{project_id}":\n' == line:
                searched_lines += 1

            if "Program prebehol úspešne.\n" == line:
                searched_lines += 1

            if f'Výstup môžete nájsť v súbore "{file}".\n' == line:
                searched_lines += 1

        assert searched_lines == 3


def DPO_NOK_test() -> None:
    path = Path("šišan.xml")
    exists = path.exists()
    success = True

    if exists:
        temp = make_temp(path)

    try:
        retcode = DPO()
        assert retcode == 1
        pattern = UNSUCCESSFULL_PATTERN
        logs = glob(pattern)
        assert len(logs) == 1
        log = logs[0]

        pattern = DPO_FILE_PATTERN
        files = glob(pattern)
        assert len(files) == 0

        with open(log, "r") as f:
            assert any(
                "Záznam o priebehu spracovaní žiadosti stavby s ID" in line
                for line in f
            )
            assert any("Vyhodená chyba:" in line for line in f)

    except AssertionError as e:
        print(e)
        success = False

    finally:
        if exists:
            clean_temp(temp)
        if not success:
            assert False


def cleanup() -> None:
    patterns = [SUCCESSFULL_PATTERN, UNSUCCESSFULL_PATTERN, DPO_FILE_PATTERN]

    for pattern in patterns:
        files = glob(pattern)
        for file in files:
            unlink(file)
