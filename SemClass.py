from threading import Lock

class Lock:
    def __init__(self):
        self.lock = None
    
    def __get__(self, instance, owner):
        return self
    
    def __set__(self, instance, value):
        if self.lock is None:
            self.lock = value
        elif self.lock == value:
            pass
        else:
            self.lock.release()
            self.lock = value
        if self.lock.acquire(False):
            return self.lock
        else:
            return None
    
    def __delete__(self, instance):
        if self.lock is not None:
            if self.lock.locked():
                self.lock.release()
            self.lock = None

    @classmethod
    def locked(cls, func):
        def wrapper(*args, **kwargs):
            with cls() as lock:
                return func(*args, **kwargs)
        return wrapper

class MyClass:
    lock = Lock()

    @lock.locked
    def my_method(self):
        # some code
