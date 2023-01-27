import re


def gerarSigla(expr:str):
    sigla = ''
    filtro = ('de', 'da', 'e')

    for termo in expr.strip().split(" "):
        if termo not in filtro:
            sigla += termo[0].upper() 
    
    print(sigla)
    return sigla


def accepts(exclude:dict=None):
    pass


def required():
    pass


def onlycharacters(elemento:str, hint:str=""):
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            if bool(re.search(r"\d", args[1])):
                raise ValueError(f"{elemento.capitalize()} não pode conter dígitos. " + hint)

            elif bool(re.compile('[@_!#$%^&*()<>?/\|}{~:]').search(args[1])):
                raise ValueError(f"{elemento.capitalize()} não pode conter caracteres especiais. " + hint)

            return func(*args, **kwargs)
        return wrapper

    return decorator