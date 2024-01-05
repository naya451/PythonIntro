import sys
def safeval(expr, global_vars=None, local_vars=None):
    try:
        if (type(global_vars) == dict):
            global_vars = global_vars.copy()
        if (global_vars is None):
            global_vars = globals().copy()
        return eval(expr, global_vars, local_vars)
    except NameError:
        return expr
    except Exception:
        return sys.exc_info()[1]

