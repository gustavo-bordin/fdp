import re
import os


class Token:
    def __init__(self, token_type, value, line_number):
        self.token_type = token_type
        self.value = value
        self.line_number = line_number

    def __repr__(self):
        return f"{self.token_type}({self.value})"


class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.token_specs = [
            ('ARROW', r'->'),
            ('AFTER', r'after'),
            ('BEFORE', r'before'),
            ('TEXT', r'".*?"'),
            ('LABEL', r'.+?(?=(?: ->|\?>))'),
            ('WHITESPACE', r'\s+'),
        ]
        self.token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_specs)
        self.line_number = 1
        self.tokens = []

    def tokenize(self):
        for match in re.finditer(self.token_regex, self.input_text):
            token_type = match.lastgroup
            token_value = match.group()

            if token_type == 'WHITESPACE':
                self.line_number += token_value.count('\n')
                continue
            
            token = Token(token_type, token_value, self.line_number)
            self.tokens.append(token)

        return self.tokens
