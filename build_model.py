#!/usr/bin/env python
import re
from collections import defaultdict
import random
import numpy as np

from progress import ProgressMonitor

def default_tokenizer(text):
    for word in text.split():
        yield word

def bible_tokenizer(text):
    for word in text.split():
        if re.match(r'\d+:\d+', word) is not None: continue
        yield word.strip('\'"()')

TOKENIZERS = {
    'default': default_tokenizer,
    'bible': bible_tokenizer,
}

def main(inputfile, states, outputwords, tokenizer='default'):
    if tokenizer not in TOKENIZERS:
        ValueError('Unknown tokenizer: "%s"' % tokenizer)

    tokenize = TOKENIZERS[tokenizer]

    with open(inputfile, 'r+') as f:
        text = f.read()

    words = list(tokenize(text))
    model = defaultdict(lambda: defaultdict(int))
    prog = ProgressMonitor(total=(len(words) - states - 1),
                           msg='Building model')

    for words, next_word in zip(
            zip(*[words[i:] for i in range(states)]), words[states:]):
        model[words][next_word] += 1
        prog.increment()

    candidates = [key for key in model.keys() if key[0].istitle()]
    string = list(random.choice(candidates))
    w = len(string)
    while True:
        if w >= outputwords:
            if string[-1].endswith('.'): break
        candidates, weights = zip(*model[tuple(string[-states:])].items())
        weights = np.asarray(weights, dtype=float)
        weights /= np.sum(weights)
        next_word = np.random.choice(candidates, p=weights)
        string.append(next_word)
        w += 1

    print
    print ' '.join(string)

if __name__ == '__main__':
    from optparse import OptionParser, OptionGroup
    parser = OptionParser(usage="Usage: %prog text states outputwords [tokenizer]")
    options, args = parser.parse_args()
    options = dict(options.__dict__)
    try:
        if len(args) < 3: raise Exception()
        args[1] = int(args[1])
        args[2] = int(args[2])
    except:
        parser.print_help()
        exit()
    main(*args, **options)
