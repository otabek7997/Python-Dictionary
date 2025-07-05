users = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
]


for user in users:
    if user["active"] == True:
        user["active"] = False


print(users)
