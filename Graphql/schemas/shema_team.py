import graphene
from graphene_django import DjangoObjectType
from team.models import Brigada


class BrigadaShema(DjangoObjectType):


    class Meta:
        model = Brigada
