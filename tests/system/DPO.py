from main import DPO
from glob import glob

from os import unlink



DPO_FILE_PATTERN = "[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9] - DPO.docx"
SUCCESSFULL_PATTERN = "DPO-log_úspešne*.txt"
UNSUCCESSFULL_PATTERN = "DPO-log_neúspešne*.txt"


def DPO_OK_test(input_file: str) -> None:
    retcode = DPO(input_file)
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


def DPO_NOK_test(input_file: str) -> None:
    retcode = DPO(input_file)
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


def cleanup() -> None:
    patterns = [SUCCESSFULL_PATTERN, UNSUCCESSFULL_PATTERN, DPO_FILE_PATTERN]

    for pattern in patterns:
        files = glob(pattern)
        for file in files:
            unlink(file)
