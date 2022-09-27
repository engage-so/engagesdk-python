
class EngageError(Exception):
    """
        Raises a custom error from the engage SDK  
        Attributes
        message -- custom error message 
    """
    def __init__(self, message="An internal error occured") -> None:
        super().__init__(message)