import graphene
from .create_team import CreateTeam
from .update_team import UpdateTeam
from .delete_team import DeleteTeam



class Mutation(graphene.ObjectType):

   create_team = CreateTeam.Field()
   update_team = UpdateTeam.Field()
   delete_team = DeleteTeam.Field()
