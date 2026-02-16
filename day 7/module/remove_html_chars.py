def help_menu():
    print(
    """
    This is the help menu
    the package has 3 methods
    """
    )
    print(help_menu.__doc__)


    
def remove_html_chars(html_input: str)-> str:
    for ch in '<>/':
        html_input=html_input.replace(ch,"")

def remove_char(input_string, rem_ove):
    print(input_string.replace(rem_ove, ""))

