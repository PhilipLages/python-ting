from file_management import txt_importer
from queue import Queue

def process(path_file, instance):
    queue = Queue()

    news = txt_importer(path_file)
    for new in news:       



def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
