from abc import ABC, abstractmethod


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class IProtocol(ABC):
    __protocol = ""

    @abstractmethod
    def set_protocol(self, *other):
        ...


class MyProtocol(IProtocol):
    __protocol = "I'm"

    def set_protocol(self, other):
        if isinstance(other, str):
            return " ".join([self.__protocol, other])

        return " ".join([self.__protocol, *other])


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyContent(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTMLContent(IContent):

    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if isinstance(self.protocol, IProtocol):
            self.__sender = self.protocol.set_protocol(sender)
        else:
            self.__sender = sender

    def set_receiver(self, *receiver):
        if isinstance(self.protocol, IProtocol):
            self.__receiver = self.protocol.set_protocol(receiver)
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


my_protocol = MyProtocol()
email = Email(my_protocol)
email.set_sender('Gosho')
email.set_receiver('Petrov', 'Shefa', 'Asistentkata')
my_content = MyContent("dfafs")
email.set_content(my_content)
print(email)
