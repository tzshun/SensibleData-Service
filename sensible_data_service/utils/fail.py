import os
import datetime
import time
import shutil
from sensible_audit import audit

#TODO: split or rename this

def fail(filename, failed_directory_path, message):
	audit.Audit().e('file_op', 'fail', {'message': message})
	safe_move(filename, failed_directory_path)

def safe_move(filename, move_to_path):
	if not os.path.exists(move_to_path):
		os.makedirs(move_to_path)
	try:
		shutil.move(filename, move_to_path)
	except:
		shutil.move(filename, os.path.join(move_to_path, str(time.time()) + '-' + os.path.basename(filename)))
