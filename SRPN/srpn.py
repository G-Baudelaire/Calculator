# This is your SRPN file. Make your changes here.
from SRPN.lexer.lexer import Lexer
from SRPN.tokens.tokenizer import Tokenizer

tokenizer = Tokenizer()
lexer = Lexer()


def process_command(command):
    substrings = lexer.read_user_input(command)
    tokens = tokenizer.read_substrings(substrings)


# This is the entry point for the program.
# Do not edit the below
if __name__ == "__main__":
    while True:
        try:
            cmd = input()
            pc = process_command(cmd)
            if pc != None:
                print(str(pc))
        except:
            exit()
