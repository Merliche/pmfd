# Notre Projet
### participants:
Alexandre Merle, Martin Bravais, Yohann pouillieute






__*Réflexion sur la manière d'aborder le projet*__


  Nous nous sommes concerté sur les différentes tâches à accomplir lors de cette mise en place de ce projet de distributeur de billets . Nous avons réunis toutes les fonctions que proposait un distributeur normal et nous avons ciblé les fonctions essentielles afin d'avoir un programmme facile d'utilisation pour le client.
  
  >Les différentes fonctions que propose un distributeur de billet :
  
   ![lien utile](https://miro.medium.com/max/640/1*UGCg3silYxpMXjhAe4Jpow.jpeg)
  
  _________________________________
  
__*L'interface graphique*__
  
  Nous nous sommes penché avec Alexandre sur la mise en page grâce à l'outil Tkinter. Nous nous sommes donc documenté sur ce langage en apprenant à insérer une image, créer une fenêtre, ajouter des boutons. Après nous être renseignés sur l'outil en lui même, nous avons attaqué le projet en lui même. 
Nous avons pris la carte de Boulogne et avons situé 4 banques afin de permettre à l'utilisateur de choisir la banque qu'il préfère. Ensuite nous avons placé des flèches pour lier ces points sur la carte à l'image de la banque qui lui corespondait en créant un bouton afin de pouvoir faire son choix. Lorsque l'utilisateur aura validé son choix, la page se détruira et une nouvelle s'ouvrira avec le distributeur pour pouvoir proposer à l'utilisateur toutes les fonctions dont la banque dispose.

_________________________________

__*Le code du distributeur*__

  Ensuite Yohann a pris le relais.
L'utilisateur devra se connecter au distributeur en rentrant les 16 chiffres de sa carte bancaire pour pouvoir utiliser ce dernier a travers les fonctions suivantes:
        * Faire un retrait
        * Regarder l'historique des transactions
        * Consulter son solde
Yohann a utilisé la librairie SQL3 afin de pouvoir créer les tableaux de données correspondant aux comptes des utlisateurs, avec leur solde et leur historique.
Lors de la fonction retrait, il appelle donc ce tableau en créant une nouvelle page tout en détruisant l'ancienne. Sur cette page, l'utilisateur pourra effectuer son retrait, si bien evidemment il n'est pas dans le rouge, en choisisant le montant. Cette action soustraira donc le montant du retrait au solde initial de l'utilisateur dans la base de donnée.

_________________________________


__*Difficultés recnontrées*__

  Fonction dépôt  
  Image du distributeur sur la deuxième fenêtre
  Fonction retrait 
  
