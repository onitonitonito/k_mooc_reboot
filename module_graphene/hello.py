"""
# Code | GraphQL
# https://graphql-kr.github.io/code/#python
"""
print(__doc__)


import graphene

class Query(graphene.ObjectType):
  hello = graphene.String()

  def resolve_hello(self, args, context, info):
    return 'Hello world!'



if __name__ == '__main__':
    schema = graphene.Schema(query=Query)
    result = schema.execute('{ hello }')
    print(result.data['hello'])
