"""
Exception class to raise exception
"""
class NotAllowed(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message