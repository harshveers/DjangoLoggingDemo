from django.http import HttpResponse
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
	return HttpResponse("Django Logging Example.")

def throw(request):
	raise Exception('This is the exception which will be logged')

def log_error(request):
	logger.error('This is the manual error logging.')
	return HttpResponse("Logged manual error.")