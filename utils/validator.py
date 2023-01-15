''' 
function definitions to validate data 
'''

def accepts(exclude:dict=None):
    pass


def required():
    pass


def onlycharacters(func):

    def wrapper(arg, message=""):
        if isinstance(arg, str) and not arg.isalnum():
            print(func.__name__)
            return
            
        result = func(arg)

        return result
    return wrapper

