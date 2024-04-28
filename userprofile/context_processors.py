from .saved import Saved

def saved(request):
    return { 'saved': Saved(request)}