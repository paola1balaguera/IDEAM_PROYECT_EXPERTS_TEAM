import graphene
from ..schemas.shema_team import BrigadaShema
from team.models import Brigada, BrigadaExperto
from ..queries.queries import Query

class UpdateTeam(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        investigacionId = graphene.Int(required=True)
        expertosIds    = graphene.List(graphene.Int, required=True)

    def mutate(self, info, investigacionId, expertosIds):
       
        exists = Query.resolve_exist_id_investigation(None, None, investigacionId)
        if not exists:
            return UpdateTeam(success=False)

        try:
          
            team = Brigada.objects.get(investigacion_id=investigacionId)
        except Brigada.DoesNotExist:
            return UpdateTeam(success=False)

  
        BrigadaExperto.objects.filter(brigada=team).delete()

        for cc in expertosIds:
            expert_obj = Query.resolve_extract_instance_from_expert(None, None, cc)
            if expert_obj:
                BrigadaExperto.objects.create(
                    brigada   = team,
                    experto_cc = expert_obj.experto_cc
                )

        return UpdateTeam(success=True)



