### situazione 1
'''
mypackage:
    main.py: some functions inside
    __init__.py: empty
'''

try:
    import MyEmptyInitPackage
    MyEmptyInitPackage.main.sum(1, 2)
except Exception as e:
    print(f'''THIS IS ILLEGAL {e}, you meant 
    import mypackage.main
    mypackage.main.sum(x, y)
    ''',)

# Questo è legale! Devo prima importare il file main, poi chiamare la funzione usando nomemodulo.nomefile.funzione()
import MyEmptyInitPackage.main
print(MyEmptyInitPackage.main.sum(1, 2))


# situazione 2
'''
mypackage:
    main.py: some functions inside
    __init__.py: from .main import functionname

    subpackage:
        main.py: some functions inside
        __init__.py: from .main import cat

Posso importare senza specificare il nome del file main, ma solo il nome del modulo
'''
# 

import MyNotEmptyInitPackage as pkg
print(pkg.sum(2, 2))
print(pkg.subpackage.cat("hello", "world"))



# situazione 3
'''
mypackage:
    main.py: some functions inside
    __init__.py: from . import main
    subpackage:
        main.py: some functions inside
        __init__.py: from . import main


simile a caso 1, devo esplicitare il nome del modulo da importare (pkg.main, oppure pkg.subpkg.main)
a differenza del caso 1, posso importare i sotto moduli o i subpkg
'''
import MyNotEmptyInitPackage2 as pkg2
print(pkg2.main.sum(1, 1))
print(pkg2.subpackage.main.cat("hello", "scem"))

# sono tutte forme legali le seguenti
import MyNotEmptyInitPackage2.main
import MyNotEmptyInitPackage2.subpackage
import MyNotEmptyInitPackage2.subpackage.main



'''
importing da un modulo nella stessa cartella
.
    app.py
    module.py: some function inside
'''
try:
    from . import module
    module.sub(1,2)
except:
    print('''Cannot use . to refer local dir, even if you have __init__.py, just write name of the file to import
    check: https://stackoverflow.com/questions/70874423/fastapi-importerror-attempted-relative-import-with-no-known-parent-package#
    ''')
import module
print(module.sub(1, 2))


