#!/usr/bin/env python3
"""
Main file
"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """function called filter_datum that returns the log message obfuscated"""
    return re.sub(r'{}(?={})'.format('|'.join(map(re.escape, fields)),
                                     re.escape(separator)), redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).\
         __init__(
            "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
            )
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        def filter_datum(fields, redaction, message, separator):
            return re.sub(r'{}(?={})'.
                          format('|'.join(map(re.escape, fields)),
                                 re.escape(separator)), redaction, message)

        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
