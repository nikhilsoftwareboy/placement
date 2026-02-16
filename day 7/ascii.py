import pyfiglet

def ascii_art(s,a):
    output=pyfiglet.figlet_format(s,a)
    print(output)
def supported_fonts():
    Fonts=pyfiglet.FigletFont.getFonts()
    print(Fonts)

#ascii_art('hello','nikhil')
supported_fonts()
