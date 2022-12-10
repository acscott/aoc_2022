from anytree import Node, PreOrderIter, Resolver, RenderTree
from anytree.search import findall

with open("input.txt", "r") as f:
    terminal = f.read().splitlines()


def get_listing(node_, listing_):
    for objects in listing_:
        if objects[0:4] == "dir ":
            node_ = Node(objects)
            node_.parent = parent
        else:
            size, name = objects.split(" ")
            node_ = Node(name, size=size)
            node_.parent = parent
    return node_


r = Resolver("name")
listing = []
get_listing_flg = False
for line in terminal:
    if get_listing_flg:
        if line[0:1] == "$":
            get_listing_flg = False
            node = get_listing(parent, listing)
            listing = []
        else:
            listing.append(line)
    if line == "$ cd /":
        root = Node("/")
        parent = root
    elif line == "$ ls":
        get_listing_flg = True
    elif line[0:4] == "$ cd":
        target = line[5:]
        if target == "..":
            parent = r.get(parent, "..")
        else:
            target = "dir " + line[5:]
            parent = r.get(parent, target)

if get_listing_flg:
    node = get_listing(parent, listing)

dirs = []
gtsize = 0
tsize = 0
for subnode in PreOrderIter(root):
    try:
        tsize += int(subnode.size)
    except AttributeError:
        pass
unused = 70000000 - tsize
to_free = 30000000 - unused
print(f"unused = {unused}")
print(f"to_free = {to_free}")

if tsize <= 100000:
    gtsize += tsize
dirs.append(tsize)

for fnode in findall(root, filter_=lambda fnode: "dir" in fnode.name):
    print(fnode.name + ":", end="")
    tsize = 0
    for subnode in PreOrderIter(fnode):
        try:
            tsize += int(subnode.size)
        except AttributeError:
            pass
    print(tsize)
    if tsize <= 100000:
        gtsize += tsize
    dirs.append(tsize)

dirs.sort()
for d in dirs:
    if d >= to_free:
        print(d)
        break
