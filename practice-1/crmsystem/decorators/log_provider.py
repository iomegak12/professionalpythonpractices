class LogProvider(object):
    def __init__(self, pre: bool = False, post: bool = False):
        super().__init__()
        self.pre = pre
        self.post = post

    def __call__(self, function):
        def wrap_call(*args, **kargs):
            print('Logging Decorator Provider ...')

            if self.pre:
                print('[BEGIN] Logging Started ...')

            result = function(*args, **kargs)

            if self.post:
                print('[END] Logging Completed ...')

            return result

        return wrap_call
