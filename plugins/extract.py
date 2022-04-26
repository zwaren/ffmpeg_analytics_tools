import subprocess
from argparse import Namespace, ArgumentParser

from plugins.base_plugin import BasePlugin


class ExtractVideoPlugin(BasePlugin):
    """Plugin for extracting video stream from media resource"""

    def handle(self, args: Namespace):
        """Run plugin

        :param args: Command line arguments passed to plugins
        :type args: class:`argparse.Namespace`
        :return:
        """
        infile = args.infile
        outfile = args.outfile
        self.extract_video(infile, outfile)

    def extract_video(self, infile: str, outfile: str):
        """Extract video stream from media resource

        :param infile: Media resource path
        :type infile: str
        :param outfile: Extracted video stream path
        :type outfile: str
        :return:
        """
        subprocess.run(f'ffmpeg -i {infile} -c:v copy -an -y {outfile}')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('outfile', nargs='?', default='outfile.mkv')
    args = parser.parse_args()
    ExtractVideoPlugin().handle(args)
