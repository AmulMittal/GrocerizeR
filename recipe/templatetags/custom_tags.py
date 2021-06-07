from django.template import Library

register = Library()

def is_in(var, args):
    return (float(var) / float(args)) * 100

register.filter(is_in)