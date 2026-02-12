def form_wanted() -> bool:
    """Checks whether user wants to fill the form.

    Params:
        
    
    Returns:
        `True`, if yes, `False` otherwise
    """

    answer: str = input("Prajete si vypĺňať 'Vyjadrenie' k žiadosti DPO? [ano/nie] \n")
    return True if answer.lower() == "ano" else False