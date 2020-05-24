"""
# Python GQL: A GraphQL client in Python.
# https://github.com/graphql-python/gql
"""
print(__doc__)

from gql import gql, Client

client = Client(schema=SampleSchema)

query = gql("""
        {
            hello
        }

    """)


client.execute(query)
