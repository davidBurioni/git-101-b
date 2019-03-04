SUFFIXES = ['Kb','MB','GB','TB','PB','EB','YB']


def approssimate_size(size):
    if size <0:
        raise ValueError('number must be non-negative')
        
    multiple = 1024
    for suffix in SUFFIXES:
        size /=SUFFIXES[multiple]:
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('number too large')
