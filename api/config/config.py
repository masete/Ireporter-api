"""
App configurations
"""


class Config:
    """
    This is the parent configurations to be inherited from
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    The configuration for the development environment
    """
    DEBUG = True


