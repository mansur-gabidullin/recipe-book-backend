from sqlalchemy import inspect


# https://stackoverflow.com/a/37350445/7738576
def scalar_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
