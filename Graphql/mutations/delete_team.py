import graphene
from ..schemas.shema_team import BrigadaShema
from team.models import Brigada, BrigadaExperto
from ..queries.queries import Query

class DeleteTeam(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        investigacionId = graphene.Int(required=True)

    def mutate(self, info, investigacionId):
        
        exists = Query.resolve_exist_id_investigation(None, None, investigacionId)
        if not exists:
            return DeleteTeam(success=False)

        try:
           
            team = Brigada.objects.get(investigacion_id=investigacionId)
            team.delete()
            return DeleteTeam(success=True)
        except Brigada.DoesNotExist:
            return DeleteTeam(success=False)


