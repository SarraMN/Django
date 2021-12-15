from rest_framework import routers
from django.urls import include, path
from .views import AbsenceModelViewSet, EnregistrementModelViewSet, EnseignantModelViewSet, EtudiantModelViewSet, EvaluationModelViewSet, GroupeModelViewSet, ModuleModelViewSet, OutilModelViewSet, Piece_attache_enonceModelViewSet, Piece_attache_renduModelViewSet, SeanceModelViewSet, Travail_a_rendreModelViewSet
# addEnregistrement, addEnseignant, addEvaluation, addGroupe, addModule, addOutil, deleteEnregistrement, deleteEnseignant, deleteEvaluation, deleteGroupe, deleteModule, deleteOutil, getAllEnregistrement, getAllEnseignants, getAllEvaluation, getAllGroupe, getAllModules, getAllOutil, getEnregistrementByPk, getEnseignantByPk, getEvaluationByPk, getGroupeByPk, getModuleByPk, getOutilByPk, updateEnregistrement, updateEnseignant, updateEvaluation, updateGroupe, updateModule, updateOutil


router=routers.DefaultRouter()
router.register(r'groupe',GroupeModelViewSet)
router.register(r'module',ModuleModelViewSet)
router.register(r'enseignant',EnseignantModelViewSet)
router.register(r'enregistrement',EnregistrementModelViewSet)
router.register(r'outil',OutilModelViewSet)
router.register(r'travail_a_rendre',Travail_a_rendreModelViewSet)
router.register(r'piece_attache_rendu',Piece_attache_renduModelViewSet)
router.register(r'seance',SeanceModelViewSet)
#################### path : Piece_attache_enonce ############################
router.register(r'piece_attache_enonce',Piece_attache_enonceModelViewSet)
################ path : Etudiant ############################
router.register(r'etudiant',EtudiantModelViewSet)
################ path : Absence ############################
router.register(r'absence',AbsenceModelViewSet)
################ path : Evaluation  ############################
router.register(r'evaluation',EvaluationModelViewSet)
urlpatterns = [
    path('',include(router.urls)),

    # path(r'outil/all/',getAllOutil,name='alloutil'),
    # path(r'outil/bypk/<int:pk>',getOutilByPk,name='outilbypk'),
    # path(r'outil/add/',addoutil,name="addoutil"),
    # path(r'outil/delete/<int:pk>',deleteoutil,name="deleteoutil"),
    # path(r'outil/update/<int:pk>',updateOutil,name="updateOutil"),
]