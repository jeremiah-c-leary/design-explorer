from design_explorer import utils


class create():
    '''
    Creates a CCA object with a given instance name.
    '''

    def __init__(self, instance_name):
        self.name = instance_name
        self.components = None

    def add_component(self, oComponent):
        self.components = utils.append_to_list(self.components, oComponent)
