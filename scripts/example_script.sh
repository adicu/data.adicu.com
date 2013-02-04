# this is a model for using some default bitly shell script setup

while [ "$1" != "" ]; do
    param=${1%=*}
    value=${1#*=}
    case $param in
        --skeleton-app)
            skeleton_app=$value
            ;;
    esac
    shift
done

# this sets the proper $ENVIRONMENT based on where this machine is running
# it also set's up `log()` and `debug()` functions
# also, if you define `$NAGIOS_SVC` you can then echo "status" | $NAGIOS_OK
. /bitly/local/bin/shared_environment.sh

# a script that has utilities for running multiple long running
# processes in parallel
# . /bitly/local/bin/shared_backgrounding.sh
