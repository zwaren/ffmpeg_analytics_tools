import subprocess
from argparse import Namespace, ArgumentParser

from plugins.base_plugin import BasePlugin


class DumpFramesDataPlugin(BasePlugin):
    """Plugin for extracting per-frame information for a first video stream into a json file"""

    def handle(self, args: Namespace):
        """Run plugin

        :param args: Command line arguments passed to plugins
        :type args: class:`argparse.Namespace`
        :return:
        """
        infile = args.infile
        outfile = args.outfile
        self.dump_frames_data(infile, outfile)

    def dump_frames_data(self, infile: str, outfile: str):
        """Extract per-frame information for a first video stream into a json file

        :param infile: Media resource path
        :type infile: str
        :param outfile: Resulting json file path
        :type outfile: str
        :return:
        """
        with open(outfile, 'w') as output:
            subprocess.run(f'ffprobe -show_frames -print_format json {infile}', stdout=output)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('outfile', nargs='?', default='outfile.json')
    args = parser.parse_args()
    DumpFramesDataPlugin().handle(args)
