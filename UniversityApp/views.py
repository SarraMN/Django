from django.db.models.fields.related import ManyToManyField
from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from UniversityApp.models import enregistrement, enseignant, etudiant, groupe, module, absence, outil, piece_attache_enonce, piece_attache_rendu,seance,evaluation, travail_a_rendre
from UniversityApp.serializer import AbsenceSerializer, EnregistrementSerializer, EnseignantSerializer, EtudiantSerializer, EvaluationSerializer, GroupeSerializer, ModuleSerializer, OutilSerializer, Piece_attache_enonceSerializer, Piece_attache_renduSerializer, SeanceSerializer, Travail_a_rendreSerializer
from rest_framework.viewsets import ModelViewSet


class GroupeModelViewSet(ModelViewSet):
    serializer_class = GroupeSerializer
    queryset = groupe.objects.all()
    
class ModuleModelViewSet(ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = module.objects.all()
    
class EnseignantModelViewSet(ModelViewSet):
    serializer_class = EnseignantSerializer
    queryset = enseignant.objects.all()
    
class EnregistrementModelViewSet(ModelViewSet):
    serializer_class = EnregistrementSerializer
    queryset = enregistrement.objects.all()
    
class OutilModelViewSet(ModelViewSet):
    serializer_class = OutilSerializer
    queryset = outil.objects.all()



class Travail_a_rendreModelViewSet(ModelViewSet):
    serializer_class = Travail_a_rendreSerializer
    queryset = travail_a_rendre.objects.all()

class Piece_attache_renduModelViewSet(ModelViewSet):
    serializer_class = Piece_attache_renduSerializer
    queryset = piece_attache_rendu.objects.all()

class SeanceModelViewSet(ModelViewSet):
    serializer_class = SeanceSerializer
    queryset = seance.objects.all()

class Piece_attache_enonceModelViewSet(ModelViewSet):
    serializer_class = Piece_attache_enonceSerializer
    queryset = piece_attache_enonce.objects.all()

################ path : Etudiant ############################
class EtudiantModelViewSet(ModelViewSet):
    serializer_class = EtudiantSerializer
    queryset = etudiant.objects.all()

################ path : Absence ############################

class AbsenceModelViewSet(ModelViewSet):
    serializer_class = AbsenceSerializer
    queryset = absence.objects.all()

class EvaluationModelViewSet(ModelViewSet):
    serializer_class = EvaluationSerializer
    queryset = evaluation.objects.all()