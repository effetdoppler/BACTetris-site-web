import os, cherrypy


class Glob(object):
    "Données à caractère global pour l'application"
    patronsHTML ="spectacles.htm" # Fichier contenant les "patrons" HTML
    html ={} # Les patrons seront chargés dans ce dictionnaire

def chargerPatronsHTML():
    # Chargement de tous les "patrons" de pages HTML dans un dictionnaire :
    fi =open(Glob.patronsHTML,"r")
    try: # pour s'assurer que le fichier sera toujours refermé
        for ligne in fi:
            if ligne[:2] =="[*": # étiquette trouvée ==>
                label =ligne[2:] # suppression [*
                label =label[:-1].strip() # suppression LF et esp évent.
                label =label[:-2] # suppression *]
                txt =""
            else:
                if ligne[:5] =="#####":
                    Glob.html[label] = txt
                else:
                    txt += ligne
    finally:
        fi.close() # fichier refermé dans tous les cas

def mep(page):
    # Fonction de "mise en page" du code HTML généré : renvoie la <page>
    # transmise, agrémentée d'un en-tête et d'un bas de page adéquats.
    return Glob.html["miseEnPage"].format(page)
