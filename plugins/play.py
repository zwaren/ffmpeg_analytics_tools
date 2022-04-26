import subprocess
from argparse import ArgumentParser, Namespace

from plugins.base_plugin import BasePlugin


class PlayPlugin(BasePlugin):
    """Plugin for playing back the media resource"""

    def handle(self, args: Namespace):
        """Run plugin

        :param args: Command line arguments passed to plugins
        :type args: class:`argparse.Namespace`
        :return:
        """
        infile = args.infile
        self.play(infile)

    def play(self, infile: str):
        """Play the media resource

        :param infile: Media resource path
        :type infile: str
        :return:
        """
        subprocess.run(f'ffplay {infile}')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('infile', help='Media resource path')
    args = parser.parse_args()
    PlayPlugin().handle(args)
