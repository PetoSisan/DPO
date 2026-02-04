def form_wanted() -> bool:
    """Checks whether user wants to fill the form.

    Params:
        
    
    Returns:
        `True`, if yes, `False` otherwise
    """

    answer: str = input("Prajete si vypĺňať formulár ohľadom informácií v druhej časti dokumentu DPO? \n [ano/nie]")
    return True if answer.lower() == "ano" else False