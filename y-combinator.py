#!/usr/bin/env python

def Y(rec):
    loop = lambda f: f(f)

    def apply_rec(loop):
        return rec(lambda x: loop(loop)(x))

    return loop(apply_rec)

def make_length():
    def recv_length_fun(fun_length):
        def length(ls):
            if len(ls) == 0:
                return 0
            else:
                return 1 + fun_length(ls[1:])
        return length
    return Y(recv_length_fun)

length_func = make_length()
print length_func([1, 2, 3, 4])
