import os

from src.config import settings



def is_dir_path(path):
    """Utility function to check whether a path is an actual directory"""
    if os.path.isdir(path):
        return path
    else:
        raise NotADirectoryError(path)
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Defines some parameters for Smart-Fishing project")
    parser.add_argument("--path",
                        help="Pattern of files to watch",
                        default=settings.watch_directory,
                        )
    parser.add_argument("-d", "--watch-delay",
                        help="Watch delay, default is 5s", 
                        default=settings.watch_delay,
                        type=int,
                        )
    parser.add_argument("-r", "--recursive",
                        action="store_true",
                        help="Whether to recursively watch for the path's children, default is True",
                        default=settings.watch_recursively,
                        )
    parser.add_argument("-p", "--pattern",
                        help="Pattern of files to watch",
                        default=settings.watch_pattern,
                        )
    # parse the arguments
    args = parser.parse_args()
    