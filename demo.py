from gini.semantics import Bottle,Concept

bottle = Bottle()

def print_me(stuff):
    print repr(stuff)

print_concept = Concept('print', ['print','show','list','blah'])
print_concept.action = print_me
bottle.vocab = [
    print_concept,
    Concept('say', ['say','speak','sprechen']),
    Concept('money', ['money','moolah','cash','denaros']),
    Concept('self', ['me','user'])
]

string = 'Show me the money'
print 'Processing string "%s"' % string
bottle.process_string(string)
print ''

bottle.guess = True
for search in ['m*','mool','rechen']:
    print 'Searching for examples matching "%s"' % search
    print bottle.match_all_concepts(search)
    print ''