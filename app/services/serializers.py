import datetime
import uuid
from functools import singledispatch


@singledispatch
def serialize(rv):
    """
    Define a generic serializable function.
    """
    return rv


@serialize.register(datetime.datetime)
def serialize_dt(rv):
    """Register the `datetime.datetime` type
    for the generic serializable function.

    Serialize a `datetime` object to `string`
    according to strict-rfc3339.
    :param rv: object to be serialized
    :type rv: datetetime.datetime
    :returns: string
    """
    return datetime.datetime.strftime(rv, '%Y-%m-%dT%H:%M:%S.%fZ')


@serialize.register(uuid.UUID)
def serialize_uuid(rv):
    """Register the `uuid.UUID` type
    for the generic serializable function.
    :param rv: object to be serialized
    :type rv: uuid.UUID
    :returns: string
    """
    return str(rv)



