import graphene
from ..schemas.shema_team import BrigadaShema
from team.models import Brigada, BrigadaExperto
from ..queries.queries import Query


class CreateTeam(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        investigacionId = graphene.Int()
        expertosIds = graphene.List(graphene.Int)  

    def mutate(self, info, investigacionId, expertosIds):
        print(expertosIds)
        id = Query.resolve_exist_id_investigation(None, None, investigacionId)
        print(id)
        if id:

            team = Brigada.objects.create(investigacion_id=investigacionId)
            print("brigada creada: ",team)

            # exit()


            # Se crea la relación en la tabla intermedia
            for cc in expertosIds:
                print(cc)
                cc_instance = Query.resolve_extract_instance_from_expert(None, None, cc)
                print("experto creado: ",cc_instance)
                BrigadaExperto.objects.create(  
                    brigada=team,  
                    experto_cc=cc_instance.experto_cc
                )
                

            return CreateTeam(success=True)

        else:
            return "NO SE CREO"

