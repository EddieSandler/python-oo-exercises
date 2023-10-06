"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    '''constructor method to initalize  counter starting at 100'''
    def __init__(self,start=100):
        self.start=start

    '''method to increment co unter at each invocation
    int:
    current_value
    =============================================='''

    def generate(self):
        current_value=self.start
        self.start +=1
        return current_value

        """method to reset counter to 100 when invoked"""
    def reset(self):
        self.start =100





