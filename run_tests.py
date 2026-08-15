from tests.system.DPO import DPO_NOK_test, DPO_OK_test, cleanup
from tests.unit.form import create_form_test


def main() -> None:
    create_form_test()
    cleanup()
    DPO_OK_test()
    cleanup()
    DPO_NOK_test()
    cleanup()


if __name__ == "__main__":
    main()
