class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title,message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'title' : title,
            'sender': sender,
            'unread': True
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user, N=0):
        """Read up to N messages from the user's inbox.

        :param str user: The username of the inbox owner.
        :param int N: The number of messages to read (0 for all).
        :return: A list of messages marked as read.
        :rtype: list
        :raises KeyError: If the user does not exist.
        """
        if user not in self.boxes:
            raise KeyError("User does not exist")
        user_box = self.boxes[user]
        if N == 0 or N >= len(user_box): # If N is 0, read all messages
            for message in user_box:
                message['unread']=False
            return user_box
        messages_to_read = user_box[:N] # Mark messages as read and return them
        for message in messages_to_read:
            message.read = False
        return messages_to_read

    def search_inbox(self, user, word):
        """Search for messages containing a specific word in the user's inbox.

        :param str user: The username of the inbox owner.
        :param str word: The keyword to search for.
        :return: A list of messages containing the word.
        :rtype: list
        :raises KeyError: If the user does not exist.
        """
        if user not in self.boxes:
            raise KeyError("User does not exist")
        user_messages = self.read_inbox(user, 0)
        word=word.lower()# Read all messages
        return [msg for msg in user_messages if word in msg['body'].lower() or word in msg['title'].lower()]


if __name__=="__main__":
    PostOffice()


