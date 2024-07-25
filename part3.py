class NamespaceManager:
    def __init__(self):
        self.namespace = {}

    def set_variable(self, name, value):
        self.namespace[name] = value

    def get_variable(self, name):
        return self.namespace[name]

    def delete_variable(self, name):
        del self.namespace[name]

    def list_variables(self):
        return list(self.namespace.keys())

    def execute_function(self, code):
        return exec(code, self.namespace)
