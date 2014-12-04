# -*- coding: utf-8 -*-

class DidoException(Exception):
	"""
	Useful for enherit all exceptions
	"""

class ValidateNotImplemented(DidoException):

	def __init__(self, message="Method validate is not implemented"):
		super(ValidateNotImplemented, self).__init__(message)

class InvalidDidoType(DidoException):

	def __init__(self, didotype, 
			message="This value is not matched with the type ({})"):
		super(InvalidDidoType, self).__init__(message.format(didotype))
