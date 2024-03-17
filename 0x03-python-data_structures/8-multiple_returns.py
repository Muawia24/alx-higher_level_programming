#!/usr/bin/python3
def multiple_returns(sentence):

    info = ()
    info += (len(sentence), )
    if not sentence:
        info += (None, )
        return info
    info += (sentence[0], )
    return info
