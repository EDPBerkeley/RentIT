import shortuuid
from django.utils.crypto import get_random_string


def create_uuid():
    """
    Utility function that creates an alphanumeric entry to be used for uuid
    NOTE: Output of function is NOT necessarily UNIQUE, uniqueness must be
    enforced by DB
    """
    return get_random_string(6, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')