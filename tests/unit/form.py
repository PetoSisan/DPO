from form.Form import Form
from form.create_form import create_form


def create_form_test() -> None:
    form: Form = create_form()
    assert form.get_current_question().row_name == "Záver"

    expected_row_names = [
        "Záver",
        "Záver",
        "Typ konania pred stavebným úradom",
        "Možnosti pripojenia k distribučnej sústave",
        "Možnosti pripojenia k distribučnej sústave",
    ]

    answers = [
        ["nesúhlas s posudzovanou dokumentáciou\n"],
        [
            "nesúhlas s posudzovanou dokumentáciou\n"
            "Odôvodnenie:\n"
            "Posudzovaná projektová dokumentácia nie je zhotovená v súlade\n"
            "so štandardami spoločnosti Západoslovenská distribučná.\n"
        ],
        ["Kolaudácia\n"],
        ["Stavbu nemožno pripojiť k distribučnej sústave, pretože ...\n"],
        [
            "Stavbu nemožno pripojiť k distribučnej sústave, pretože\n"
            "v dosahu miesta stavby sa nachádza distribučná sústava, ale neboli určené\n"
            "technické podmienky pripojenia: Na pripojenie do distribučnej sústavy je potrebné\n"
            "uzavrieť zmluvu o pripojení do distribučnej sústavy, na základe ktorej bude\n"
            "zabezpečená kapacita v distribučnej sústave.\n"
        ],
    ]

    expected_answers = [
        [
            "súhlas s posudzovanou dokumentáciou\n",
            "súhlas s posudzovanou dokumentáciou s podmienkami uvedenými v tomto vyjadrení\n",
            "nesúhlas s posudzovanou dokumentáciou\n",
        ],
        [
            "nesúhlas s posudzovanou dokumentáciou\n"
            "Odôvodnenie:\n"
            "Posudzovaná projektová dokumentácia nie je zhotovená v súlade\n"
            "so štandardami spoločnosti Západoslovenská distribučná.\n",
            "nesúhlas s posudzovanou dokumentáciou\n"
            "Odôvodnenie:\n"
            "Stavba má byť umiestnená v ochrannom pásme elektrických vedení\n"
            "a elektroenergetických zariadení spoločnosti Západoslovenská\n"
            "distribučná podľa § 43 zákona o energetike a jej realizáciou\n"
            "môže dôjsť k ich poškodeniu alebo ohrozeniu ich prevádzky.\n",
            "nesúhlas s posudzovanou dokumentáciou\n"
            "Odôvodnenie:\n"
            "Stavba má byť umiestnená v ochrannom pásme elektronickej\n"
            "komunikačnej siete spoločnosti Západoslovenská distribučná\n"
            "podľa § 23 zákona o elektronických komunikáciách a jej realizáciou\n"
            "môže dôjsť k ohrozeniu jej bezpečnosti a spoľahlivosti.\n",
        ],
        [
            "Stavebný zámer\n",
            "Predĺženie platnosti rozhodnutia o stavebnom zámere\n",
            "Ohlásenie stavieb a stavebných úprav\n",
            "Kolaudácia\n",
            "Zmena užívania stavby\n",
            "Dočasné užívanie stavby\n",
            "Predčasné užívanie stavby\n",
        ],
        [
            "Stavbu možno pripojiť k distribučnej sústave.\n"
            "V dosahu miesta stavby sa nachádza distribučná sústava.\n",
            "Stavbu možno pripojiť k distribučnej sústave.\n"
            "V dosahu miesta stavby sa nenachádza distribučná sústava – pre účely\n"
            "pripojenia stavby dôjde k jej rozšíreniu.\n",
            "Stavbu nemožno pripojiť k distribučnej sústave, pretože ...\n",
        ],
        [
            "Stavbu nemožno pripojiť k distribučnej sústave, pretože\n"
            "stavba nie je elektroenergetickým zariadením ani odberným elektrickým zariadením\n",
            "Stavbu nemožno pripojiť k distribučnej sústave, pretože\n"
            "v dosahu miesta stavby sa nenachádza distribučná sústava,\n"
            "alebo sa nenachádza distribučná sústava v dostatočnej kapacite\n"
            "pre pripojenie stavby a spoločnosť Západoslovenská distribučná\n"
            "a stavebník sa nedohodli na rozšírení distribučnej sústavy:\n"
            "Na pripojenie do distribučnej sústavy je potrebné uzavrieť zmluvu\n"
            "o pripojení do distribučnej sústavy,\n"
            "na základe ktorej bude dohodnuté rozšírenie distribučnej sústavy\n"
            "a zabezpečená kapacita v distribučnej sústave.\n",
            "Stavbu nemožno pripojiť k distribučnej sústave, pretože\n"
            "v dosahu miesta stavby sa nachádza distribučná sústava, ale neboli určené\n"
            "technické podmienky pripojenia: Na pripojenie do distribučnej sústavy je potrebné\n"
            "uzavrieť zmluvu o pripojení do distribučnej sústavy, na základe ktorej bude\n"
            "zabezpečená kapacita v distribučnej sústave.\n",
        ],
    ]

    for i, row_name in enumerate(expected_row_names):
        q = form.get_current_question()

        assert q is not None
        assert q.row_name == row_name

        for answer in expected_answers[i]:
            assert answer in q.answers.keys()

        form.add_answers(answers[i])
        assert form.qna[q.row_name] == answers[i]

        form.next_question(answers[i])

    assert form.get_current_question() is None
    assert len(form.qna) == 3
