import abc
from argparse import Namespace


class BasePlugin(abc.ABC):
    """Base class for other plugins' implementation."""

    @abc.abstractmethod
    def handle(self, args: Namespace):
        """Run plugin

        :param args: Command line arguments passed to plugins
        :type args: class:`argparse.Namespace`
        :return:
        """
        raise NotImplementedError
