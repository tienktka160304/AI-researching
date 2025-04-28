def foo(name,/, **kwds):
    return 'name' in kwds

foo(1, **{'name':2})