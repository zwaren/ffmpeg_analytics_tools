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
play_parser.add_argument('infile')
play_parser.set_defaults(func=lambda args: PlayPlugin().handle(args))

# plugin 2
extract_parser = subparsers.add_parser('extract', help='Extract a video stream')
extract_parser.add_argument('infile')
extract_parser.add_argument('outfile', nargs='?', default='outfile.mkv')
extract_parser.set_defaults(func=lambda args: ExtractVideoPlugin().handle(args))

# plugin 3
dump_parser = subparsers.add_parser('dump_frames_data',
                                    help='Extract per-frame information for a first video stream into a json file')
dump_parser.add_argument('infile')
dump_parser.add_argument('outfile', nargs='?', default='outfile.json')
dump_parser.set_defaults(func=lambda args: DumpFramesDataPlugin().handle(args))

# plugin 4
save_sqlite_parser = subparsers.add_parser('save_frames_data', help='Save per-frame information into an sqlite database')
save_sqlite_parser.add_argument('infile')
save_sqlite_parser.add_argument('outfile', nargs='?', default='frames.db')
save_sqlite_parser.set_defaults(func=lambda args: SaveFramesDataToSQLitePlugin().handle(args))

# plugin 5
create_plot_parser = subparsers.add_parser('create_plot', help='build a plot and save is as a `.png` image')
create_plot_parser.add_argument('infile')
create_plot_parser.add_argument('outfile', nargs='?', default='frames.png')
create_plot_parser.set_defaults(func=lambda args: CreateFramesDataPlotPlugin().handle(args))


if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
