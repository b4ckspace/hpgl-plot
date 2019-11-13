# HP 7475A plotter sendhpgl script

Python module to send HP-GL code to a 7475A plotter

## Installation

Clone this repository and `cd` into the directory:

```
git clone https://github.com/b4ckspace/hpgl-plot
cd hpgl-plot
```

You should install the module and its dependencies in a Python virtual environment. To create and enter one, execute:

```
virtualenv env
source env/bin/activate
```

To install the sendhpgl module along with its deps, run:

```
pip install .
```

## Usage

The module takes two arguments:

* The serial port your plotter is connected to (probably /dev/ttyUSB0)
* The path to your .hpgl file

To run it, execute the following while inside the venv:

```
sendhpgl /dev/ttyUSB0 path/to/file.hpgl
```

Your device should now start plotting.

## Troubleshooting

* If after an SP your plotter places a dot at its previous position, you should insert a `PU` command *before* each `SP`. It will still move to its last position, but it won't drop the pen.
