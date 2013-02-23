lib directory
=============

lib directory has files that provide generic formatters, database accessors, or other related methods
files in this directory should never handle requests directly, but should have defined input/outputs

files in this directory are also often shared with other applications, and `~/test.sh` ensures that files
named the same are identical. This is the preferred method to share code between applications.

It is expected to re-use library files from other applications by copying things (like MemcachePool.py) into
this directory.
