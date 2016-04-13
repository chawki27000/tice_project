from .models import *
from rest_framework import serializers
from tice_project.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')


class TimeStampedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStampedModel
        fields = ('created', 'modified')


class AdministrateurSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Administrateur
        fields = ('user', 'grade_util')


class FormateurSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Formateur
        fields = ('user', 'spec_formation', 'type_formation')


class CategorieSerializer(serializers.ModelSerializer):
    administrateur = AdministrateurSerializer()
    class Meta:
        model = Categorie
        fields = ('lib_categ', 'administrateur')


class FormationSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer()
    class Meta:
        model = Formation
        fields = ('lib_form', 'date_deb_form', 'date_fin_form', 'categorie')


class ApprenantSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    formation = FormateurSerializer()
    class Meta:
        model = Apprenant
        fields = ('user', 'grade_util', 'diplome_appr', 'formation')


class RegroupementSerializer(serializers.ModelSerializer):
    formation = FormationSerializer()
    class Meta:
        model = Regroupement()
        fields = ('date_group', 'formation')


class CoursSerialzer(serializers.ModelSerializer):
    formation = FormationSerializer()
    class Meta:
        model = Cours
        fields = ('lib_cour', 'formation')


class ChapitreSerializer(serializers.ModelSerializer):
    cours = CoursSerialzer()
    class Meta:
        model = Chapitre
        fields = ('lib_chap', 'cours')


class RessourceSerializer(serializers.ModelSerializer):
    chapitre = ChapitreSerializer()
    class Meta:
        model = Ressource
        fields = ('lib_ress', 'type_ress', 'chapitre')


class AnimerSerializer(serializers.ModelSerializer):
    id_util = FormateurSerializer()
    id_form = FormateurSerializer()
    class Meta:
        model = Animer
        fields = ('id_util', 'id_form')


class TestSerializer(serializers.ModelSerializer):
    id_util = ApprenantSerializer()
    id_form = FormationSerializer()

    class Meta:
        model = Test
        fields = ('id_util', 'id_form', 'date_test', 'note_test')
