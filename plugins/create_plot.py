import sqlite3
from argparse import Namespace, ArgumentParser

import matplotlib.pyplot as plt

from plugins.base_plugin import BasePlugin


class CreateFramesDataPlotPlugin(BasePlugin):
    """Plugin for creating a plot which reflects the dependence of the frame size on its number"""

    def handle(self, args: Namespace):
        """Run plugin

        :param args: Command line arguments passed to plugins
        :type args: class:`argparse.Namespace`
        :return:
        """
        infile = args.infile
        outfile = args.outfile
        self.create_frames_data_plot(infile, outfile)

    def create_frames_data_plot(self, infile: str, outfile: str):
        """Create a plot (x - frame id, y - frame size) and save to .png

        :param infile: Sqlite database path
        :type infile: str
        :param outfile: Resulting plot image path
        :type outfile: str
        :return:
        """
        con = sqlite3.connect(infile)

        frames_numbers = []
        frames_sizes = []
        for row in con.execute('select id, pkt_size from frames'):
            frames_numbers.append(row[0])
            frames_sizes.append(int(row[1]))
        con.close()

        fig, ax = plt.subplots()
        ax.plot(frames_numbers, frames_sizes)
        plt.savefig(outfile)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('outfile', nargs='?', default='frames.png')
    args = parser.parse_args()
    CreateFramesDataPlotPlugin().handle(args)
