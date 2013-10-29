from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class GCCLexer(RegexLexer):
    name = 'GCC'
    aliases = 'gcc'

    tokens = {
        'root': [
            (r'\s+', Text),

            # GENERIC trees
            (r'(<)([a-z_]+)', bygroups(Punctuation, Name.Tag)),
            (r'>', Punctuation),

            # RTL trees
            (r'(\()([a-z_]+)((/)([a-z]+))?((:)([A-Z]+))?',
                bygroups(Punctuation, Name.Tag,
                    None, Punctuation, Name,
                    None, Punctuation, Name)),
            (r'\(|\)', Punctuation),
            (r'\[|\]', Punctuation),
            (r';.*$', Comment.Single),

            # Common syntax elements: file names, etc.
            (r'([-_.a-zA-Z0-9]+)(:)([0-9]+)(:)([0-9]+)',
                bygroups(String, Punctuation, Number.Integer, Punctuation,
                    Number.Integer)),
            (r'/[^ ]+', String),
            (r'"[^"]*"', String),
            (r'0x[0-9a-f]+', Number.Hex),
            (r'-?[0-9]+', Number.Integer),
            (r'[-_.a-zA-Z]+', Name),
        ],
    }
