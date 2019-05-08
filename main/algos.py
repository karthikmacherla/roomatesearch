import random

# This algorithm finds the number of focal closures between a user
# and the rest of the users on the server.
# Algo: Runs BFS and finds all vertices that are 2 away (since the graph 
# bipartite). Vertices that are two away on multiple paths (i.e. multiple triadic
# closures) will recieve higher numbers in the map we return. 

def find_triadic_closures(user):
    queryset = user.category_set.all()
    usersMap = dict()
    for category in queryset:
        for user in category.users.all():
            if user.group_set.count() > 0:
                # don't include people in groups
                continue
            if usersMap.__contains__(user):
                usersMap.update({user: usersMap.get(user) + 1})
            else:
                usersMap.update({user: 1})
    return usersMap
  