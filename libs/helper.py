import logging


class CatchBaseException(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args)
        except BaseException as e:
            logging.exception(e)
        finally:
            logging.info("Done!")
