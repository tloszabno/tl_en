class Sender(object):
    def __init__(self, supplier):
        self.supplier = supplier
        self.listeners = []

    def register_listener(self, listener):
        self.listeners.append(listener)

    def send(self):
        product = self.supplier.get()
        if product:
            for listener in self.listeners:
                listener(product)
