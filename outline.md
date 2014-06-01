# Command Line Python

----

# Made Up Of

* Python is very good for command-line programs
  * It's already installed, probably
      * You probably have an old version though
      * Quick start-up
      * Low memory requirements
      
* Command-Line Arguments
  * Options:
    * getopt, optparse, argparse
    * click, cliff, ??
  * Don't use getopt
  * Use argparse
* Input
  * stdin
  * getpass
* Output (Stdout, Stderr)
  * Using `print`
    * Formatting operator vs str.format
  * Colour
* Error-handling
  * Catch exceptions properly!
  * Catch KeyboardInterrupt!
* Signals from the OS
  * Handling signals from the OS
  * Making sure your main thread is not blocking
* Distribution
  * distutils, setuptools
  * platform-specific packaging
  * run your own PyPI

* Interactive command-line programs
* Configuration

pygmentize -O fontfamily='Source Code Pro' -O style=colorful,linenos=1 -f rtf
