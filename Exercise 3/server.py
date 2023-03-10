stored_content = {}
def create (name, content):
    stored_content[name] = content

def read(name):
    return stored_content[name]

def update(name, content):
    stored_content[name] = content

def delete (name):
    del stored_content[name]