import tornado.web


class ArgumentMixin(object):
    def get_bool_argument(self, name, *args, **kwargs):
        """get a request argument that evaluates to a boolean value
        valid values are value.lower() == 'true' || 'false'
        takes an optional default=default_value which is not restricted to bool,
        and may also be None type
        """
        value = self.get_argument(name, *args, **kwargs)
        if not isinstance(value, (str, unicode)):
            return value
        if value.lower() not in ['true', 'false']:
            raise tornado.web.HTTPError(500, "Invalid argument %s. must be true|false" % name)
        return value.lower() == 'true'

    _INT_ARG_DEFAULT = []

    def get_int_argument(self, name, default=_INT_ARG_DEFAULT):
        """get a request argument that evaluates to int(value), or return default
        if provided. Otherwise raise a http 500 error.
        """
        if default is self._INT_ARG_DEFAULT:
            value = self.get_argument(name)
        else:
            value = self.get_argument(name, default=default)

        try:
            return int(value)
        except (TypeError, ValueError):
            if default is not self._INT_ARG_DEFAULT:
                return default
        raise tornado.web.HTTPError(500, "Invalid argument %s. must be int" % name)

    _INT_ARGUMENT_RANGE_DEFAULT = []

    def get_int_argument_range(self, key, min_range, max_range, default=_INT_ARGUMENT_RANGE_DEFAULT):
        """get a request argument that evaluates to int(value), or return default
        if provided. Otherwise raise a http 500 error.
        additionally bound the return value to min..max; default can also be None
        """
        if default is self._INT_ARGUMENT_RANGE_DEFAULT:
            value = self.get_int_argument(key)
        else:
            value = self.get_int_argument(key, default)
        if not isinstance(value, int):
            return default
        value = min(value, max_range)
        value = max(value, min_range)
        return value
