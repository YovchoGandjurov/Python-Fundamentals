class User:
    def __init__(self, username, received_messages=None):
        self.username = username
        if received_messages is None:
            self.received_messages = []
        else:
            self.received_messages = received_messages

    def add_message(self, message):
        self.received_messages.append(message)


class Messages:
    def __init__(self, sender, content):
        # super().__init__(username, received_messages)
        self.content = content
        self.sender = sender


data = input()

registered_user = []
collected_massages = []
final_users = []

while data != "exit":
    data = data.split()

    if data[0] == 'register':
        if data[1] not in registered_user:
            registered_user.append(data[1])

    else:
        sender = data[0]
        recipient = data[2]
        content = data[3]

        if sender in registered_user and recipient in registered_user:
            message = Messages(sender, content)
            collected_massages.append(message)
            user = User(sender)
            if sender not in [x.username for x in final_users]:
                final_users.append(user)

    data = input()


for message in collected_massages:
    for user in final_users:
        if user.username == message.sender:
            user.add_message(message.content)

final_input = input().split()

user1 = final_input[0]
user2 = final_input[1]

filtered_list = list(filter(lambda x: x.username == user1 or
                            x.username == user2, final_users))

result = []

if len(filtered_list) == 0:
    print('No messages')

elif len(filtered_list) == 1:
        for item in filtered_list[0].received_messages:
            result.append(f"{filtered_list[0].username}: {item}")
else:
    counter = 1
    if user1 != filtered_list[0].username:
        filtered_list.reverse()

    for item in filtered_list[0].received_messages:
        result.append(f"{filtered_list[0].username}: {item}")

    for item in filtered_list[1].received_messages:
        result.insert(counter, f"{item} :{filtered_list[1].username}")
        counter += 2

print('\n'.join(result))
