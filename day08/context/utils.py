from flask import g


def log_a():
    print('log_a %s ' % g.username)


def log_b():
    print('log_a %s ' % g.username)


def log_c():
    print('log_a %s ' % g.username)
