def validarNombre(nombre = ""):

    if nombre.isalpha():

        if len(nombre) < 6:
            valido = False
        elif len(nombre) > 12:
            valido = False
        else:
            valido = True

    else:
        valido = False

    return valido

def generardorPassword():

    abcMinus = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    abcMayus = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    nums = ['1','2','3','4','5','6','7','8','9','0']
    simbs = ['*','+','-','_',';','¿','?','¡','!','º','ª']




