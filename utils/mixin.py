class ReprMixin:
    def __repr__(self):
         return f'Создан объект {self.__class__.__name__} ({self.__dict__.items()})'
