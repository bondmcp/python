"""BondMCP SDK Exceptions"""

class BondMCPError(Exception):
    """Base exception for BondMCP SDK"""
    pass

class AuthenticationError(BondMCPError):
    """Authentication related errors"""
    pass

class APIError(BondMCPError):
    """API related errors"""
    pass
