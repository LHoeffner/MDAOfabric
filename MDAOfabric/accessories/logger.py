import logging


class Logger(logging.Logger):
    """Customized logger class

    In addition to the regular Python logger (which it inherits from), it automatically creates console output
    """
    #TODO: extend to use settings, allow file output
    def __init__(self):
        super(Logger, self).__init__('MDAOlogger')

        # adds console output for every log
        self.console_handle = logging.StreamHandler()
        self.console_handle.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.console_handle.setFormatter(self.formatter)
        self.addHandler(self.console_handle)

    def SetConsoleLevel(self, level):
        """Sets the minimum level for a log to be output to the console

        :param level: new minimum level for console output
        :return: None
        """
        self.console_handle.setLevel(level)


log = Logger()
