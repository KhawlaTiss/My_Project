from numpy.ma.core import nomask
class Livre :
    def __init__(self,title,auteur):
        self.title=title
        self.auteur=auteur

class Auteur :
    def __init__(self,nom):
        self.nom=nom
        



auteur1=Auteur("J.K. Rowling")
livre1= Livre("Harry Potter and the Sorcerer's Stone",auteur1)


class Biblio:
    def __init__(self):
        self.collection=[]
        
    
    def emprunter_livre(self,livre):
        if livre in self.collection :
            self.collection.remove(livre)
            return f"{livre.titre} a ete emprunte."
        else :
            return "le livre n'est pas dispo."
        


biblio1=Biblio()
res=biblio1.emprunter_livre(livre1)



print("hello world")
print(res)




