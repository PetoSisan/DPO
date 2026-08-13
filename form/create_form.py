from form.Form import Form
from form.SingleChoiceQuestion import SingleChoiceQuestion


def create_form() -> Form:
    answers = {
        "Stavbu nemožno pripojiť k distribučnej sústave, pretože\n"
        "stavba nie je elektroenergetickým zariadením "
        "ani odberným elektrickým zariadením\n": None,

        "Stavbu nemožno pripojiť k distribučnej sústave, pretože\n"
        "v dosahu miesta stavby sa nenachádza distribučná sústava,\n"
        "alebo sa nenachádza distribučná sústava v dostatočnej kapacite\n"
        "pre pripojenie stavby a spoločnosť Západoslovenská distribučná\n"
        "a stavebník sa nedohodli na rozšírení distribučnej sústavy:\n"
        "Na pripojenie do distribučnej sústavy je potrebné uzavrieť zmluvu\n"
        "o pripojení do distribučnej sústavy,\n"
        "na základe ktorej bude dohodnuté rozšírenie distribučnej sústavy\n"
        "a zabezpečená kapacita v distribučnej sústave.\n": None,

        "Stavbu nemožno pripojiť k distribučnej sústave, pretože\n"
        "v dosahu miesta stavby sa nachádza distribučná sústava, "
        "ale neboli určené\n"
        "technické podmienky pripojenia: Na pripojenie do distribučnej "
        "sústavy je potrebné\n"
        "uzavrieť zmluvu o pripojení do distribučnej sústavy, "
        "na základe ktorej bude\n"
        "zabezpečená kapacita v distribučnej sústave.\n": None,
    }

    question = SingleChoiceQuestion(
        "Stavbu nemožno pripojiť k distribučnej sústave, pretože",
        "Možnosti pripojenia k distribučnej sústave",
        answers,
    )

    answers = {
        "Stavbu možno pripojiť k distribučnej sústave.\n"
        "V dosahu miesta stavby sa nachádza distribučná sústava.\n": None,

        "Stavbu možno pripojiť k distribučnej sústave.\n"
        "V dosahu miesta stavby sa nenachádza distribučná "
        "sústava – pre účely\n"
        "pripojenia stavby dôjde k jej rozšíreniu.\n": None,

        "Stavbu nemožno pripojiť k distribučnej sústave, "
        "pretože ...\n": question,
    }

    question = SingleChoiceQuestion(
        "Možnosti pripojenia k distribučnej sústave",
        "Možnosti pripojenia k distribučnej sústave",
        answers,
    )

    answers = {
        "Stavebný zámer\n": question,
        "Predĺženie platnosti rozhodnutia o stavebnom zámere\n": question,
        "Ohlásenie stavieb a stavebných úprav\n": question,
        "Kolaudácia\n": question,
        "Zmena užívania stavby\n": question,
        "Dočasné užívanie stavby\n": question,
        "Predčasné užívanie stavby\n": question,
    }

    question = SingleChoiceQuestion(
        "Typ konania pred stavebným úradom",
        "Typ konania pred stavebným úradom",
        answers,
    )

    answers = {
        "nesúhlas s posudzovanou dokumentáciou\n"
        "Odôvodnenie:\n"
        "Posudzovaná projektová dokumentácia nie je zhotovená v súlade\n"
        "so štandardami spoločnosti Západoslovenská distribučná.\n": question,

        "nesúhlas s posudzovanou dokumentáciou\n"
        "Odôvodnenie:\n"
        "Stavba má byť umiestnená v ochrannom pásme elektrických vedení\n"
        "a elektroenergetických zariadení spoločnosti Západoslovenská\n"
        "distribučná podľa § 43 zákona o energetike a jej realizáciou\n"
        "môže dôjsť k ich poškodeniu alebo "
        "ohrozeniu ich prevádzky.\n": question,

        "nesúhlas s posudzovanou dokumentáciou\n"
        "Odôvodnenie:\n"
        "Stavba má byť umiestnená v ochrannom pásme elektronickej\n"
        "komunikačnej siete spoločnosti Západoslovenská distribučná\n"
        "podľa § 23 zákona o elektronických komunikáciách a jej realizáciou\n"
        "môže dôjsť k ohrozeniu jej bezpečnosti a spoľahlivosti.\n": question,
    }

    justification = SingleChoiceQuestion(
        "Odôvodnenie nesúhlasu",
        "Záver",
        answers
    )

    answers = {
        "súhlas s posudzovanou dokumentáciou\n": question,
        "súhlas s posudzovanou dokumentáciou s podmienkami "
        "uvedenými v tomto vyjadrení\n": question,
        "nesúhlas s posudzovanou dokumentáciou\n": justification,
    }

    question = SingleChoiceQuestion(
        "Záver k posudzovanej dokumentácií", "Záver", answers
    )

    return Form(question)
