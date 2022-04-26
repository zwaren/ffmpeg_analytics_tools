from argparse import ArgumentParser

from plugins import PlayPlugin, ExtractVideoPlugin, DumpFramesDataPlugin, SaveFramesDataToSQLitePlugin, \
    CreateFramesDataPlotPlugin

parser = ArgumentParser()
subparsers = parser.add_subparsers(
    title='FFmpeg Analytic Plugins',
    description='Collection of plugins for working with media resources using ffmpeg cli tools',
    help='Installed plugins',
)

# plugin 1
play_parser = subparsers.add_parser('play', help='Play the file')
play_parser.add_argument('infile', help='Media resource path')
play_parser.set_defaults(func=lambda args: PlayPlugin().handle(args))

# plugin 2
extract_parser = subparsers.add_parser('extract', help='Extract a video stream')
extract_parser.add_argument('infile', help='Media resource path')
extract_parser.add_argument('outfile', nargs='?', default='outfile.mkv', help='Extracted video stream path')
extract_parser.set_defaults(func=lambda args: ExtractVideoPlugin().handle(args))

# plugin 3
dump_parser = subparsers.add_parser('dump_frames_data',
                                    help='Extract per-frame information for a first video stream into a json file')
dump_parser.add_argument('infile', help='Media resource path')
dump_parser.add_argument('outfile', nargs='?', default='outfile.json', help='Resulting json file path')
dump_parser.set_defaults(func=lambda args: DumpFramesDataPlugin().handle(args))

# plugin 4
save_sqlite_parser = subparsers.add_parser('save_frames_data', help='Save per-frame information into an sqlite database')
save_sqlite_parser.add_argument('infile', help='Json file path')
save_sqlite_parser.add_argument('outfile', nargs='?', default='frames.db', help='Resulting sqlite database path')
save_sqlite_parser.set_defaults(func=lambda args: SaveFramesDataToSQLitePlugin().handle(args))

# plugin 5
create_plot_parser = subparsers.add_parser('create_plot', help='build a plot and save is as a `.png` image')
create_plot_parser.add_argument('infile', help='Sqlite database path')
create_plot_parser.add_argument('outfile', nargs='?', default='frames.png', help='Resulting plot image path')
create_plot_parser.set_defaults(func=lambda args: CreateFramesDataPlotPlugin().handle(args))


if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
