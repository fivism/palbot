import re, random


def decider(self, e):
    rps = [u"\u270A", u"\u270B", u"\u270C"]
    things = re.split(", or |, | or ", e.input, flags=re.IGNORECASE)
    if len(things) > 1: 
        item = random.randint(0, len(things) - 1)
        e.output = "{}: {}".format(e.nick, things[item].strip())
        if things[0].strip() == things[1].strip():
            e.output = "when the illusion of choice is presented choosing is meaningless"
    if e.input in rps:
        item = random.randint(0, 2)
        e.output = "{} : {}".format(e.nick, rps[item])
        
    return e
decider.command = "bot"

def dec_borgi (self, e):
    return decider(self, e)
dec_borgi.command = "borgi"

def dec_Borgi (self, e):
    return decider(self, e)
dec_Borgi.command = "Borgi"
