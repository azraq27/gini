import gini

bottle = gini.semantics.Bottle()

def print_me(stuff):
    print repr(stuff)

bottle.actions = {'print':print_me}
bottle.vocab = {
    'print': ['show','list','blah'],
    'say': ['speak','sprechen'],
    'money': ['moolah','cash','denaros'],
    'self': ['me','user']
}

bottle.process('Show me the money')