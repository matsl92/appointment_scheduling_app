from faunadb import query as q  
from faunadb.objects import Ref   
from faunadb.client import FaunaClient  

client = FaunaClient(secret="fnAE0FVUgRACULoXNJ7d58wf3HuH9E0KROfhQbs2")  

indexes = client.query(q.paginate(q.indexes()))  

print(indexes)