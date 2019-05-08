import random
from .models import Pair

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

# stores number of triadic closures between two users
class UserTcsTuple:

    def __init__(self, u1, u2, tcs):
        self.u1 = u1
        self.u2 = u2
        self.tcs = tcs
    
    def __lt__(self, o2):
        return self.tcs < o2.tcs

def helper_number_of_tcs(u1, u2):
    union = (u1.category_set.all() | u2.category_set.all()).distinct()
    return union.count()

def pair_group(group):
    members = list(group.users.all())
    n = len(members) # number of members in group

    # set matched to true because group has now been matched
    group.matched = True
    group.save()

    l = [] # list of UserTcsTuples

    # go through every pair of members and find # of triadic closures
    for i in range(n):
        for j in range(i + 1, n):
            u1 = members[i]
            u2 = members[j]
            tcs = helper_number_of_tcs(u1, u2)
            l.append(UserTcsTuple(u1, u2, tcs))
    
    # sort in descending orders, highest first
    l.sort(reverse=True)
    count = 0 # keep track of how many pairs we've made
    matched = {} # boolean dict for keeping track of who's matched
    # final_pairs = [] # final list of n/2 pairs
    for pair in l:
        # stop when count is n/2
        if count >= n/2:
            break
        u1 = pair.u1
        u2 = pair.u2
        tcs = pair.tcs
        if not (u1 in matched) and not (u2 in matched): # if neither user has been matched
            matched[u1] = True
            matched[u2] = True # they're now matched
            # make them each other's partner
            pair = Pair()
            pair.user1 = u1
            pair.user2 = u2
            pair.save()
            # add to final pairs
            #final_pairs.append(pair)
            count += 1 # increment count

    #return final_pairs

def find_pairs_in_group(group):
    members = list(group.users.all())
    matched = set() # set for keeping track of who's matched
    pairs = [] # list of pairs

    for member in members:
        if not member in matched:
            pair = member.pair1
            if pair==None:
                pair = member.pair2
                if pair==None:
                    continue
            pairs.append(pair)
            matched.add(pair.user1)
            matched.add(pair.user2)
    
    return pairs