import cython

cdef class hello:
    print('\033[95m'"hello there, cython import works"'\033[0m')