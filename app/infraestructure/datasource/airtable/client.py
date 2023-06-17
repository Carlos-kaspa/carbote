
import os
from pyairtable import Api

class AirtableClient():
    def __init__(self):
        self.api = Api(os.environ.get('_AIRTABLE_TOKEN_'))

airtable = AirtableClient()