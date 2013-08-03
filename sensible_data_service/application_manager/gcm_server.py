from gcm import GCM
import gcm
from utils import SECURE_settings
import sys

API_KEY = SECURE_settings.GCM_API_KEY

def sendNotification(gcm_id, data, type):
	gcm_obj = GCM(API_KEY)
	try: 
		response = gcm_obj.plaintext_request(registration_id=gcm_id, data=data)
		return response
	except gcm.gcm.GCMInvalidRegistrationException: pass
	except gcm.gcm.GCMNotRegisteredException: pass
	except: pass
	return {'error':'oooops'}


