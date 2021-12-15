from django.db import models
from datetime import datetime, timezone
from django.db.models.fields import  DateTimeField
from django.db.models.fields.related import ManyToManyField    
from django.utils import timezone


   
class outils(models.TextChoices):
    materiel=('M','materiel')
    logiciel=('L','logiciel')
     
# class etat_etudiant(models.TextChoices):
#     present=('P','Present')
#     absent=('A','Absent')
#     exclu=('E','Exclu')
#     Retard=('R','Retard')
 
class situation(models.TextChoices):
    Redoublant=('R','Redoublant')
    nouveau=('N','nouveau')
    derogataire=('D','derogataire')
    autre=('autre','autre')
      
class etat_travail_a_rendre(models.TextChoices):
    en_cours=('EN_COURS','en cours')
    terminee=('TERMINEE','terminée')
    annulee=('ANNULEE','annulée')
    differee=('DIFFEREE','differée')
    
class groupe(models.Model):
    nom=models.CharField(name='nom_du_groupe',max_length=25,blank=False)
    nbr_etudiants=models.IntegerField()
    email=models.CharField(blank=False,unique=True,max_length=25)
    niveau=models.CharField(name='niveau',max_length=25,blank=False,default="1ere")  
     
class module(models.Model):
    nom=models.CharField(name='nom',blank=False,max_length=25)
    du=models.IntegerField(blank=False)
    type=models.CharField(name='Type du module',max_length=25,blank=False)
    niveau=models.CharField(name='niveau du module',max_length=25,blank=False)
    groupe= models.ManyToManyField(groupe)   
                
class enseignant(models.Model):
    nom=models.CharField(name='nom',blank=False,max_length=20)
    prenom=models.CharField(name='prenom',blank=False,max_length=20)
    du=models.IntegerField(blank=False)
    email_personnel=models.EmailField(blank=False,unique=True,name='Email personnel')
    email_du_travail=models.EmailField(blank=False,unique=True,name='Email du travail')
    photo = models.ImageField(name='photo enseignant',upload_to='photos/enseignants')
    module= models.ManyToManyField(module)
    responsable =models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    #id_respo=BigAutoField(name='ID Responsable',blank=True)

  
class etudiant(models.Model):
    nom=models.CharField(max_length=50,null=False, blank=False)
    prenom=models.CharField(max_length=50, null=False, blank=False)
    date=models.DateField(default=timezone.now, null=False, blank=False)
    photo=models.ImageField(upload_to='photos/etudiants') 
    email=models.CharField(max_length=50,null=False, blank=False)
    situatin=models.CharField(max_length=50,
                                          choices=situation.choices,
                                          default=situation.nouveau)
    idgroupe=models.ForeignKey(groupe, on_delete=models.CASCADE)
    enseignant=ManyToManyField(enseignant)

class evaluation(models.Model):
    note=models.CharField(max_length=500)
    commentaire=models.CharField(max_length=500,null=True,blank=True)
    # def __str__(self):
    #     return self.note
    
class travail_a_rendre(models.Model):
    titre=models.CharField(name='titre',max_length=100)
    date_lancement=models.DateField(default=timezone.now())
    date_limite_retour=models.DateField()
    nature=models.CharField(name='nature',max_length=100)
    descriptif=models.CharField(name='descriptif',max_length=100)
    etat=models.CharField(max_length=10,choices=etat_travail_a_rendre.choices,default=etat_travail_a_rendre.en_cours)
    etudiants=ManyToManyField(etudiant)
    module=models.ForeignKey(module,on_delete=models.CASCADE)
    evaluation=models.ForeignKey(evaluation,on_delete=models.CASCADE)
  

class outil(models.Model):
    type=models.CharField(max_length=50,choices=outils.choices,default=outils.materiel)
       

class seance(models.Model):
    heure_de_debut=DateTimeField(blank=False,default=datetime.now())
    heure_de_fin=DateTimeField(blank=False,default=datetime.now())
    num_salle=models.IntegerField(blank=True)
    objectif=models.CharField(name='Objectif',blank=False,max_length=1000)
    resume=models.CharField(name='Resume',blank=False,max_length=1000)
    outils =models.ManyToManyField(outil)
    ETAT = [
        ('C','En_cours'),
        ('T','Terminee'),
        ('A','Anulee'),
        ('D','Differee'),
    ]
    TYPE = [
        ('N','Normale'),
        ('R','Rattrapage'),
        ('S','Soutien'),
        ('F','Formation'),
    ]
    etat = models.CharField(
        max_length=8,
        choices=ETAT,
        blank=True,
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE,
        blank=False,
    )
    module=models.ForeignKey(module,on_delete=models.CASCADE,null=True)
       
              
class piece_attache_rendu(models.Model):
    date=models.DateField(null=True,blank=True)
    url=models.CharField(blank=False,unique=True,max_length=1000)
    titre=models.CharField(blank=False,max_length=100)
    travail_a_rendre =models.ForeignKey(travail_a_rendre,on_delete=models.CASCADE)
    
class piece_attache_enonce(models.Model):
    date=models.DateField(null=True,blank=True)
    url=models.CharField(blank=False,unique=True,max_length=1000)
    titre=models.CharField(blank=False,max_length=100)
    travail_a_rendre=models.ManyToManyField(travail_a_rendre)
   

class enregistrement(models.Model):
    nom=models.CharField(max_length=50,null=False, blank=False, unique=True)
    url=models.CharField(max_length=50, null=True, blank=True)
    contenu=models.CharField(max_length=50, null=False, blank=False)
    description=models.CharField(max_length=50)
    date=models.DateField(default=timezone.now,null=False, blank=False)
    idseance=models.ForeignKey(seance, on_delete=models.CASCADE)
      
  
class absence(models.Model):
    date=models.DateField(default=timezone.now)
    motif=models.CharField(name='motif',max_length=100)
    justification=models.CharField(name='justification',max_length=100)
    etudiant=models.ForeignKey(etudiant,on_delete=models.CASCADE)
    seance=models.ForeignKey(seance,on_delete=models.CASCADE)


        
        

               


