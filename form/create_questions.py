from form.Question import Question
from form.Form import Form




def create_questions() -> Form:
    answers = {
        "stavba nie je elektroenergetickým zariadením ani odberným elektrickým zariadením": None,
               
        """v dosahu miesta stavby sa nenachádza distribučná sústava, alebo sa nenachádza distribučná sústava v
        dostatočnej kapacite pre pripojenie stavby a spoločnosť Západoslovenská distribučná a stavebník sa nedohodli
        na rozšírení distribučnej sústavy: Na pripojenie do distribučnej sústavy je potrebné uzavrieť zmluvu o
        pripojení do distribučnej sústavy, na základe ktorej bude dohodnuté rozšírenie distribučnej sústavy a
        zabezpečená kapacita v distribučnej sústave.""": None,

        """v dosahu miesta stavby sa nachádza distribučná sústava, ale neboli určené technické podmienky pripojenia:
        Na pripojenie do distribučnej sústavy je potrebné uzavrieť zmluvu o pripojení do distribučnej sústavy,
        na základe ktorej bude zabezpečená kapacita v distribučnej sústave.""": None  
    }

    question = Question("Stavbu nemožno pripojiť k distribučnej sústave, pretože",
                       "Možnosti pripojenia k distribučnej sústave", answers)
    
    answers = {
        "Stavbu možno pripojiť k distribučnej sústave. V dosahu miesta stavby sa nachádza distribučná sústava." : None,

        """Stavbu možno pripojiť k distribučnej sústave. V dosahu miesta stavby sa nenachádza distribučná sústava
        – pre účely pripojenia stavby dôjde k jej rozšíreniu. """: None,

        "Stavbu nemožno pripojiť k distribučnej sústave, pretože ... ": question
    }
    
    question = Question("Možnosti pripojenia k distribučnej sústave",
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

    question = Question("Typ konania pred stavebným úradom",
                 "Typ konania pred stavebným úradom", answers)
    

    # TODO

    return Form(question)
