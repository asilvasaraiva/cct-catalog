class BookNotFoundError(Exception):
    """Raised by the service layer when a requested book does not exist.

    Equivalent to something like Java's EntityNotFoundException: the
    controller layer is expected to catch this and turn it into an
    HTTP response (404 Not Found).
    """
