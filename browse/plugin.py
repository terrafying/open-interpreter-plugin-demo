class InterpreterPlugin:
    def __init__(self, name):
        print(f"Initializing {name} plugin...")
        self.name = name
        self.functions = []
        self.callMap = {}

    def get_functions(self):
        return self.functions

    def register_function(self, function_def, function):
        self.functions.append(function_def)
        self.callMap[function_def["name"]] = function

    def execute_function(self, function_name="", parameters={}):
        if function_name not in self.callMap:
            return {"error": "Function not found"}
        else:
            return self.callMap[function_name](self, **parameters)
