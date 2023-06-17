
import os
from pyairtable import Api

class AirtableClient():
    def __init__(self):
        self.api = Api(os.environ.get('AIRTABLE_TOKEN'))

airtable = AirtableClient()