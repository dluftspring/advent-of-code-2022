import os
import sys
import re
from typing import Callable, Iterable, Mapping, Tuple
from common.utils import load_data


class DirectoryWalker(object):

    def __init__(self, cli_commands: Iterable):
        self.cli_commands = cli_commands
        self.current_path = '/'
        self.dir_size = {'/': 0}

    def walk(self):
        for cmd in self.cli_commands:
            self._parse_cmd(cmd)

    @property
    def cmd_mapper(self) -> Mapping[str, Callable]:
        return {
            'ls': self._ls,
            'cd': self._cd,
            'dir': self._dir,
        }

    def _parse_cmd(self, cmd: str) -> Tuple[str, str]:
        cmd = cmd.replace('$','').strip()
        cmd_type = self._determine_line_type(cmd)
        line = cmd.split(' ')

        if cmd_type == 'file':
            arg = line[0]
        elif cmd_type == 'ls':
            arg = None
        else:
            arg = line[1]

        if arg:
            self.cmd_mapper.get(cmd_type, self._process_file)(arg)

    def _ls(self, *args: str):
        pass


    def _cd(self, path: str):

        if path == '..':
            self.current_path = self.current_path.rsplit('/', 2)[0] + '/'

        elif path == '/':
            self.current_path = '/'

        else:
            self.current_path += f'{path}/'

    def _dir(self, path: str):
        if not self.dir_size.get(self.current_path+path+'/'):
            self.dir_size[self.current_path+path+'/'] = 0

    def _determine_line_type(self, line: str) -> str:

        if line.startswith('dir'):
            return 'dir'

        if line.startswith('cd'):
            return 'cd'

        if line.startswith('ls'):
            return 'ls'

        if re.match('[0-9]', line):
            return 'file'

    def _process_file(self, size: str):

        num_dirs = self.current_path.count('/') + 1
        for i in range(1, num_dirs):
            super_path = self.current_path.rsplit('/', i)[0] + '/'
            self.dir_size[super_path] += int(size)

    def sum_dirs_with_size(self, size: int) -> Iterable[str]:
        return sum([v for _, v in self.dir_size.items() if v >= size])

    def sum_dirs_less_than_size(self, size: int) -> Iterable[str]:
        return sum([v for _, v in self.dir_size.items() if v <= size])

    def find_dir_with_size(self, size: int, epsilon: int = None) -> Iterable[str]:
        return sorted([v for k, v in self.dir_size.items() if v >= size])[0]


if __name__ == "__main__":

    cli_commands = load_data(day=7)
    walker = DirectoryWalker(cli_commands)
    walker.walk()
    print(f"Total size of directories less than 100,000 is: {walker.sum_dirs_less_than_size(100_000)}")
    free_space_required = 30_000_000-(70_000_000-walker.dir_size['/'])
    print(f"The smallest directory that would increase free space is: {walker.find_dir_with_size(free_space_required)}")