def classFactory(iface=None):
    from .RootController import rootController
    return rootController(iface)


