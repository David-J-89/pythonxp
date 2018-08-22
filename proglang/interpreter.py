###################
#LEXER
###################


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0


###################
#MAIN           
###################
with open("script.txt", "r") as f:
    data = f.read()

print (data)