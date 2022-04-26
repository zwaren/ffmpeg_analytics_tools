import json
import os
import sqlite3
from argparse import Namespace, ArgumentParser

from plugins.base_plugin import BasePlugin


class SaveFramesDataToSQLitePlugin(BasePlugin):
    """Plugin for saving frame data from json file to sqlite database"""

    def handle(self, args: Namespace):
        """Run plugin

        :param args: Command line arguments passed to plugins
        :type args: class:`argparse.Namespace`
        :return:
        """
        infile = args.infile
        outfile = args.outfile
        self.save_frames_data_to_sqlite(infile, outfile)

    def save_frames_data_to_sqlite(self, infile: str, outfile: str):
        """Save frame data from json file to sqlite database

        :param infile: Json file path
        :type infile: str
        :param outfile: Resulting sqlite database path
        :type outfile: str
        :return:
        """
        frames = json.load(open(infile)).get('frames')
        columns = frames[0].keys()
        values = ['?' for _ in columns]
        frames_values = [list(frame.values()) for frame in frames]

        if os.path.isfile(outfile):
            os.remove(outfile)
        con = sqlite3.connect(outfile)
        con.execute(f'create table frames (id integer primary key, {", ".join(columns)})')
        with con:
            con.executemany(f'insert into frames ({", ".join(columns)}) '
                            f'values ({", ".join(values)})', frames_values)
        con.close()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('outfile', nargs='?', default='frames.db')
    args = parser.parse_args()
    SaveFramesDataToSQLitePlugin().handle(args)
