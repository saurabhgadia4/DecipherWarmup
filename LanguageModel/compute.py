import os
import logging
def deleteFiles(path=None, files=[]):
	try:
		if not files:
			if path:
				files = os.listdir(path)
		for file in files:
			if os.path.exists(file):
				os.remove(file)
	except Exception as e:
		logging.exception(e)


