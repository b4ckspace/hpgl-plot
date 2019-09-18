# Send HP-GL code to 7475A plotter
# Copyright (C) 2019  Luca Schmid

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from argparse import ArgumentParser
from serial import Serial
from time import sleep

def read_code(path):
    code = 'IN;'
    with open(path, 'r') as f:
        code = f.read()
    return code

def check_avail(serial):
    serial.write(b'\x1B.B')
    b = serial.read()
    n = 0
    while b != b'\r':
        if len(b) == 0:
            continue
        n = n * 10 + b[0] - 48
        b = serial.read()
    return n

def main():
    parser = ArgumentParser()
    parser.add_argument('port')
    parser.add_argument('file')
    args = parser.parse_args()

    serial = Serial(port=args.port, timeout=0)
    code = read_code(args.file)
    pos = 0

    while pos < len(code):
        avail = check_avail(serial)
        if avail < 512:
            sleep(0.01)
            continue

        end = pos + avail
        if len(code)-pos < avail:
            end = len(code)

        serial.write(code[pos:end].encode('utf-8'))
        pos = end

if __name__ == '__main__':
    main()
