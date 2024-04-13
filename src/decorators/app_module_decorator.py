def AppModule(imports=None):
    imports = imports or []

    def decorator(cls):
        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.modules = []
            for module_class in imports:
                module_instance = module_class(self.server)
                self.modules.append(module_instance)
                print(f"{module_class.__name__} added")

        cls.__init__ = __init__
        return cls

    return decorator
