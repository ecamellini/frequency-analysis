import sys


def substitute(text, dictionary):
    """Substitute each char in 'text'
    using 'dictionary' as a map for the
    substitution pattern."""
    output = ""
    for i in text:
        output = output + dictionary[i]
    return output


def rot13_dict():
    """Generate the rot13
    substitution dictionary"""
    d = {}
    for i in range(0, 13):
        char1 = chr(ord('a') + i)
        char2 = chr(ord(char1) + 13)
        d[char1] = char2
        d[char2] = char1
        char1 = chr(ord('A') + i)
        char2 = chr(ord(char1) + 13)
        d[char1] = char2
        d[char2] = char1
    return d

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print "Missing argument - Usage:"
        print "python rot13.py text"
        sys.exit()
    text = sys.argv[1]
    print substitute(text, rot13_dict())
