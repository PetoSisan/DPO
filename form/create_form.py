from form.SingleChoiceQuestion import SingleChoiceQuestion
from form.Form import Form


def create_form() -> Form:
    answers = {
        """Stavbu nemožno pripojiť k distribučnej sústave, pretože
        stavba nie je elektroenergetickým zariadením ani odberným elektrickým zariadením""": None,
               
        """Stavbu nemožno pripojiť k distribučnej sústave, pretože
        v dosahu miesta stavby sa nenachádza distribučná sústava, alebo sa nenachádza distribučná sústava v
        dostatočnej kapacite pre pripojenie stavby a spoločnosť Západoslovenská distribučná a stavebník sa nedohodli
        na rozšírení distribučnej sústavy: Na pripojenie do distribučnej sústavy je potrebné uzavrieť zmluvu o
        pripojení do distribučnej sústavy, na základe ktorej bude dohodnuté rozšírenie distribučnej sústavy a
        zabezpečená kapacita v distribučnej sústave.""": None,

        """Stavbu nemožno pripojiť k distribučnej sústave, pretože
        v dosahu miesta stavby sa nachádza distribučná sústava, ale neboli určené technické podmienky pripojenia:
        Na pripojenie do distribučnej sústavy je potrebné uzavrieť zmluvu o pripojení do distribučnej sústavy,
        na základe ktorej bude zabezpečená kapacita v distribučnej sústave.""": None  
    }

    question = SingleChoiceQuestion("Stavbu nemožno pripojiť k distribučnej sústave, pretože",
                       "Možnosti pripojenia k distribučnej sústave", answers)
    
    answers = {
        "Stavbu možno pripojiť k distribučnej sústave. V dosahu miesta stavby sa nachádza distribučná sústava." : None,

        """Stavbu možno pripojiť k distribučnej sústave. V dosahu miesta stavby sa nenachádza distribučná sústava
        – pre účely pripojenia stavby dôjde k jej rozšíreniu. """: None,

        "Stavbu nemožno pripojiť k distribučnej sústave, pretože ...": question
    }
    
    question = SingleChoiceQuestion("Možnosti pripojenia k distribučnej sústave",
                 "Možnosti pripojenia k distribučnej sústave", answers)
    
    answers = {
        "Stavebný zámer" : question,
        "Predĺženie platnosti rozhodnutia o stavebnom zámere": question,
        "Ohlásenie stavieb a stavebných úprav": question,
        "Kolaudácia" : question,
        "Zmena užívania stavby": question,
        "Dočasné užívanie stavby": question,
        "Predčasné užívanie stavby": question
    }

    question = SingleChoiceQuestion("Typ konania pred stavebným úradom",
                 "Typ konania pred stavebným úradom", answers)
    
    answers = {
        """nesúhlas s posudzovanou dokumentáciou
        Odôvodnenie: 
        Posudzovaná projektová dokumentácia nie je zhotovená v súlade
        so štandardami spoločnosti Západoslovenská distribučná.""": question,

        """nesúhlas s posudzovanou dokumentáciou
        Odôvodnenie:
        Stavba má byť umiestnená v ochrannom pásme elektrických vedení
        a elektroenergetických zariadení spoločnosti Západoslovenská distribučná podľa § 43 zákona o energetike
        a jej realizáciou môže dôjsť k ich poškodeniu alebo ohrozeniu ich prevádzky.""": question,

        """nesúhlas s posudzovanou dokumentáciou
        Odôvodnenie:
        Stavba má byť umiestnená v ochrannom pásme elektronickej komunikačnej siete spoločnosti Západoslovenská distribučná
        podľa § 23 zákona o elektronických komunikáciách a jej realizáciou môže dôjsť k ohrozeniu jej bezpečnosti
        a spoľahlivosti.""": question,
 
    }

    justification = SingleChoiceQuestion("Odôvodnenie nesúhlasu", "Záver", answers)

    answers = {
        "súhlas s posudzovanou dokumentáciou": question,
        "súhlas s posudzovanou dokumentáciou s podmienkami uvedenými v tomto vyjadrení": question,
        "nesúhlas s posudzovanou dokumentáciou": justification
    }

    question = SingleChoiceQuestion("Záver k posudzovanej dokumentácií", "Záver", answers)

    return Form(question)
