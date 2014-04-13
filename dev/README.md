
#Dev Data

Run `load_dev_dump.sh` to import dev data to your postgres server.
If the server is not on, run:

  sudo service postgresql restart

##Generating Dev Data

Mostly logging this incase it needs to be repeated.
I just deleted from tables until they were a more reasonable size using the random() operator.

    DELETE from {TABLE} WHERE random() < {fraction of what you want left}
