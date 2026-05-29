from main import DPO
from glob import glob

from os import unlink

from shutil import copy
from tempfile import NamedTemporaryFile
from pathlib import Path

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



DPO_FILE_PATTERN = "[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9] - DPO.docx"
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
    project_id = file.split(' ')[0]

    with open(log, "r") as f:
        assert any(f"Záznam o priebehu spracovaní žiadosti stavby s ID \"{project_id}\":" in line for line in f)
        assert any(f"Program prebehol úspešne. Výstup môžete nájsť v súbore \"{file}\"." in line for line in f)


def DPO_NOK_test() -> None:
    path = Path("šišan.xml")
    exists = path.exists()
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
            assert any(f"Záznam o priebehu spracovaní žiadosti stavby s ID" in line for line in f)
            assert any(f"Vyhodená chyba:" in line for line in f)
    
    except AssertionError as e:
        if exists:
            clean_temp(temp)
        print(e)
        assert False
    
    if exists:
        clean_temp(temp)


def cleanup() -> None:
    patterns = [SUCCESSFULL_PATTERN, UNSUCCESSFULL_PATTERN, DPO_FILE_PATTERN]

    for pattern in patterns:
        files = glob(pattern)
        for file in files:
            unlink(file)
