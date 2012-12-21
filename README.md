# elapsedtimelogger

logging elapsed time in `with` statement.


## Installation

    python setup.py install


## Usage

Basic use:

    >>> from elapsedtimelogger import Logger
    >>> with Logger():
    ...     sum = 0
    ...     for i in range(10000):
    ...         sum += i
    ... 
    0.00346803665161 

With message:

    >>> with Logger(message='foo bar baz'):
    ...     sum = 0
    ...     for i in range(10000):
    ...         sum += i
    ... 
    0.00329089164734 foo bar baz

or

    >>> with Logger() as log:
    ...     log.message = 'foo bar baz'
    ...     sum = 0
    ...     for i in range(10000):
    ...         sum += i
    ... 
    0.00329899787903 foo bar baz

Custom format:

    >>> import logging
    >>> formatter = logging.Formatter('%(asctime)s %(elapsed_time)s %(message)s')
    >>> handler = logging.StreamHandler()
    >>> handler.setFormatter(formatter)
    >>> with Logger(handler, message='foo bar baz'):
    ...     sum = 0
    ...     for i in range(10000):
    ...         sum += i
    ... 
    2012-12-20 22:26:43,175 0.00329899787903 foo bar baz

Log to file:

    >>> formatter = logging.Formatter('%(asctime)s %(elapsed_time)s %(message)s')
    >>> handler = logging.FileHandler('output.log')
    >>> handler.setFormatter(formatter)
    >>> with Logger(handler, message='foo bar baz'):
    ...     sum = 0
    ...     for i in range(10000):
    ...         sum += i
    
    $ cat output.log
    2012-12-20 22:28:14,428 0.0032958984375 foo bar baz


## License

MIT License

