from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from xml.dom import minidom
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from django.http import *
from django.contrib.auth.models import User
import xml.etree.ElementTree as ET
import sys
import os

from chat.models import ChatRoom

def prettify(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def logintosystem(request,password,username,command):
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)

			success = Element('success',{'version':'1.0'})

			comment = Comment('Succes, user valid')
			success.append(comment)

			child_user = SubElement(success, 'code', {'user':username})
			child_user.text = '007'

			child_command = SubElement(success, 'child_command', {'command':command})
			child_command.text = 'command executed was ' + command

			print prettify(success)

			return HttpResponseRedirect('/accounts/loggedin/')
		else:
			error = Element('error',{'version':'1.0'})

			comment = Comment('Error, user invalid')
			error.append(comment)

			child_user = SubElement(error, 'code', {'user':username})
			child_user.text = '007'

			child_command = SubElement(error, 'child_command', {'command':command})
			child_command.text = 'command to be executed ' + command

			print prettify(error)

			return HttpResponseRedirect('/accounts/invalid/')
	else:
		error = Element('error',{'version':'1.0'})

		comment = Comment('Error, user invalid')
		error.append(comment)

		child_user = SubElement(error, 'code', {'user':username})
		child_user.text = '007'

		child_command = SubElement(error, 'child_command', {'command':command})
		child_command.text = 'command to be executed ' + command

		print prettify(error)

		return HttpResponseRedirect('/accounts/invalid/')

def auth_view(request):
	currentdirpath = os.getcwd()
	tree = ET.parse(os.path.join(os.getcwd(), 'login_user.xml'))
	root = tree.getroot()
	print root
	for i in root.iter('root'):
		password = i.attrib['password']
		user = i.attrib['user']
		command = i.attrib['command']
		print user,password,command
	if command == 'logintosystem':
		logintosystem(request,password,user,command)
	else:
		return False

@login_required
def index(request):
    chat_rooms = ChatRoom.objects.order_by('name')[:5]
    context = {
        'chat_list': chat_rooms,
    }
    return render(request,'chats/index.html', context)

@login_required
def chat_room(request, chat_room_id):
    chat = get_object_or_404(ChatRoom, pk=chat_room_id)
    return render(request, 'chats/chat_room.html', {'chat': chat})

@login_required
def longpoll_chat_room(request, chat_room_id):
    chat = get_object_or_404(ChatRoom, pk=chat_room_id)
    return render(request, 'chats/longpoll_chat_room.html', {'chat': chat})
