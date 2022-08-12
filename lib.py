import io
from io import StringIO, BytesIO

charLookup = {
    0: 'Ø',  # NUL Null 0x00 \0
    1: '.',  # SOH Start of Header
    2: '.',  # STX Start of Text
    3: '.',  # ETX End of Text
    4: '.',  # EOT End of Transmission
    5: '.',  # ENQ Enquiry
    6: '.',  # ACK Acknowledge
    7: '.',  # BEL Bell
    8: '.',  # BS Backspace
    9: '⇥',  # HT \t Horizontal Tab
    10: '↲',  # LF \n Line Feed
    11: '.',  # VT Vertical Tab
    12: '.',  # FF Form Feed
    13: '↲',  # CR \r Carriage Return
    14: '.',  # SO Shift Out
    15: '.',  # SI Shift In
    16: '.',  # DLE Data Link Escape
    17: '.',  # DC1 Device Control 1
    18: '.',  # DC2 Device Control 2
    19: '.',  # DC3 Device Control 3
    20: '.',  # DC4 Device Control 4
    21: '.',  # NAK Negative Acknowledge
    22: '.',  # SYN Synchronize
    23: '.',  # ETB End of Transmission Block
    24: '.',  # CAN Cancel
    25: '.',  # EM End of Medium
    26: '.',  # SUB Substitute
    27: '.',  # ESC Escape
    28: '.',  # FS File Separator
    29: '.',  # GS Group Separator
    30: '.',  # RS Record Separator
    31: '.',  # US Unit Separator
    32: ' ',  # space
    33: '!',
    34: '"',
    35: '#',
    36: '$',
    37: '%',
    38: '&',
    39: '\'',
    40: '(',
    41: ')',
    42: '*',
    43: '+',
    44: ',',
    45: '-',
    46: '.',
    47: '/',
    48: '0',  # 0
    49: '1',
    50: '2',
    51: '3',
    52: '4',
    53: '5',
    54: '6',
    55: '7',
    56: '8',
    57: '9',  # 9
    58: ':',
    59: ';',
    60: '<',
    61: '=',
    62: '>',
    63: '?',
    64: '@',
    65: 'A',  # A
    66: 'B',
    67: 'C',
    68: 'D',
    69: 'E',
    70: 'F',
    71: 'G',
    72: 'H',
    73: 'I',
    74: 'J',
    75: 'K',
    76: 'L',
    77: 'M',
    78: 'N',
    79: 'O',
    80: 'P',
    81: 'Q',
    82: 'R',
    83: 'S',
    84: 'T',
    85: 'U',
    86: 'V',
    87: 'W',
    88: 'X',
    89: 'Y',
    90: 'Z',  # Z
    91: '[',
    92: "\\",
    93: ']',
    94: '^',
    95: '_',
    96: '`',
    97: 'a',  # a
    98: 'b',
    99: 'c',
    100: 'd',
    101: 'e',
    102: 'f',
    103: 'g',
    104: 'h',
    105: 'i',
    106: 'j',
    107: 'k',
    108: 'l',
    109: 'm',
    110: 'n',
    111: 'o',
    112: 'p',
    113: 'q',
    114: 'r',
    115: 's',
    116: 't',
    117: 'u',
    118: 'v',
    119: 'w',
    120: 'x',
    121: 'y',
    122: 'z',  # z
    123: '{',
    124: '|',
    125: '}',
    126: '~',
    127: '.',  # DEL Delete

    # End of ASCII

    128: '.',
    129: '.',
    130: '.',
    131: '.',
    132: '.',
    133: '.',
    134: '.',
    135: '.',
    136: '.',
    137: '.',
    138: '.',
    139: '.',
    140: '.',
    141: '.',
    142: '.',
    143: '.',
    144: '.',
    145: '.',
    146: '.',
    147: '.',
    148: '.',
    149: '.',
    150: '.',
    151: '.',
    152: '.',
    153: '.',
    154: '.',
    155: '.',
    156: '.',
    157: '.',
    158: '.',
    159: '.',
    160: '.',
    161: '.',
    162: '.',
    163: '.',
    164: '.',
    165: '.',
    166: '.',
    167: '.',
    168: '.',
    169: '.',
    170: '.',
    171: '.',
    172: '.',
    173: '.',
    174: '.',
    175: '.',
    176: '.',
    177: '.',
    178: '.',
    179: '.',
    180: '.',
    181: '.',
    182: '.',
    183: '.',
    184: '.',
    185: '.',
    186: '.',
    187: '.',
    188: '.',
    189: '.',
    190: '.',
    191: '.',
    192: '.',
    193: '.',
    194: '.',
    195: '.',
    196: '.',
    197: '.',
    198: '.',
    199: '.',
    200: '.',
    201: '.',
    202: '.',
    203: '.',
    204: '.',
    205: '.',
    206: '.',
    207: '.',
    208: '.',
    209: '.',
    210: '.',
    211: '.',
    212: '.',
    213: '.',
    214: '.',
    215: '.',
    216: '.',
    217: '.',
    218: '.',
    219: '.',
    220: '.',
    221: '.',
    222: '.',
    223: '.',
    224: '.',
    225: '.',
    226: '.',
    227: '.',
    228: '.',
    229: '.',
    230: '.',
    231: '.',
    232: '.',
    233: '.',
    234: '.',
    235: '.',
    236: '.',
    237: '.',
    238: '.',
    239: '.',
    240: '.',
    241: '.',
    242: '.',
    243: '.',
    244: '.',
    245: '.',
    246: '.',
    247: '.',
    248: '.',
    249: '.',
    250: '.',
    251: '.',
    252: '.',
    253: '.',
    254: '.',
    255: '•',  # 0xFF
}


def hexdump(src: BytesIO, chunk_size: int = 32, split_size: int = 8) -> str:
    s = StringIO()

    while data := src.read(chunk_size):
        offset = src.seek(0, io.SEEK_CUR)
        s.write('{0:05d} {0:04x}'.format(offset - len(data)))
        s.write(' | ')

        # Hex
        for i, d in enumerate(data):
            if i != 0 and i % split_size == 0:
                s.write('  ')

            s.write("{:02x} ".format(d))

        if len(data) != chunk_size:
            s.write('   ' * (chunk_size - len(data)))
            s.write('  ' * int((chunk_size - len(data)) / split_size))

        s.write(" | ")

        # ASCII
        for i, d in enumerate(data):
            if i != 0 and i % split_size == 0:
                s.write('  ')

            c = chr(d)
            if c.isprintable():
                s.write(c)
            else:
                s.write(charLookup[d])
        s.write("\n")

    return s.getvalue()
