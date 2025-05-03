import graphene
from ..schemas.schema_experto import ExpertoShema
from ..schemas.shema_team import BrigadaShema
from ..schemas.schema_expert_team import ExpertTeamShema
from expert.models import Experto
from team.models import Brigada, BrigadaExperto
from django.db import connections



class Query(graphene.ObjectType):


    # -----------------------------------------

    all_expertos = graphene.List(ExpertoShema)
    all_team = graphene.List(BrigadaShema)
    last_id_team = graphene.Int()
    experts_by_id_team = graphene.List(ExpertTeamShema, brigada_id=graphene.Int(required=True))
    exist_id_investigation = graphene.Int()
    extract_instance_from_expert = graphene.Field(ExpertoShema, cc=graphene.Int(required=True))

    


    def resolve_all_expertos(root, info):

        return Experto.objects.using('secondary').all()
    
    def resolve_last_id_team(root, info):

        last_brigada = Brigada.objects.latest('brigada_id')
        return last_brigada.brigada_id
    
    def resolve_all_team(root, info):

        return Brigada.objects.all()
    
    def resolve_experts_by_id_team(root, info, brigada_id):

        print("siuu")

        brigadas = BrigadaExperto.objects.filter(brigada_id=brigada_id)

        print(brigadas)

        return brigadas
    
    def resolve_exist_id_investigation(root, info, id):
        with connections['auxiliary'].cursor() as cursor:
            cursor.execute("SELECT 1 FROM investigacion WHERE investigacion_id = %s LIMIT 1", [id])
            return cursor.fetchone() is not None

    def resolve_extract_instance_from_expert(self, info, cc):
        print(cc)
        experto = Experto.objects.using('secondary').filter(experto_cc=cc).first()
        print(experto)
        return experto