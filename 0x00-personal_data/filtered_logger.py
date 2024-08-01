#!/usr/bin/env python3
""" Use of regex in replacing occurrences of certain field values """
import re


def filter_datum(fields: list[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Return regex log message """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)

    return message
