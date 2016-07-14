 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from ollinvfx_test.models import *
from django.shortcuts import render_to_response, redirect, render
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.db.models import Q
import simplejson

# Create your views here.

