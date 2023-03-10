import server
from hashlib import sha256

content = {}

def create(topic, data):
    print(f"Creating topic {topic} with data {data}")
    server.create(topic, data)
    content[topic] = sha256(data.encode()).hexdigest()

def read(topic):
    print(f"Reading topic {topic}")
    if topic not in content:
        return None
    if content[topic] != sha256(server.read(topic).encode()).hexdigest():
        print("Hashes don't match")
        return None
    return server.read(topic)

def update(topic, data):
    print(f"Updating topic {topic} with data {data}")
    if topic not in content:
        return None
    server.update(topic, data)
    content[topic] = sha256(data.encode()).hexdigest()

def delete(topic):
    print(f"Deleting topic {topic}")
    if topic not in content:
        return None
    server.delete(topic)
    del content[topic]

create("foo", "bar")
print(read("foo"))
update("foo", "baz")
print(read("foo"))
delete("foo")
print(read("foo"))