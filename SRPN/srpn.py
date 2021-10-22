# This is your SRPN file. Make your changes here.
from SRPN.lexer.lexer import Lexer
from SRPN.parse.parser import Parser
from SRPN.stack.stack import Stack
from SRPN.tokens.tokenizer import Tokenizer

tokenizer = Tokenizer()
lexer = Lexer()
parser = Parser()
stack = Stack()


def process_command(command):
    substrings = lexer.read_user_input(command)
    tokens = tokenizer.read_substrings(substrings)
    parser.read_tokens(stack, tokens)


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
