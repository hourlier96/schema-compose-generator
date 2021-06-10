from config import *


class Generator:
    DIAG = 'with Diagram("{0}", show=False):'
    CLUSTER = 'with Cluster("{0}"):'

    def __init__(self):
        self.output = DIAG_IMPORT
        self.lvl = 0
        self.list_element = []
        pass

    def create_diag(self, diag_name):
        _diag = self.DIAG.format(diag_name)
        _comment = f'\t# Create Diagrams: {diag_name}\n'
        self.lvl += 1
        self.output += f"{_diag}\n"
        self.output += _comment

    def create_cluster(self, cluster_name):
        _clust = self.CLUSTER.format(cluster_name)
        for _ in range(self.lvl): self.output += "\t"
        self.output += f"{_clust}\n"
        self.lvl += 1

    def create_element(self,  service_name=None, element_name=None):
        _element = f'elem_{service_name.lower().replace("-","_")} = {element_name}("{service_name}")\n'
        self.list_element.append(service_name)
        for _ in range(self.lvl): self.output += "\t"
        self.output += f'{_element}\n'

    def create_link(self, ele1, ele2):
        if ele1.lower() in self.list_element and ele2.lower() in self.list_element:
            self.output += f'\telem_{ele1.lower()} >> elem_{ele2.lower()}\n'
