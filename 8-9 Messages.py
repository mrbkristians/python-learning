
def show_messages(messages):
    '''Showing all messages'''
    while messages:
        messages = list(messages)
        msg = messages.pop()
        print(msg)
        sended_messages.append(msg)

def archive_messages(sended_messages):
    for message in sended_messages:
        output_text = f"\n\tMessage has been send: {message}"
        print(output_text)

message_pack = ["hello", "how are you", "what you what", "who you with"]
sended_messages = []

show_messages(message_pack)
print(archive_messages(sended_messages))