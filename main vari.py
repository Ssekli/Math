#fonctions avec nb de paramètres variable

def plus(title, **args) : #la 2e étoile sert à donner une clé a chaque valeur.
    print ("TITLE :", title)
    result = 0
    for n in args.values() :  #.values() sert à aller chercher les valeurs des paramètres si que somme de nombre enlever .values()
        result += n
    return result

print(plus("somme", math=4, anglais=9, geo=3)) #pas de maj pour les clés