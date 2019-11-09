from abc import ABCMeta, abstractmethod


class Channel(metaclass=ABCMeta):

    @abstractmethod
    async def open(self):
        raise NotImplemented()

    @abstractmethod
    async def receive(self):
        raise NotImplemented()

    @abstractmethod
    async def send(self, message):
        raise NotImplemented()

    @abstractmethod
    async def close(self):
        raise NotImplemented()
