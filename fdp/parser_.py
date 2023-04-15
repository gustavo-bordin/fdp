class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.current_token = None
        self.advance()

    def parse(self):
        instructions = []
        while self.current_token is not None:
            instruction = self.parse_instruction()
            instructions.append(instruction)
        return instructions

    def parse_instruction(self):
        label = self.parse_label()
        self.parse_arrow()
        after_text = self.parse_text('AFTER')
        before_text = self.parse_text('BEFORE')
        return {'label': label, 'after': after_text, 'before': before_text}

    def parse_label(self):
        return self.consume('LABEL').value

    def parse_arrow(self):
        self.consume('ARROW')

    def parse_text(self, expected_type):
        self.consume(expected_type)
        return self.consume('TEXT').value.strip('"')

    def consume(self, expected_type):
        token = self.current_token
        if token.token_type != expected_type:
            raise SyntaxError(f"Expected token '{expected_type}'")
        self.advance()
        return token

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
