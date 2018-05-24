from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.template import loader
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from quanti.models import User
from quanti.models import Admin
from email.mime.text import MIMEText as text
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError

from pandas_datareader import data, wb
from collections import OrderedDict

import smtplib
import json
import datetime
import subprocess
import webbrowser, sys, os
import pytz

import urllib.request
import http.cookiejar
from getpass import getpass
import pandas_datareader.data as web

from django.db import connection



# Create your views here.

