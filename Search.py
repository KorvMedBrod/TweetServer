from riak import RiakClient


client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)
results = client.fulltext_search("tweets", "*")
print results
print results['docs']