def convert(inspection):
    return {f[0] : f[1] for f in inspection if f[1].__doc__}
