## Dependencies
To display the output graphically you need to have `turtle` library.

**NOTE!** If you just want to see the output on the console ignore installing `turtle`

#### Windows Installation
We need to install Python-3 (not Python-2)

#### Linux Installation
Linux operating system, e.g. Ubuntu and Mint, have pre-installed Python-3, but it may not contain `turtle` library.
To install the `turtle` library, use following command:

`$ sudo apt-get install python3-tk`
## **How to Run**

~~~
usage: 
  main.py [-h] [-r READER] -a READER_ARGS [READER_ARGS ...] [-op OUTPUT_TYPE] [-z ZOOM_LEVEL]

optional arguments:
  -h, --help            show this help message and exit

output options:
  -op OUTPUT_TYPE, --output OUTPUT_TYPE
                        Display the result to user additional to the stdout.
                        Currently only 'TurtleGraphic' available (Default
                        None)

  -z ZOOM_LEVEL, --zoom ZOOM_LEVEL
                        Zoom level if -op is set to 'TurtleGraphic' (Default
                        25)

input options:
  -r READER, --reader READER
                        Input type to read data from (default 'readfile')
  
  -a READER_ARGS [READER_ARGS ...], --arguments READER_ARGS [READER_ARGS ...]
                        Arguments to be passed to the reader defined in -r
                        option
~~~

##### _Example to run with graphical output:_
~~~
    python -a <path/to/coordinates/file> -op TurtleGraphic -z 25
~~~
##### _Example to run WITHOUT graphical output_
~~~
    python -a <path/to/coordinates/file>
~~~

