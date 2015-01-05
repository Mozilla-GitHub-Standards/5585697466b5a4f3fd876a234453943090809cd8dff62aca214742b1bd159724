def action(func):
    def func_wrapper(self, **kwargs):
        if func.__name__ in self.settings:
            if self.settings[func.__name__]:
                self.logger.debug('Task [%s] is enabled.' % func.__name__)
                return func(self, enabled=True, **kwargs)
            else:
                self.logger.debug('Task [%s] is disabled.' % func.__name__)
        else:
            self.logger.debug('There is no [%s] in settings file, it will run with default settings.' % func.__name__)
            if enabled:
                return func(self, **kwargs)
            else:
                self.logger.debug('Task [%s] is disabled.' % func.__name__)
    return func_wrapper
