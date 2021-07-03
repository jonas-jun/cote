import time

def check(func, *case):
    '''
    func: function to check
    case: all parameters to input. not list but each
    '''
    start = time.time()
    ans = func(*case)
    duration = time.time() - start
    return round(duration, 6), ans

# for insert mode