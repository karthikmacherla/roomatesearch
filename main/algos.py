import random

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
  