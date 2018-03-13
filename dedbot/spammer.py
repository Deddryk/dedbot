import re

class Spammer:

    DEFAULT_SPAM = "The quick brown fox jumps over the lazy dog"
    MAX_MESSAGE_LENGTH=140
    EMPTY_LINE_REGEX = '^\s*$'

    def __init__(self, spam_file=None, spam_text=DEFAULT_SPAM, max_message_length=MAX_MESSAGE_LENGTH):
        self.spam_file = spam_file
        self.spam_text = spam_text
        self.max_message_length = max_message_length
        if not self.spam_file is None:
            self.load_spam()
        self.spam_index = 0

    def load_spam(self):
        with open(self.spam_file) as f:
            self.spam = re.sub(Spammer.EMPTY_LINE_REGEX, '', f.read()).split('\n')

    def repeat_spam(self):
        return self.spam_text

    def inc_index(self):
        self.spam_index = (self.spam_index + 1) % len(self.spam)

    def file_spam(self):
        while re.match(Spammer.EMPTY_LINE_REGEX, self.spam[self.spam_index]):
            self.inc_index()
        index = self.spam_index
        self.inc_index()
        return self.spam[index]

    def get_line(self):
        if self.spam_file:
            return self.file_spam()
        else:
            return self.repeat_spam()

    def __next__(self):
        return self.get_line()

    def __iter__(self):
        return self

