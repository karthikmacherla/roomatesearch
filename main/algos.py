
def find_triadic_closures(user):
    queryset = user.category_set.all()
    usersMap = dict()
    for category in queryset:
        for user in category.users.all():
            if usersMap.__contains__(user):
                usersMap.update({user: usersMap.get(user) + 1})
            else:
                usersMap.update({user: 1})
    return usersMap
