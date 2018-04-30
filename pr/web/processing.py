import re


def preprocess(text):
    text = text.lower()
    text = re.sub(r'(?<=\w)["’᾿΄´‘°](?=[яєїю])', '\'', text)
    chars_to_remove = '!"#$€%&()*+‚,./:;<=>?@[\\]¬^_`{|}±¶•§®™~«…»\n\t“„”№0123456789'
    text = text.translate(str.maketrans(chars_to_remove, ' ' * len(chars_to_remove)))
    apostrophes = '’᾿΄´‘°'
    text = text.translate(str.maketrans(apostrophes, '\'' * len(apostrophes)))
    dashes = '‐-‒–—―'
    text = text.translate(str.maketrans(dashes, '-' * len(dashes)))
    return ' '.join(text.split())
