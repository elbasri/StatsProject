import os
from django.core.files.storage import StaticFilesStorage

class GraphsStaticStorage(StaticFilesStorage):
    location = 'graphs'

    def __init__(self, base_url=None):
        super().__init__(base_url)
        self.base_url = base_url or '/'
