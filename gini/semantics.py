from fuzzywuzzy import fuzz
import fnmatch

def matches_from_list(item,options,fuzzy=90):
    '''Returns the indices of the members of ``options`` that best matches ``item``. Will prioritize
    exact matches, then filename-style matching, then fuzzy matching (``fuzzy`` or greater, out of 100, match)'''
    matches = []
    
    # Exact matches
    if item in options:
        matches += [i for i in xrange(len(options)) if options[i]==item]
    
    # Filename-style matches
    matches += [options.index(x) for x in fnmatch.filter(options,item) if options.index(x) not in matches]
    
    # Fuzzy matches
    matches += [i for i in xrange(len(options)) if fuzz.ratio(item,options[i])>=fuzzy if i not in matches]
    
    return matches

def best_match_from_list(item,options,fuzzy=90):
    '''Returns the best match from :meth:`matches_from_list` or ``None`` if no good matches'''
    matches = matches_from_list(item,options,fuzzy)
    if len(matches)>0:
        return matches[0]
    return None

def match_and_classify(item,option_dict,fuzzy=90):
    '''Takes a dict where keys are an abstract name of a type, and the values are lists of
    examples. Will try to match the ``item`` to one of the examples, and then return a tuple
    of the matching (type,example)'''
    
    examples = [a for b in option_dict.values() for a in b]
    best_match = best_match_from_list(item,examples,fuzzy)
    if best_match!=None:
        best_match = examples[best_match]
        for item_type in option_dict:
            if best_match in option_dict[item_type]:
                return (item_type,best_match)
    return None

class Bottle(object):
    '''Container for semantic information (and magical creatures)'''
    def __init__(self):
        #: dict of possible actions, and corresponding methods
        self.actions = {}
        #: dict of abstract names and exemplars
        self.vocab = {}
    
    def process(self,string):
        items = string.split()
        for item in items:
            c = match_and_classify(item,self.vocab)
            if c and c[0] in self.actions:
                del(items[items.index(item)])
                self.actions[c[0]](items)