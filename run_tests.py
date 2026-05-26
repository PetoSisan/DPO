from tests.unit.form import create_form_test
from tests.system.DPO import DPO_OK_test
from tests.system.DPO import DPO_NOK_test
from tests.system.DPO import cleanup


def main() -> None:
    create_form_test()

    cleanup()
    DPO_OK_test("šišan.xml")
    cleanup()
    DPO_NOK_test("hello_world.xml")
    cleanup()


if __name__ == "__main__":
    main()