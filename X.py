x = input("Xinter ==> ")  
PLUS = "Plus" 
MINUS = "Minus"
DIV = "Division"
MUL = "Multiplication"
nums = "1234567890"
INT = 'INT' 
FLOAT = 'FLOAT'
OPAREN="LPAREN"
CPAREN="RPAREN"
PRINT="PRINT"
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.curr_char = None
        self.tokens = []
        self.advance()

    def advance(self):
        self.pos += 1
        self.curr_char = self.text[self.pos] if self.pos < len(self.text) else None

    def tokenize(self):
        while self.curr_char is not None:
            if self.curr_char.isspace():
                self.advance()
            elif self.curr_char == "+":
                self.tokens.append(PLUS)
                self.advance()
            elif self.curr_char == "-":
                self.tokens.append(MINUS)
                self.advance()
            elif self.curr_char == "/":
                self.tokens.append(DIV)
                self.advance()
            elif self.curr_char == "*":
                self.tokens.append(MUL)
                self.advance()
            elif self.curr_char == "(":
                self.tokens.append(OPAREN)
                self.advance()
            elif self.curr_char == ")":
                self.tokens.append(CPAREN)
                self.advance()
            elif self.curr_char in nums or self.curr_char == ".":
                self.tokens.append(self._parse_number())
            else:
                raise ValueError(f"Unexpected character: {self.curr_char}")
        return self.tokens

    def _parse_number(self):
        num_str = ""
        dots = 0
        while self.curr_char is not None and (self.curr_char in nums or self.curr_char == "."):
            if self.curr_char == ".":
                if dots == 1:
                    raise ValueError("Invalid number format: Too many dots in number")
                dots += 1
            num_str += self.curr_char
            self.advance()

        if dots == 0:
            return f'{INT}: {int(num_str)}'
        else:
            return f'{FLOAT}: {float(num_str)}'
lexer = Lexer(x)
tokens = lexer.tokenize()
print(tokens)

