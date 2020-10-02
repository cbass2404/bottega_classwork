"""
_ in data attribute says it is protected
__ in data attribute name says it is private
@property is a decorator to tell you it is something you may want to use later and lets you unlocked locked
    attributes
"""

class Invoice:
    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total


google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)
