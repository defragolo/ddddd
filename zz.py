# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:27:25 2019

@author: Idriss
"""

import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    createdAT = graphene.DateTime()


class Query(graphene.ObjectType):
    users = graphene.List(User, limit=graphene.Int())
    hello = graphene.String()#Int
    is_hjkl = graphene.Boolean()
    
    def resolve_hello(self, info):
        return "world"
        
    def resolve_is_admin(self, info):
        return True
    
    def resolve_users(self, info, limit=None):
        return[User(id="1", username = "Fred", createdAT=datetime.now()), User(id="2", username="Doug", createdAT=datetime.now())][:limit]
		
schema = graphene.Schema(query=Query, auto_camelcase=False)

result = schema.execute(
'''
{
    user{
    id
    username
    crearedAT
    }
}
'''
)

print(result.data.items())
