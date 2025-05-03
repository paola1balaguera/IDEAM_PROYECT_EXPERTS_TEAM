import graphene
from graphene_django import DjangoObjectType
from expert.models import Experto


class ExpertoShema(DjangoObjectType):
    # cedula = graphene.Int()
    # primer_nombre = graphene.String()
    # segundo_nombre = graphene.String()
    # primer_apellido = graphene.String()
    # segundo_apellido = graphene.String()
    # fecha_nacimiento = graphene.Date()
    # clasificacion = graphene.String()

    class Meta:
        model = Experto
        fields = (
            'cedula',
            'primer_nombre',
            'primer_apellido',
            'clasificacion'
        )