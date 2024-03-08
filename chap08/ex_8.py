#8_9
def show_messages(messages):
    for message in messages:
        print(message)


messages = ['hi ', 'my ', 'name ', 'is ', 'name']
show_messages(messages)

#8_10
def send_messages(messages):
    sent_messages=list()
    for message in messages:
        sent_messages.append(message)
    return sent_messages

msg = send_messages(messages)
show_messages(msg)

msgs = []

while messages: 
    current_message = messages.pop()
    msgs.append(current_message)


print(f"msgs 출력 : {msgs}")
show_messages(msgs)