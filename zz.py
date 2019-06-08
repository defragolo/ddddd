import graphene
import json
from datetime import datetime 

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    createdAt = graphene.DateTime()




class Query(graphene.ObjectType):
    hello = graphene.Int()
    users= graphene.List(User, limit=graphene.Int()) 
    is_admin = graphene.Boolean()
    def resolve_is_admin(self, info):
        return True
    def resolve_hello(drlf, info):
        return 2
    def resolve_users(self, info, limit=None):
        return[
            User(id="1",username="Fred",
                    createdAt=datetime.now()),
            User(id="2", username="Fred",
                    createdAt=datetime.now())
            ][:limit]
schema = graphene.Schema(query=Query, auto_camelcase=False)
result = schema.execute(
'''
{
    users{
    id
    username
    createdAt
    }
}
'''

)

print(result.data.items())