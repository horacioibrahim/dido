# -*- coding: utf-8 -*-
"""
Receveices, outcomes, manipulates metadata of the objects.
"""

import json


class Metadata(object):
	"""
	Class handling objects that are database schemas.
	Basically one dictionary metadata with key/value pair
	contained {'columne_name': 'python type'}
	"""

	def __init__(self):
		self._meta = None

	@property
	def meta(self):  
	    return self._meta
	
	@meta.setter
	def meta(self, model):
		"""
		Data information organization.

		:param model: dictionary with column and type value "in python world" 
		passed as string (e.g: {'column_1': 'str'} )

		"""
		self._meta = model

	def to_json(self):
		# Returns meta values as json
		return json.dumps(self._meta)

	#def __call__(self):
	#	return self.meta # Try play

	# private
	#def validate_metadata(self):
	#	for k, v in self._meta:


	#_validate_metadata = validate_metadata

	
