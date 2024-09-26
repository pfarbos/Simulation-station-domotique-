def ordreChrono(tab):#la fonction permettant de trier notre database par odre chronologique
    ordreChronoTab= []#ce tableau servira à la fin à stocker les données filtrées
    sommeTab = []#ce tableau sert à stocker la somme a+m+j+h+m+s de chaque capteur
    for i in range(0, len(tab), 5):#on se déplace dans notre tableau database (de capteur en capteur)
        somme = tab[i][0]*60*60*24*365 + tab[i][1]*30*24*60*60 + tab[i][2]*24*60*60 + tab[i+1][0]*60*60 + tab[i+1][1]*60 + tab[i+1][2]#pour chaque capteur, on calcule la somme a+m+j+h+m+s (convertie en secondes)
        sommeTab.append(somme)#on stocke la valeur dans le tableau prévu plus haut
    sommeTab = trierliste(sommeTab)#quand on a calculé les sommes a+m+j+h+m+s de chaque capteur et que  celles-ci sont stockées dans le tableau sommeTab,on utilise la fonction trierliste pour obtenir le même tableau mais cette fois-ci , avec les valeurs dans l'ordre croissant
    for j in sommeTab:#pour chaque élément du tableau sommeTab
        for i in range(0, len(tab), 5): #pour chaque capteur
            if j == tab[i][0]*60*60*24*365 + tab[i][1]*30*24*60*60 + tab[i][2]*24*60*60 + tab[i+1][0]*60*60 + tab[i+1][1]*60 + tab[i+1][2]:#on regarde si les résultats a+m+j+h+m+s correspondent 
                ordreChronoTab.append(tab[i:i+5])#si c'est le cas, la ligne du capteur est stockée dans un nouveau tableau (ordreChronoTab)
    if sexyDataOn==True:#Si dans la console, on a activé l'habillage sexy,
        soSexy(ordreChronoTab,1)#le tableau sera renvoyé sous une forme plus lisible pour l'Homme
    else:#sinon
        print(ordreChronoTab)#on affiche les données brutes (difficiles à lire)


    
def trierliste(tab):#fonction pour trier dans l'ordre croissant les valeurs numériques d'un tableau
    r = []#tableau vide
    for i in range(len(tab)):#boucle qui s'effectue len(tab) fois
        max = min(tab)#on cherche la valeur minimum (la plus faible) parmi tout le tableau
        tab.remove(max)#on la supprime du tableau
        r.append(max)#on la remet (cela a pour effet d'avoir les valeurs les plus faibles en premier dans le tableau (ordre croissant) )
    return r#on return r sinon, celui-ci serait vide


def filtrageDate(tab):#fonction pour filtrer le tableau database en donnant des dates d'"intervalle"
    TabFiltrageParDate = []#ce tableau servira à la fin à stocker les données filtrées
    datestart=int(input("année de départ :"))#on demande à l'utilisateur d'entrer dans la console une année de départ
    heurestart=int(input("heure de départ :"))#on demande à l'utilisateur d'entrer dans la console une heure de départ
    dateend =int(input("année de fin :"))#on demande à l'utilisateur d'entrer dans la console une année de fin
    heureend =int(input("heure de fin :"))#on demande à l'utilisateur d'entrer dans la console une heure de départ
    for i in range(0,len(tab),5):#on se déplace dans notre tableau database (de capteur en capteur)
        if tab[i][0] >= datestart and tab[i][0] <= dateend and tab[i+1][0] >= heurestart and tab[i+1][0] <= heureend:#si les données du capteur sont comprises dans l'intervalle année et heure qu'il a entré plus tôt 
            TabFiltrageParDate.append(tab[i:i + 5])#on stocke la ligne du capteur dans le tableau TabFiltrageParDate
    if sexyDataOn==True:#Si dans la console, on a activé l'habillage sexy,
        soSexy(TabFiltrageParDate,1)#le tableau sera renvoyé sous une forme plus lisible pour l'Homme
    else:#sinon
        print(TabFiltrageParDate)#on affiche les données brutes (difficiles à lire)


def filtrageTypeCapteur(tab,type):#cette fonction va filtrer le tableau database pour ne garder les types de capteurs que l'on souhaite
    TabFiltrageTypeCapteur = []#ce tableau servira à la fin à stocker les données filtrées
    for i in range(4, len(tab), 5):#on va regarder chaque ligne du tableau database sur l'index correspondant au Type du capteur (index 4) et ça, pour chaque capteur
        if tab[i] == type:#si le capteur a pour type l'élément que l'on recherche,
            TabFiltrageTypeCapteur.append(tab[i-4:i+1])#la ligne du capteur est stockée dans un nouveau tableau appelé TabFiltrageTypeCapteur
    if sexyDataOn==True:#Si dans la console, on a activé l'habillage sexy,
        soSexy(TabFiltrageTypeCapteur,1)#on affiche le tableau TabFiltrageTypeCapteur en mode sexy.
    else:#sinon
        print(TabFiltrageTypeCapteur)#on affiche les données brutes (difficiles à lire)



def filtrageParID(tab,ID):#cette fonction va filtrer le tableau database pour ne garder que les capteurs avec l'ID que l'on souhaite
    TabFiltrageParID = []#ce tableau servira à la fin à stocker les données filtrées
    for i in range(2, len(tab), 5):#pour chaque ligne de données de capteur dans la database, on se place à chaque fois sur la l'index contenant l'ID (2) et
        if tab[i] == ID:#on regarde si l'ID contenu sur l'index est égal à l'ID que l'on recherche et si c'est le cas,
            TabFiltrageParID.append(tab[i-2:i + 3])#on prend les données de ce capteur pour les stockées dans le tableau TabFiltrageParID
    if sexyDataOn==True:#Si dans la console, on a activé l'habillage sexy,
        soSexy(TabFiltrageParID,1)#on affiche le tableau du filtrage ID de manière sexy
    else:#sinon
        print(TabFiltrageParID)#on affiche les données brutes (difficiles à lire)




def soSexy(tab,longueurBloc):#cette fonction sert à donner un habillage des données plus lisible pour l'Homme
    for i in range(0, len(tab), longueurBloc):#on tronçonne notre tableau database en différentes lignes avec une longueur d'index de longueurBloc
        print(tab[i:i + longueurBloc])#on affiche les données contenues de l'intervalle i à i + la longueur du bloc (cela reviens à afficher la ligne de données entière d'un capteur(et ça , pour chaque capteur dans le tab)



def ajouterDonnee(tab,date,heure,ID,valeur,type):#cette fonction envoie les données récupérées par les capteurs à la database
    tab.append(date)
    tab.append(heure)
    tab.append(ID)
    tab.append(valeur)
    tab.append(type)

def simulationCapteur(tab):#cette fonction simule des données enregistrées par des capteurs et utilise la fonction ajouterDonnee pour renvoyer ces données à la database
    ajouterDonnee(tab,(2020,12,4),(15,40,10),'Bureau',25,'Température')#données du capteur 1
    ajouterDonnee(tab,(2017,3,23),(12,42,1),'Amphi',12,'Température')#données du capteur 2
    ajouterDonnee(tab, (2020, 9, 4), (15, 40, 10), 'Salle TP PC', '24', 'Température')#données du capteur 3
    ajouterDonnee(tab, (2019, 4, 7), (23, 12, 4), 'Bureau', 15, "Taux d'humidité")  # données du capteur 4
    ajouterDonnee(tab, (2003, 1, 19), (11, 32, 0), 'Bureau',56, "Taux de luminonité")  # données du capteur 5
    ajouterDonnee(tab,(2020,4,12),(9,22,45),'Amphi',2,"Taux d'humidité")#données du capteur 6
    ajouterDonnee(tab, (2017, 4, 9), (23, 12, 14), 'Bureau', 12, 'Température')  # données du capteur 7


def affichage():
    global database
    database = []#le tableau qui va stocker toutes les données des capteurs
    print("############Données brutes############")####graphique
    simulationCapteur(database)#utilisation de la fonction simulationCapteur. Elle récupère les données des capteurs et les envoies à la database
    print(database)#on affiche les informations brutes stockées dans le tableau database
    print("__________________________________________________________________")####graphique


def menu():#on définit notre fonction menu qui nous servira a utiliser toutes les fonctions énoncées plus haut
  global sexyDataOn####graphique(pour faire un "switch" pour l'habillage sexy des données)
  sexyDataOn=False#par défaut, les données ne sont pas sous la forme "sexy"
  fin = False#pour une boucle. Quand on lance le script, le menu se répète en boucle tant que la condition est respectée
  print("Hello world !")#test start
  affichage()#####surtout graphique + affichage des données brutes de départ
  while(not fin):#le menu se répète en boucle tant que la condition est respectée
    print("1 : Trier par ID")####graphique
    print("2 : Trier par Type")####graphique
    print("3 : Trier par intervalle de temps donné:")####graphique
    print("4 : Trier par ordre chronologique:")####graphique
    if sexyDataOn==False:###Esthétique (pour le "switch" de l'habillage sexy)
        print("50 : Activer l'habillage sexy des données<3")####graphique
    else:#sinon
        print("50 : Désactiver l'habillage sexy des données<3")####graphique
    print("99 : Quitter")####graphique
    choix = int(input("Entrez votre choix: "))    # l'utilisateur est invité à saisir son choix
    # en fonction du choix de l'utilisateur on déclenche telle ou telle partie du code
    if choix == 1:# si choix 1, lance la fonction filtrage par ID
      print ("Vous avez choisi la première option")####graphique
      print("##################Tri par ID##################")####graphique
      filtrageParID(database, input("ID :")) # filtrage par ID
      print("__________________________________________________________________")####graphique
    elif choix == 2:# si choix 2, lance la fonction filtrage par Type
      print("Vous avez choisi la deuxième option")####graphique
      print("##################Tri par Type##################")####graphique
      filtrageTypeCapteur(database,input("Type :"))# filtrage par Type
      print("__________________________________________________________________")####graphique
    elif choix == 50 and sexyDataOn==False :####graphique +pour le switch
      print("Vous avez choisi la cinquantième option")####graphique
      print("")####graphique
      print("*****Habillage sexy activé*****")####graphique
      print("")####graphique
      sexyDataOn=True #on active l'habillage sexy (switch activé)
    elif choix == 50 and sexyDataOn==True :####graphique +pour le switch
      print("Vous avez choisi la cinquantième option")####graphique
      print("")####graphique
      print("*****Habillage sexy désactivé*****")####graphique
      print("")####graphique
      sexyDataOn=False#on désactive l'habillage sexy (switch désactivé)
    elif choix == 3:# si choix 3, lance la fonction filtrage par intervalle de temps donné
        print("Vous avez choisi la troisième option")####graphique
        print("##################Tri par intervalle de temps donné##################")####graphique
        filtrageDate(database) # filtrage par intervalle de temps donné
        print("__________________________________________________________________")####graphique
    elif choix == 4:# si choix 4, lance la fonction de tri par ordre chronologique
        print("Vous avez choisi la quatrième option")####graphique
        print("##################Tri par ordre chronologique##################")
        ordreChrono(database)# tri par ordre chronologique
        print("__________________________________________________________________")####graphique
    elif choix == 99:#si choix 99,fin de la boucle du menu 
        print("Goodbye world !")#test end
        fin = True#programme fini
    else:#si le choix ne fait pas parmi des différentes possibilitées ci-dessus, 
      print("Choix invalide")####graphique
      #le menu continu 
      
menu()#on lance la fonction menu(on appuie sur le boutton ON)





