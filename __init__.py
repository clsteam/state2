# -*- coding:utf-8 -*-
import inspect
import functools


class State(object):
    @staticmethod
    def __begin__(host):
        pass

    @staticmethod
    def __end__(host):
        pass


def stateful(cls):
    defaults = []
    for i in cls.__dict__.values():
        if inspect.isclass(i) and issubclass(i, State) and hasattr(i, 'default') and i.default:
            defaults.append(i)
    if not defaults:
        raise Exception('%s\'s default state is not found.' % cls.__name__)
    if len(defaults) > 1:
        raise Exception('%s\'s has too much default state.%s' % (cls.__name__, defaults))
    default = defaults[0]

    old__init__ = cls.__init__
    if hasattr(cls, '__getattr__'):
        old__getattr__ = getattr(cls, '__getattr__')
    else:
        old__getattr__ = getattr(cls, '__getattribute__')

    def __init__(self, *args, **kwargs):
        self.__state__ = default
        self.__state__.__begin__(self)
        return old__init__(self, *args, **kwargs)

    def __getattr__(self, name):
        try:
            old__getattr__(self, name)
        except AttributeError as e:
            pass
        try:
            f = getattr(curr(self), name)
        except AttributeError as e:
            raise e
        if not callable(f):
            raise Exception("{0} must be callable.".format(name))
        return functools.partial(f, self)

    cls.__init__ = __init__
    cls.__getattr__ = __getattr__
    return cls


def curr(host):
    return host.__state__


def switch(host, new_state):
    host.__state__ = new_state


behavior = staticmethod

