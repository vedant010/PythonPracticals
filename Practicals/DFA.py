def DFA_strings_ends_with_a(text):
    return "Accepted" if q0(text) else "Rejected"

def q0(text):
    if text.startswith('b'):
        if len(text) == 1:
            return False
        else:
            return q0(text[1:])
    elif text.startswith('a'):
        if len(text) == 1:
            return True
        else:
            return q1(text[1:])
    else:
        return False

def q1(text):
    if text.startswith('a'):
        if len(text) == 1:
            return True
        else:
            return q1(text[1:])
    elif text.startswith('b'):
        if len(text) == 1:
            return False
        else:
            return q0(text[1:])
    else:
        return False

print(DFA_strings_ends_with_a("babababbababbaba"))
