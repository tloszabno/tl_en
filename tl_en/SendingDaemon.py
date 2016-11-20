import schedule
import config


class SendingDaemon(object):
    def __init__(self, supplier):
        self.supplier = supplier
        self.listeners = []

    def register_listener(self, listener):
        self.listeners.append(listener)

    def run(self):
        schedule.every(config.SENDING_INTERVAL_MIN).minutes.do(self.job)

    def job(self):
        product = self.supplier.get()
        if product:
            map(lambda listener: listener(product), self.listeners)
