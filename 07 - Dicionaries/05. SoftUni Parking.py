n_commands = int(input())

user_database = {}

for i in range(n_commands):
    line = input()

    if line.split()[0] == "register":
        username = line.split()[1]
        plates = line.split()[2]

        if username not in user_database:
            user_database[username] = plates
            print(f"{username} registered {user_database[username]} successfully")
        elif username in user_database:
            print(f"ERROR: already registered with plate number {user_database[username]}")


    elif line.split()[0] == "unregister":
        username = line.split()[1]
        if username in user_database:
            del user_database[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for user, plates_number in user_database.items():
    print(f"{user} => {plates_number}")