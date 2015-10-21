class RrdGraphError(Exception):
    status = 400


class RrdDoesNotExist(RrdGraphError):
    status = 404
