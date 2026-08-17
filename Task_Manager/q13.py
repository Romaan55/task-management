def build_tree(records):
    nodes = {} #store all nodes
    for record in records: #create node
        nodes[record["id"]] = {
            "id": record["id"],
            "name": record["name"],
            "children": []
        }

    tree = [] #store root nodes
    for record in records:# Connect child with parent

        if record["parentId"] is None:
            tree.append(nodes[record["id"]])#root node

        else:
            parent = nodes[record["parentId"]] #add node to its parent
            parent["children"].append(nodes[record["id"]])

    return tree

records = [
    {"id": 1, "parentId": None, "name": "A"},
    {"id": 2, "parentId": 1, "name": "B"},
    {"id": 3, "parentId": 1, "name": "C"},
    {"id": 4, "parentId": 2, "name": "D"}
]

print(build_tree(records))