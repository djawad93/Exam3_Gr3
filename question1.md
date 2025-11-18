créer une fonction qui qui genere la signature

fonction generer signature(message)

signature =""

chiffre= ['1','2','3','4','5','6','7','8','9']
cle_gr3=[
['a','b','c','d','e','f','g','h','i'],['j','k','l','m','n','o','p','q','r'],['j','k','l','m','n','o','p','q','r'],
]



mettre les groupes de lettres:

gr1=['a','b','c','d','e','f','g','h','i']
gr2=['j','k','l','m','n','o','p','q','r']
gr3=['j','k','l','m','n','o','p','q','r']


pour chaque caratere dans le message:


        si lettre est dans le groupe1:
            index= position de lettredans groupe1
            signature=signature + chiffre[index]

         sinon si lettre est dans le groupe2:
            index= position de lettredans groupe2
            signature=signature + chiffre[index]

         sinon si lettre est dans le groupe3:
                    index= position de lettre dans groupe3
                    signature=signature + chiffre[index]


signature= signature + lettre
retourner signature