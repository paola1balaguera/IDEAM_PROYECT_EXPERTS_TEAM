import graphene
from graphene_django import DjangoObjectType
from team.models import BrigadaExperto


class ExpertTeamShema(DjangoObjectType):


    class Meta:
        model = BrigadaExperto
