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


# Create your views here.
def home(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		
		template = loader.get_template('index_finance.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_finance.html')
		return HttpResponse(template.render(context, request))

def index(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index.html')
		return HttpResponse(template.render(context, request))
	
def page404(request):
    return render(request, '404.html')
	
def about1(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('about1.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('about1.html')
		return HttpResponse(template.render(context, request))
	
def about2(request):
	uname = request.session.get('username')

	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('about2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('about2.html')
		return HttpResponse(template.render(context, request))

def about3(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('about3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('about3.html')
		return HttpResponse(template.render(context, request))

def about4(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('about4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('about4.html')
		return HttpResponse(template.render(context, request))

def about5(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('about5.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('about5.html')
		return HttpResponse(template.render(context, request))
		
def administration(request):
	uname = request.session.get('adminuser')
	
	if not uname:
		request.session['adminuser'] = ''
		
		context = {
			'adminuser': '',
		}
		template = loader.get_template('admin_login.html')
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect('/adminpage')

def backtesting(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('backtesting.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('backtesting.html')
		return HttpResponse(template.render(context, request))
		
def filesystem(request):
	uname = request.session.get('adminuser')
	
	if not uname:
		return HttpResponseRedirect('/administration')
	else:
		context = {
			'adminuser': uname,
		}
		template = loader.get_template('filesystem.html')
		return HttpResponse(template.render(context, request))
		
def userlist(request):
	uname = request.session.get('adminuser')
	
	if not uname:
		return HttpResponseRedirect('/administration')
	else:
		noteslist = User.objects.all()
		
		result = {'rows':[]}
		for note in noteslist:
			result['rows'].append({'userid':str(note.id), 'username':note.username, 'password':note.password, 'email':note.email})
		template = loader.get_template('userlist.html')
		return HttpResponse(template.render(result, request))
		
def adminpage(request):
	uname = request.session.get('adminuser')
	
	if not uname:
		return HttpResponseRedirect('/administration')
	else:
		context = {
			'adminuser': uname,
		}
		template = loader.get_template('admin_page.html')
		return HttpResponse(template.render(context, request))
		
def adminmail(request):
	uname = request.session.get('adminuser')
	
	if not uname:
		return HttpResponseRedirect('/administration')
	else:
		context = {
			'adminuser': uname,
		}
		template = loader.get_template('admin_mail.html')
		return HttpResponse(template.render(context, request))
		
def adminsms(request):
	uname = request.session.get('adminuser')
	
	if not uname:
		return HttpResponseRedirect('/administration')
	else:
		context = {
			'adminuser': uname,
		}
		template = loader.get_template('admin_sms.html')
		return HttpResponse(template.render(context, request))

def adminlogout(request):
	request.session['adminuser'] = ''
	return HttpResponseRedirect('/administration')

def alertsandwells(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('alerts-and-wells.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('alerts-and-wells.html')
		return HttpResponse(template.render(context, request))

def blog_grid_col_2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_grid_col_2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_grid_col_2.html')
		return HttpResponse(template.render(context, request))
	
def blog_grid_col_3(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_grid_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_grid_col_3.html')
		return HttpResponse(template.render(context, request))
	
def blog_grid_col_4(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_grid_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_grid_col_4.html')
		return HttpResponse(template.render(context, request))
	
def blog_grid_masonry_col_2(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_grid_masonry_col_2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_grid_masonry_col_2.html')
		return HttpResponse(template.render(context, request))
	
def blog_grid_masonry_col_3(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_grid_masonry_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_grid_masonry_col_3.html')
		return HttpResponse(template.render(context, request))
	
def blog_grid_masonry_col_4(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_grid_masonry_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_grid_masonry_col_4.html')
		return HttpResponse(template.render(context, request))
	
def blog_single_left_sidebar(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_single_left_sidebar.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_single_left_sidebar.html')
		return HttpResponse(template.render(context, request))
	
def blog_single_right_sidebar(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_single_right_sidebar.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_single_right_sidebar.html')
		return HttpResponse(template.render(context, request))

def blog_standard_left_sidebar(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_standard_left_sidebar.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_standard_left_sidebar.html')
		return HttpResponse(template.render(context, request))
	
def blog_standard_right_sidebar(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('blog_standard_right_sidebar.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('blog_standard_right_sidebar.html')
		return HttpResponse(template.render(context, request))
	
def buttons(request):
    return render(request, 'buttons.html')
	
def contact1(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('contact1.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('contact1.html')
		return HttpResponse(template.render(context, request))
	
def contact2(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('contact2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('contact2.html')
		return HttpResponse(template.render(context, request))
	
def contact3(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('contact3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('contact3.html')
		return HttpResponse(template.render(context, request))
	
def content_box(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('content_box.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('content_box.html')
		return HttpResponse(template.render(context, request))
	
def documentation(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('documentation.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('documentation.html')
		return HttpResponse(template.render(context, request))
	
def faq(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('faq.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('faq.html')
		return HttpResponse(template.render(context, request))
	
def forms(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('forms.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('forms.html')
		return HttpResponse(template.render(context, request))
	
def gallery_col_2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('gallery_col_2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('gallery_col_2.html')
		return HttpResponse(template.render(context, request))
	
def gallery_col_3(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('gallery_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('gallery_col_3.html')
		return HttpResponse(template.render(context, request))
	
def gallery_col_4(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('gallery_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('gallery_col_4.html')
		return HttpResponse(template.render(context, request))
	
def gallery_col_6(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('gallery_col_6.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('gallery_col_6.html')
		return HttpResponse(template.render(context, request))
	
def icons(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('icons.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('icons.html')
		return HttpResponse(template.render(context, request))
	
def index_agency(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_agency.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_agency.html')
		return HttpResponse(template.render(context, request))
	
def index_landing(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_landing.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_landing.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_classic_flexslider(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_classic_flexslider.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_classic_flexslider.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_classic_gradient_overlay(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_classic_gradient_overlay.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_classic_gradient_overlay.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_classic_static(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_classic_static.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_classic_static.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_classic_text_rotator(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_classic_text_rotator.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_classic_text_rotator.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_classic_video_background(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_classic_video_background.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_classic_video_background.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_fullscreen_flexslider(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_fullscreen_flexslider.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_fullscreen_flexslider.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_fullscreen_gradient_overlay(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_fullscreen_gradient_overlay.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_fullscreen_gradient_overlay.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_fullscreen_static(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_fullscreen_static.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_fullscreen_static.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_fullscreen_text_rotator(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_fullscreen_text_rotator.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_fullscreen_text_rotator.html')
		return HttpResponse(template.render(context, request))
	
def index_mp_fullscreen_video_background(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_mp_fullscreen_video_background.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_mp_fullscreen_video_background.html')
		return HttpResponse(template.render(context, request))
	
def index_op_fullscreen_gradient_overlay(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_op_fullscreen_gradient_overlay.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_op_fullscreen_gradient_overlay.html')
		return HttpResponse(template.render(context, request))
	
def index_photography(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_photography.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_photography.html')
		return HttpResponse(template.render(context, request))
	
def index_portfolio(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_portfolio.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_portfolio.html')
		return HttpResponse(template.render(context, request))
	
def index_restaurant(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_restaurant.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_restaurant.html')
		return HttpResponse(template.render(context, request))
	
def index_shop(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('index_shop.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('index_shop.html')
		return HttpResponse(template.render(context, request))
	
def login_register(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('login_register.html')
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect('/')
	
def logout(request):
	request.session['username'] = ''
	request.session['password'] = ''
	return HttpResponseRedirect('/')

def notebook(request):
	os.system('jupyter notebook Work.ipynb')
	return HttpResponseRedirect('/')
	
def partnership(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		
		template = loader.get_template('partnership.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('partnership.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_boxed_col_2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_boxed_col_2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_boxed_col_2.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_boxed_col_3(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_boxed_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_boxed_col_3.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_boxed_col_4(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_boxed_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_boxed_col_4.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_boxed_gutter_col_2(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_boxed_gutter_col_2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_boxed_gutter_col_2.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_boxed_gutter_col_3(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_boxed_gutter_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_boxed_gutter_col_3.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_boxed_gutter_col_4(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_boxed_gutter_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_boxed_gutter_col_4.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_full_width_col_2(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_full_width_col_2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_full_width_col_2.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_full_width_col_3(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_full_width_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_full_width_col_3.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_full_width_col_4(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_full_width_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_full_width_col_4.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_full_width_gutter_col_2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_full_width_gutter_col_2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_full_width_gutter_col_2.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_full_width_gutter_col_3(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_full_width_gutter_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_full_width_gutter_col_3.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_full_width_gutter_col_4(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_full_width_gutter_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_full_width_gutter_col_4.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_hover_black(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_hover_black.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_hover_black.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_hover_gradient(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_hover_gradient.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_hover_gradient.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_masonry_boxed_col_2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_masonry_boxed_col_2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_masonry_boxed_col_2.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_masonry_boxed_col_3(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_masonry_boxed_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_masonry_boxed_col_3.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_masonry_boxed_col_4(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_masonry_boxed_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_masonry_boxed_col_4.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_masonry_full_width_col_2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_masonry_full_width_col_2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_masonry_full_width_col_2.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_masonry_full_width_col_3(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_masonry_full_width_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_masonry_full_width_col_3.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_masonry_full_width_col_4(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_masonry_full_width_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_masonry_full_width_col_4.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_single_featured_image1(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_single_featured_image1.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_single_featured_image1.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_single_featured_image2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_single_featured_image2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_single_featured_image2.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_single_featured_slider1(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_single_featured_slider1.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_single_featured_slider1.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_single_featured_slider2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_single_featured_slider2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_single_featured_slider2.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_single_featured_video1(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_single_featured_video1.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_single_featured_video1.html')
		return HttpResponse(template.render(context, request))
	
def portfolio_single_featured_video2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('portfolio_single_featured_video2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('portfolio_single_featured_video2.html')
		return HttpResponse(template.render(context, request))
	
def pricing1(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('pricing1.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('pricing1.html')
		return HttpResponse(template.render(context, request))
	
def pricing2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('pricing2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('pricing2.html')
		return HttpResponse(template.render(context, request))
	
def progressbars(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('progress-bars.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('progress-bars.html')
		return HttpResponse(template.render(context, request))
	
def restaurant_menu1(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('restaurant_menu1.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('restaurant_menu1.html')
		return HttpResponse(template.render(context, request))
	
def restaurant_menu2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('restaurant_menu2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('restaurant_menu2.html')
		return HttpResponse(template.render(context, request))
	
def service1(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('service1.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('service1.html')
		return HttpResponse(template.render(context, request))
	
def service2(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('service2.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('service2.html')
		return HttpResponse(template.render(context, request))
	
def service3(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('service3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('service3.html')
		return HttpResponse(template.render(context, request))
	
def shop_checkout(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('shop_checkout.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('shop_checkout.html')
		return HttpResponse(template.render(context, request))
	
def shop_product_col_3(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('shop_product_col_3.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('shop_product_col_3.html')
		return HttpResponse(template.render(context, request))
	
def shop_product_col_4(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('shop_product_col_4.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('shop_product_col_4.html')
		return HttpResponse(template.render(context, request))
	
def shop_single_product(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('shop_single_product.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('shop_single_product.html')
		return HttpResponse(template.render(context, request))
	
def tabs_and_accordions(request):
	uname = request.session.get('username')
	
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('tabs_and_accordions.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('tabs_and_accordions.html')
		return HttpResponse(template.render(context, request))
	
def typography(request):
	uname = request.session.get('username')
	 
	if not uname:
		request.session['username'] = ''
		request.session['idval'] = 0
		request.session['password'] = ''
		
		context = {
			'username': '',
		}
		template = loader.get_template('typography.html')
		return HttpResponse(template.render(context, request))
	else:
		context = {
			'username': uname,
		}
		template = loader.get_template('typography.html')
		return HttpResponse(template.render(context, request))

@csrf_exempt
def search(request):
	uname = request.session.get('username')
    #if post request came 
	if request.method == 'POST':
		#getting values from post
		fromdate = request.POST.get("fromdate")
		todate = request.POST.get("todate")
		
		data = OrderedDict()
		data['SPY'] = web.DataReader('SPY',data_source='google',start=fromdate, end=todate)

		context = {
            'searchresult': data['SPY'].head(),
			'username': uname,
        }
        #getting our showdata template
		template = loader.get_template('backtesting.html')

        #returing the template 
		return HttpResponse(template.render(context, request))

@csrf_exempt
def check(request):
    #if post request came 
    if request.method == 'POST':
		#getting values from post
        uname = request.POST.get("username")
        pword = request.POST.get("password")
		
        userlist = Admin.objects.filter(username=uname, password=pword)
        if not userlist:
            #adding the values in a context variable 
            context = {
                'errormsg': 'Your username and password did not match. Please try again.',
            }
            #getting our showdata template
            template = loader.get_template('admin_login.html')

            #returing the template 
            return HttpResponse(template.render(context, request))
        else:
            request.session['adminuser'] = uname

            uid = json.dumps(userlist.values_list("id")[0])
            uid1 = uid.replace('[', '')
            uid2 = uid1.replace(']', '')
            request.session['adminid'] = uid2
            return HttpResponseRedirect('/adminpage')
    else:
        return HttpResponseRedirect('/administration')

@csrf_exempt
def insert(request):
	uname = request.session.get('username')
	
	#if post request came 
	if request.method == 'POST':
		#getting values from post
		semail = request.POST.get('email')
		user_name = request.POST.get('username')
		pass_word = request.POST.get('password')
		repwd = request.POST.get('re-password')
		contact_no = request.POST.get('contactno')
		
		if(pass_word==repwd):
			msg = 'User registered successfully'

			#adding the values in a context variable 
			context = {
				'msg': msg,
				'username': uname,
			}

			template = loader.get_template('login_register.html')

			query = User(email = semail , username = user_name, password = pass_word, contactno = contact_no)
			query.save()
			return HttpResponse(template.render(context, request))
		else:
			msg = 'The passwords does not match'

			#adding the values in a context variable 
			context = {
				'error': msg,
				'username': uname,
			}

			template = loader.get_template('login_register.html')
			return HttpResponse(template.render(context, request))
	else:
		#if post request is not true 
		#returing the form template 
		return HttpResponseRedirect('/login_register')
		
def user_profile(request):
	uname = request.session.get('username')
	pword = request.session.get('password')
	
	if not uname:
		return HttpResponseRedirect('/')
	else:
		userlist = User.objects.filter(username=uname)
		
		email = json.dumps(userlist.values_list("email")[0])
		cntnumbet = json.dumps(userlist.values_list("contactno")[0])

		mail1 = email.replace('"', '')
		mail2 = mail1.replace('[', '')
		mail3 = mail2.replace(']', '')
		
		contactno1 = cntnumbet.replace('"', '')
		contactno2 = contactno1.replace('[', '')
		contactno3 = contactno2.replace(']', '')

		context = {
			'email': mail3,
			'username': uname,
			'password': pword,
			'contactno': contactno3,
		}
		template = loader.get_template('profile.html')
		return HttpResponse(template.render(context, request))


@csrf_exempt
def smssend(request):
	uname = request.session.get('adminuser')
    #if post request came
	if request.method == 'POST':
		#getting values from post
		accno = request.POST.get("phone")
		password = request.POST.get("password")
		message = request.POST.get("message")
		
		errormsg = ''
		
		subject = 'Titan - The best downloaded template ever\n' + message
		
		try:
			subject = "+".join(subject.split(' '))
			url_for_wsms = 'http://site24.way2sms.com/Login1.action?'
			data_for_wsms = 'username='+accno+'&password='+password+'&Submit=Sign+in'
			data_for_wsms = data_for_wsms.encode('UTF-8')
			
			noteslist = User.objects.all()
			for note in noteslist:
				cookie_jar = http.cookiejar.CookieJar()
				cookie_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

				cookie_opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
			
				user_open = cookie_opener.open(url_for_wsms, data_for_wsms)

				ssionId = str(cookie_jar).split('~')[1].split(' ')[0]
				smsurl = 'http://site24.way2sms.com/smstoss.action?'
				smsdata = 'ssaction=ss&Token='+ssionId+'&mobile='+str(note.contactno)+'&message='+message+'&msgLen=136'
				cookie_opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+ssionId)]
				smsdata = smsdata.encode('UTF-8')
				sentpage = cookie_opener.open(smsurl,smsdata)

			#adding the values in a context variable 
			context = {
                'smsbackmsg': '<div class="alert alert-success alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Your message is send to all customers</div>',
				'username': uname,
            }
            #getting our showdata template
			template = loader.get_template('admin_sms.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
		except BadHeaderError as Ex:
            #adding the values in a context variable 
			context = {
                'smsbackmsg': '<div class="alert alert-danger alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Something bad happend during sending this message. Please try again later</div>',
				'username': uname,
            }
            #getting our showdata template
			template = loader.get_template('admin_sms.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
	else:
        #if post request is not true 
        #returing the form template 
		template = loader.get_template('admin_page.html')
		return HttpResponse(template.render())


@csrf_exempt	
def promotionmail(request):
	uname = request.session.get('adminuser')
    #if post request came 
	if request.method == 'POST':
		#getting values from post
		frommail = request.POST.get("email")
		password = request.POST.get("password")
		message = request.POST.get("message")
		
		errormsg = ''
		
		subject = 'Titan - The best downloaded template ever'
		body = message
		
		try:
			m = text(body)
			m['Subject'] = subject

			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls()
			s.login(frommail, password)
			
			noteslist = User.objects.all()
			for note in noteslist:
				s.sendmail(frommail, note.email, m.as_string())
			
			s.quit()

			#adding the values in a context variable 
			context = {
                'contactbackmsg': '<div class="alert alert-success alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Your mail is send</div>',
				'username': uname,
            }
            #getting our showdata template
			template = loader.get_template('admin_mail.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
		except BadHeaderError as Ex:
            #adding the values in a context variable 
			context = {
                'contactbackmsg': '<div class="alert alert-danger alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Something bad happend during sending this message. Please try again later</div>',
				'username': uname,
            }
            #getting our showdata template
			template = loader.get_template('admin_mail.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
	else:
        #if post request is not true 
        #returing the form template 
		template = loader.get_template('admin_page.html')
		return HttpResponse(template.render())

@csrf_exempt		
def partnerrequest(request):
	uname = request.session.get('username')
    #if post request came
	if request.method == 'POST':
		#getting values from post
		nameval = request.POST.get("name")
		ageval = request.POST.get("age")
		frommail = request.POST.get("email")
		password = request.POST.get("password")
		message = request.POST.get("message")
		contactno = request.POST.get("phonenumber")
		
		errormsg = ''
		
		subject = 'Titan - The best downloaded template ever - Partnership Request'
		body = 'From: '+nameval+' \nAge: '+ageval+' \nPhone number: '+contactno
		
		try:
			m = text(body)
			m['Subject'] = subject

			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls()
			s.login(frommail, password)
			s.sendmail(frommail, "info@quanti.ai", m.as_string())
			s.quit()

			#adding the values in a context variable 
			context = {
                'partnermessage': '<div class="alert alert-success alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Thank You! I will be in touch</div>',
				'username': uname,
            }
            #getting our showdata template
			template = loader.get_template('partnership.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
		except BadHeaderError as Ex:
            #adding the values in a context variable 
			context = {
                'partnermessage': '<div class="alert alert-danger alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Something bad happend during sending this message. Please try again later</div>',
				'username': uname,
            }
            #getting our showdata template
			template = loader.get_template('partnership.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
	else:
        #if post request is not true 
        #returing the form template 
		template = loader.get_template('partnership.html')
		return HttpResponse(template.render())

@csrf_exempt		
def getintouch(request):
	uname = request.session.get('username')
    #if post request came 
	if request.method == 'POST':
		#getting values from post
		nameval = request.POST.get("name")
		frommail = request.POST.get("email")
		password = request.POST.get("password")
		message = request.POST.get("message")
		
		errormsg = ''
		
		subject = 'Contact Form : Titan - The best downloaded template ever'
		body = 'From: '+nameval+' \nEmail: '+frommail+' \nMessage: '+message
		
		try:
			m = text(body)
			m['Subject'] = subject

			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls()
			s.login(frommail, password)
			s.sendmail(frommail, "info@quanti.ai", m.as_string())
			s.quit()

			#adding the values in a context variable 
			context = {
                'contactbackmsg': '<div class="alert alert-success alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Thank You! I will be in touch</div>',
				'username': uname,
            }
            #getting our showdata template
			template = loader.get_template('index_finance.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
		except BadHeaderError as Ex:
            #adding the values in a context variable 
			context = {
                'contactbackmsg': '<div class="alert alert-danger alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Something bad happend during sending this message. Please try again later</div>',
				'username': uname,
            }
            #getting our showdata template
			template = loader.get_template('index_finance.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
	else:
        #if post request is not true 
        #returing the form template 
		template = loader.get_template('index_finance.html')
		return HttpResponse(template.render())
		
@csrf_exempt
def callback(request):
	uname = request.session.get('username')

    #if post request came 
	if request.method == 'POST':
		#getting values from post
		nameval = request.POST.get("name")
		subjectval = request.POST.get("subject")
		phonenum = request.POST.get("phone")
		frommail = request.POST.get("mailid")
		password = request.POST.get("password")
		
		errormsg = ''
		
		subject = 'Please Call Me : Titan - Responsive HTML5 Template for Consultants & Professionals'
		body = 'From: '+nameval+' \nPhone: '+phonenum+' \nSubject: '+subjectval
		
		try:
			m = text(body)
			m['Subject'] = subject

			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls()
			s.login(frommail, password)
			s.sendmail(frommail, "info@quanti.ai", m.as_string())
			s.quit()

			#adding the values in a context variable 
			context = {
                'username': uname,
                'callbackmsg': '<div class="alert alert-success alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Thank You! I will be in touch</div>',
            }
            #getting our showdata template
			template = loader.get_template('index_finance.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
		except BadHeaderError as ex:
            #adding the values in a context variable 
			context = {
                'username': uname,
                'callbackmsg': '<div class="alert alert-danger alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>Something bad happend during sending this message. Please try again later</div>',
            }
            #getting our showdata template
			template = loader.get_template('index_finance.html')

            #returing the template 
			return HttpResponse(template.render(context, request))
	else:
        #if post request is not true 
        #returing the form template 
		template = loader.get_template('index_finance.html')
		return HttpResponse(template.render())

@csrf_exempt		
def validate(request):
    #if post request came 
    if request.method == 'POST':
		
		#getting values from post
        uname = request.POST.get("username")
        pword = request.POST.get("password")
		
        userlist = User.objects.filter(username=uname, password=pword)
        if not userlist:
            #adding the values in a context variable 
            context = {
                'loginerror': 'Your username and password did not match. Please try again.',
            }
            #getting our showdata template
            template = loader.get_template('login_register.html')

            #returing the template 
            return HttpResponse(template.render(context, request))
        else:
            request.session['username'] = uname
            request.session['password'] = pword

            uid = json.dumps(userlist.values_list("id")[0])
            uid1 = uid.replace('[', '')
            uid2 = uid1.replace(']', '')
            request.session['idval'] = uid2
            return HttpResponseRedirect('/index_finance')
    else:
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('login_register.html')
        return HttpResponse(template.render())
		
@csrf_exempt
def changedetails(request):
	uname = request.session.get('username')

	if not uname:
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':
			#getting values from post
			user_name = request.POST.get('username')
			pass_word = request.POST.get('password')
			semail = request.POST.get('email')
			contact_no = request.POST.get('contactno')

			msg = 'Details are Updated successfully'

			#adding the values in a context variable 
			context = {
				'msg': msg,
                'username': user_name,
			}

			template = loader.get_template('profile.html')

			uid = request.session.get('idval')
			userid = int(uid)
			User.objects.filter(id=userid).update(username = user_name, password = pass_word, email = semail, contactno = contact_no)
			request.session['username'] = user_name
			request.session['password'] = pass_word
			return HttpResponse(template.render(context, request))
		else:
			#if post request is not true 
			#returing the form template 
			return HttpResponseRedirect('/user_profile')
