from rest_framework import serializers
from UniversityApp.models import absence, enregistrement, enseignant, etudiant, evaluation, groupe, module, outil, piece_attache_enonce, piece_attache_rendu, seance, travail_a_rendre


class GroupeSerializer(serializers.ModelSerializer):
    class Meta :
        model = groupe
        fields="__all__"
       
class ModuleSerializer(serializers.ModelSerializer):
    groupe = GroupeSerializer(read_only=True, many=True)
    class Meta :
        model = module
        fields="__all__"
           
class EnseignantSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(read_only=True, many=True)
    class Meta :
        model = enseignant
        fields="__all__"

class EtudiantSerializer(serializers.ModelSerializer):
    enseignant = EnseignantSerializer(read_only=True, many=True)
    class Meta :
        model = etudiant
        fields="__all__"
        
class AbsenceSerializer(serializers.ModelSerializer): 
    class Meta :
        model = absence
        fields="__all__"
        
class Piece_attache_renduSerializer(serializers.ModelSerializer):
     class Meta :
        model = piece_attache_rendu
        fields="__all__"

class Travail_a_rendreSerializer(serializers.ModelSerializer):
    etudiant= EtudiantSerializer(read_only=True, many=True)
    class Meta :
        model = travail_a_rendre
        fields="__all__"
        
class Piece_attache_enonceSerializer(serializers.ModelSerializer):
    travail_a_rendre=  Travail_a_rendreSerializer(read_only=True, many=True)
    class Meta :
        model = piece_attache_enonce
        fields="__all__"
        
class OutilSerializer(serializers.ModelSerializer):
    class Meta :
        model = outil
        fields="__all__"

class SeanceSerializer(serializers.ModelSerializer):
    outil= OutilSerializer(read_only=True, many=True)
    class Meta :
        model = seance
        fields="__all__"
            
class EnregistrementSerializer(serializers.ModelSerializer):
    class Meta :
        model = enregistrement
        fields="__all__"
        
class EvaluationSerializer(serializers.ModelSerializer):
    class Meta :
        model = evaluation
        fields="__all__"

