from src.shared.helpers.errors.base_error import BaseError

class NoItemsFound(BaseError):
    def __init__(self, message: str):
        super().__init__(f'No items found for {message}')

class UserRegistered(BaseError):
    def __init__(self, message: str):
        super().__init__(f'User is already registered {message}')

class UserNotRegistered(BaseError):
    def __init__(self, message: str):
        super().__init__(f'User is not registered {message}')

class NoSpaceRooms(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Not enough space for subscribe the item {message}')

class DuplicatedItem(BaseError):
    def __init__(self, message: str):
        super().__init__(f'The item alredy exists for this {message}')
        
class ForbiddenAction(BaseError):
    def __init__(self, message: str):
        super().__init__(f'That action is forbidden for this {message}')

