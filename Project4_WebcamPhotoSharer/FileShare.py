from filestack import Client


class FileShare:

    def __init__(self, filepath):
        self.filepath = filepath
        self.api_key = 'AGpMqP8ULTsKfd21RlRm9z'

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath= self.filepath)
        return new_filelink.url
