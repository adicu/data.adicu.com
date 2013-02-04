scripts
=======

this folder gets helper scripts; things that are needed in development
to simulate data, things for production debugging, database start/stop scripts
or one-time data migration scripts. where possible these scripts should leverage lib classes,
and should be runnable in development, even if they serve little purpose there.

python files in this directory should be executed from within this directory
and they should add the application path to sys.path by doing an expanded relative addition.

    import os
    import sys
    base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    if base_dir not in sys.path:
        sys.path.append(base_dir)

(a note about sys.path; It's ok to add the application directory into sys.path when running 
scripts in a sub-directory; that directory must be expanded and not relative to 
'current working directory'. There are no other acceptable cases for changing sys.path)

python files should run `tornado.options.options.parse_command_line()` in their `__main__` block
shell scripts should accept command line arguments matching `.sh` bitly standards
