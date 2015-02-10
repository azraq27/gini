from gini.semantics import Bottle,Concept

bottle = Bottle()

def print_me(stuff):
    print repr(stuff)

print_concept = Concept('print', ['show','list','blah'])
print_concept.action = print_me
bottle.vocab = [
    print_concept,
    Concept('say', ['speak','sprechen']),
    Concept('money', ['moolah','cash','denaros']),
    Concept('self', ['me','user'])
]

bottle.process('Show me the money')