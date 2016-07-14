 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from ollinvfx_testdebug.models import *
from django.db.models import Max, Min, Count, Avg, Q
import datetime
from django.shortcuts import render_to_response, redirect, render
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.core import serializers
import simplejson

# Create your views here.

##########################################################
#					GLOBAL VARIABLES					 #
##########################################################

try:
	asse_obj = Assets.objects.all()order_by('assetname')
	proj_obj = Project.objects.all().order_by('projectname')
	shot_obj = Shot.objects.all().order_by('shotname')
except Exception as e:
	print '%s (%s)' % (e.message, type(e))

task_entity_types = {
						'ENTITY_TYPE_PROJECT':1,
						'ENTITY_TYPE_SEQUENCE':2,
						'ENTITY_TYPE_SHOT':3,
						'ENTITY_TYPE_BID':4,
						'ENTITY_TYPE_SERVICE':5,
						'ENTITY_TYPE_TASK':6,
						'ENTITY_TYPE_MILESTONE':7
					}


##########################################################
#					  GLOBAL METHODS					 #
##########################################################

def getTaskIDFromEntityTypeAndEntityID(taskEntityTypeID,entityID):
	taskID = -1
	try:
		task_obj = Task.objects.get(Q(entitytypeid=taskEntityTypeID) & Q(entityid=entityID))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	if task_obj != None:
		taskID = task_obj.taskid
	return taskID

def getTaskEntityNameFromEntityTypeAndEntityID(taskEntityTypeID,entityID):
	taskName = -1
	try:
		task_obj = Task.objects.get(Q(entitytypeid=taskEntityTypeID) & Q(entityid=entityID))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	if task_obj != None:
		taskName = task_obj.taskname
	return taskName

def getLastTaskForProject(projectid):
	position = -1
	try:
		task_obj = Task.objects.filter(projectid=projectid).aggregate(Max('position'))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	if task_obj != None:
		position = task_obj['position__max']
	return position

def prepareSQLString(sql):
	safeSQL = sql.replace("'","''")
	safeSQL = safeSQL.replace("\\","\\\\")
	safeSQL = safeSQL.replace("\"","\\\"")
	safeSQL = safeSQL.replace("\\x00","\\\\x00")
	safeSQL = safeSQL.replace("\\n","\\\\n")
	safeSQL = safeSQL.replace("\\r","\\\\r")
	safeSQL = safeSQL.replace("\\xla","\\\\xla")
	return str(safeSQL)

def getAssetTypeFromString(typen):
	typeID = ''
	try:
		typeID = Assettype.objects.get(assettypename=typen)
		typeID = typeID.assettypeid
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	return typeID

def encodeAssetPermissions(tmpbin):
	dec = 0
	i = 0
	for it in tmpbin:
		dec = dec | (1 << i) * it
		i += 1
	return dec

def stringToPermissions(strper):
	tmpBin = [0]*5
	if strper.find('C',0) != -1:
		tmpBin[0] = 1
	if strper.find('A',0) != -1:
		tmpBin[1] = 1
	if strper.find('E',0) != -1:
		tmpBin[2] = 1
	if strper.find('V',0) != -1:
		tmpBin[3] = 1
	if strper.find('S',0) != -1:
		tmpBin[4] = 1
	return encodeAssetPermissions(tmpBin)

def getPermissionsListForUserType(typeuser):
	lst = ''
	if (typeuser.typename == 'Administrator') or (typeuser.typename == 'Capturer'):
		for i in range(1,63):
			lst += str(i)
			if i <= 62:
				lst += ','
		return lst
	pw = (2**(int(typeuser.usertype)-3))
	for i in range(1,63):
		if (i % pw) == 0:
			for j in range(0,pw+1):
				lst += str(i+j)
				if i+j <= 62:
					lst += ','
			i = i + pw
	return lst

##########################################################
# Theses steps validate if a user is authenticate or not #
##########################################################

def login_user(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/accounts/loggedin/')
		else:
			return HttpResponseRedirect('/accounts/invalid/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def invalid_login(request):
	return render_to_response('invalid_login.html')

@login_required
def loggedin(request):
	return render_to_response('loggedin.html',{'full_name': request.user.username})

@login_required
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/accounts/login_user/')

##########################################################
# Theses steps checks if a user is allowed to execute a  #
# given command and also checks for the extended         #
# permissions of the user                                #
##########################################################

'''@login_required
def allow(username, password, command):
	if userIsBlocked(username):
		return False
	user = User.objects.get(userid=username, password=password)

	return True'''

@login_required
def shot_options(request):
	return render_to_response('shot_options.html')

##########################################################
# Theses steps updates a shot along with all the other   #
# that are related to the table Shot                     #
##########################################################

@login_required
def update_shot(request):
	c = {}
	c.update(csrf(request))
	try:
		task_obj = Task.objects.filter(projectid__in=[78,12,456,11])
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	shot_ids = []
	proj_ids = []
	vfxi_ids = []
	sequ_ids = []
	shnm_ids = []
	stat_ids = []
	print len(task_obj)
	for i in shot_obj:
		shot_ids.append(i.shotid)
		if i.vfxid not in vfxi_ids:
			vfxi_ids.append(i.vfxid)
		if i.sequenceid not in sequ_ids:
			sequ_ids.append(i.sequenceid)
		if i.shotname not in shnm_ids:
			shnm_ids.append(i.shotname)
		if i.status not in stat_ids:
			stat_ids.append(i.status)
	c['proj_obj'] = proj_obj
	c['sequ_ids'] = sequ_ids
	c['shnm_ids'] = sorted(shnm_ids)
	c['shot_ids'] = shot_ids
	c['stat_ids'] = sorted(stat_ids)
	c['vfxi_ids'] = sorted(vfxi_ids)
	return render_to_response('updateshotgeneral.html',c)

def updateshotstatus(projectid,shotid,status):
	prevStatus = ''
	prevStatusName = ''
	newStatusName = ''
	vfxID = ''
	shotName = ''
	notifyVFXProd = False
	statusName = ''
	error = False
	try:
		status_obj = Status.objects.filter(Q(shotid=shotid) & Q(projectid=projectid)).values('status','vfxid','shotname')
		prevStatus = status_obj[0].status
		vfxID = status_obj[0].vfxid
		shotName = status_obj[0].shotname
		if status != prevStatus:
			notifyVFXProd = True
			try:
				status_obj = Status.objects.filter(Q(status=status) | Q(status=prevStatus)).values('status','statusname')
				print 'Status obtained %i' % st_obj[0].status

				if len(status_obj) == 2:
					for i in status_obj:
						if i.status == status:
							statusName = i.statusname
						else:
							prevStatusName = i.statusname
			except Exception as e:
				print '%s (%s)' % (e.message, type(e))
			#statusChange(projectid,shotid,prevStatusName,statusName,user)
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	try:
		shot_obj = Shot.objects.filter(shotid=shotid).update(status=status)
	except Exception as e:
		error = True
		print '%s (%s)' % (e.message, type(e))
	if (notifyVFXProd) and (not error):
		prevStatusName = ''
		newStatusName = ''
		try:
			status_obj = Status.objects.filter(Q(status=status)|Q(status=prevStatus))
			if len(status_obj) > 0:
				for j in status_obj:
					if j.status == prevStatus:
						prevStatusName = j.statusname
						# addToLog(user,'PrevStatusName: '+prevStatusName)
					elif j.status == status:
						newStatusName = j.statusname
						# addToLog(user,'PrevStatusName: '+newStatusName)
		except Exception as e:
			print '%s (%s)' % (e.message, type(e))
		projName = ''
		projNickName = ''
		try:
			proj_obj = Project.objects.filter(projectid=projectid).values('projectname','projectnickname')
			if len(proj_obj) > 0:
				projName = proj_obj[0].projectname
				projNickName = proj_obj[0].projectnickname
		except Exception as e:
			print '%s (%s)' % (e.message, type(e))
		#if notifyVFXProd:
			#send email with details

@login_required
def updateshotgeneral(request):
	# user = request.user
	# print 'User name %s' % user.username
	# print 'User password %s' % user.password
	# if allow(user.username, user.password, 'updateshotgeneral'):
	error = False
	update = True
	projectid = request.POST.get('projectid')
	shotid = request.POST.get('shotid')
	vfxid = request.POST.get('vfxid')
	workedby = request.POST.get('workedby')
	location = request.POST.get('location')
	isreference = request.POST.get('isreference', 0)
	scenenumber = request.POST.get('scenenumber')
	pagenumber = request.POST.get('pagenumber')
	cameramotion = request.POST.get('cameramotion')
	sequenceid = request.POST.get('sequenceid')
	shotname = request.POST.get('shotname')
	directornotes = request.POST.get('directornotes', '')
	shotdescription = request.POST.get('shotdescription', '')
	vfxtasks = request.POST.get('vfxtasks', '')
	frames = request.POST.get('frames')
	status = request.POST.get('status')
	typeshot = request.POST.get('type')
	lens = request.POST.get('lens', '')
	sortindex = request.POST.get('sortindex', -1)
	take = request.POST.get('take', 0)
	if (shotname == '') and (vfxid == ''):
		update = False
	if update:
		try:
			print 'ENTRO ACA!!!!!!!!'
			shot_obj = Shot.objects.get(Q(shotid=shotid) & Q(projectid=projectid))
			if shotname != '':
				shot_obj.shotname = shotname
			else:
				pass
			if vfxid != '':
				shot_obj.vfxid = vfxid
			else:
				pass
			if directornotes != '':
				shot_obj.directornotes = directornotes
			else:
				pass
			if workedby != '':
				shot_obj.workedby = workedby
			else:
				pass
			if scenenumber != '':
				shot_obj.scenenumber = scenenumber
			else:
				pass
			if sequenceid != '':
				shot_obj.sequenceid = sequenceid
			else:
				pass
			if cameramotion != '':
				shot_obj.cameramotion = cameramotion
			else:
				pass
			if pagenumber != '':
				shot_obj.pagenumber = pagenumber
			else:
				pass
			if shotdescription != '':
				shot_obj.shotdescription = shotdescription
			else:
				pass
			if vfxtasks != '':
				shot_obj.vfxtasks = vfxtasks
			else:
				pass
			if frames != '':
				shot_obj.frames = frames
			else:
				pass
			if typeshot != '':
				shot_obj.type = typeshot
			else:
				pass
			if lens != '':
				shot_obj.lens = lens
			else:
				pass
			if isreference != '':
				shot_obj.isreference = isreference
			else:
				pass
			if sortindex != '':
				shot_obj.sortindex = sortindex
			else:
				pass
			if take != '':
				shot_obj.take = take
			else:
				pass
			shot_obj.save()
			return render_to_response('updateshotgeneral_success.html')
		except Exception as e:
			error = True
			print '%s (%s)' % (e.message, type(e))
		updateshotstatus(projectid,shotid,status)
		#DELETE ALL ARTIST RELATED TO THIS SHOT
		# try:
		# 	Shotuser.objects.filter(shotid=shotid).delete()
		# except Exception as e:
		# 	error = True
		# 	print '%s (%s)' % (e.message, type(e))
		# if not (error):
		# 	for i in artist_list:
		# 		try:
		# 			SU = Shotuser()
		# 			SU.shotid = shotid
		# 			SU.userid = i
		# 			SU.save()
		# 		except Exception as e:
		# 			print '%s (%s)' % (e.message, type(e))
		# else:
		# 	print 'ERROR IN UPLOADSHOTGENERAL!!!'
		#SAVE THE CUSTOMFIELDS, UPDATE IF THERE, INSERT IF NOT
		# if not (error):
		# 	for j in custom_fields:
		# 		if j.shotcustomshotfieldid == 0:
		# 			try:
		# 				SCSF = Shotcustomshotfield()
		# 				SCSF.shotid = shotid
		# 				SCSF.customshotfieldid = j.customshotfieldid
		# 				SCSF.value = j.value
		# 				SCSF.save()
		# 			except Exception as e:
		# 				print '%s (%s)' % (e.message, type(e))
		# 		else:
		# 			try:
		# 				scsf_obj = Shotcustomshotfield.objects.get(shotcustomshotfieldid=j.shotcustomshotfieldid)
		# 				scsf_obj.value = j.value
		# 				scsf_obj.save()
		# 			except Exception as e:
		# 				print '%s (%s)' % (e.message, type(e))
		#EDIT SHOTAUTOTASK TO REFLECT THE SEQUENCE CHANGE
		# shotTaskID = getTaskIDFromEntityTypeAndEntityID(str(ENTITY_TYPE_SHOT),shotid)
		# if shotTaskID != -1:
		# 	parentTaskID = ''
		# 	parentEntityType = ''
		# 	parentEntityID = ''
		# 	if sequenceid != 0:
		# 		parentEntityType = str(ENTITY_TYPE_SEQUENCE)
		# 		parentEntityID = sequenceid
		# 	else:
		# 		parentEntityType = str(ENTITY_TYPE_PROJECT)
		# 		parentEntityID = projectid
		# 	parentTaskID = getTaskIDFromEntityTypeAndEntityID(parentEntityType,parentEntityID)
		# 	try:
		# 		task_obj = Task.objects.get(taskid=shotTaskID)
		# 		task_obj.parentid = parentTaskID
		# 		task_obj.taskname = str(vfxid) + '/' + str(shotname)
		# 		task_obj.save()
		# 	except Exception as e:
		# 		print '%s (%s)' % (e.message, type(e))
	else:
		return render_to_response('updateshotgeneral_error.html')
	#return not(error)

##########################################################
# Theses steps removes a shot along with all the other   #
# that are related to the table Shot                     #
##########################################################

@login_required
def remove_shot(request):
	c = {}
	c.update(csrf(request))
	c['shot_obj'] = shot_obj
	return render_to_response('removeshot.html',c)

def removeTask(taskid,reallyDelete):
	error = False
	if (taskid == 0) or (taskid == -1):
		return False
	if reallyDelete == True:
		try:
			task_obj = Task.objects.filter(parentid=taskid)
		except Exception as e:
			print '%s (%s)' % (e.message, type(e))
		children = []
		if len(task_obj) > 0:
			for i in task_obj:
				children.insert(0,i.taskid)
		for j in children:
			removeTask(j,True)
	else:
		theParent = 0
		try:
			task_obj = Task.objects.filter(parentid=taskid)
			theParent = task_obj.parentid
		except Exception as e:
			error = True
			print '%s (%s)' % (e.message, type(e))
		if not (error):
			try:
				Task.objects.filter(parentid=taskid).update(parentid=theParent)
			except Exception as e:
				error = True
				print '%s (%s)' % (e.message, type(e))
	if not (error):
		try:
			Task.objects.filter(taskid=taskid).delete()
		except Exception as e:
			error = True
			print '%s (%s)' % (e.message, type(e))
	if not (error):
		try:
			Taskartist.objects.filter(taskid=taskid).delete()
		except Exception as e:
			error = True
			print '%s (%s)' % (e.message, type(e))
	if not (error):
		try:
			Taskdependencies.objects.filter(dependencyid=taskid).delete()
		except Exception as e:
			error = True
			print '%s (%s)' % (e.message, type(e))
	return not (error)

def removeAutoTask(entitytypeid,entityid,shotid,reallyDelete):
	error = False
	if reallyDelete == '':
		reallyDelete = False
	try:
		task_obj = Task.objects.get(Q(entitytypeid=entitytypeid) & Q(entityid=entityid))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	if (task_obj.taskid == 0) or (task_obj.taskid == -1):
		return False
	return removeTask(task_obj.taskid,reallyDelete)

def deleteShotDelivery(shotid):
	try:
		Shotdelivery.objects.filter(shotid=shotid).delete()
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))

@login_required
def delete_shot(request):
	error = False
	reallyDelete = ''
	shotid = request.POST.get('shotid')
	try:
		shot_obj = Shot.objects.get(shotid=shotid)
		enti_obj = Entitytype.objects.get(entitytypeid=shot_obj.type)
		task_obj = Task.objects.get(Q(projectid=shot_obj.projectid) & Q(entitytypeid=enti_obj.entitytypeid))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	try:
		Shotsservice.objects.filter(shotid=shotid).delete()
	except Exception as e:
		error = False
		print '%s (%s)' % (e.message, type(e))
	if not (error):
		try:
			Assets.objects.filter(shotid=shotid).update(shotid=-1)
		except Exception as e:
			error = False
			print '%s (%s)' % (e.message, type(e))
	if not (error):
		try:
			Shotcustomshotfield.objects.filter(shotid=shotid).delete()
		except Exception as e:
			error = False
			print '%s (%s)' % (e.message, type(e))
	if not (error):
		try:
			Bid.objects.filter(shotid=shotid).delete()
		except Exception as e:
			error = False
			print '%s (%s)' % (e.message, type(e))
	if not (error):
		try:
			Shot.objects.filter(shotid=shotid).delete()
			reallyDelete = True
		except Exception as e:
			error = False
			print '%s (%s)' % (e.message, type(e))
	taskDeleted = removeAutoTask(enti_obj.entitytypeid,task_obj.entityid,shot_obj.shotid,reallyDelete)
	deleteShotDelivery(shotid)
	if not (error) and not(taskDeleted):
		return render_to_response('deleteshot_success.html')
	else:
		return render_to_response('deleteshot_error.html')

##########################################################
# Theses steps adds a shot to the table Shot along with  #
# all the other that are related to the table Shot       #
##########################################################

@login_required
def new_shot(request):
	c = {}
	c.update(csrf(request))
	c['proj_obj'] = proj_obj
	return render_to_response('newshot.html',c)

def addAutoTask(projectid,taskname,entitytypeid,entityid,taskParentID,duration,Isactive):
	taskID = -1
	if (duration == '') or (duration <= 0):
		duration = 1
	if taskname == '':
		taskname = getTaskEntityNameFromEntityTypeAndEntityID(entitytypeid,entityid)
	position = getLastTaskForProject(projectid) + 1
	try:
		next_task_id = Task.objects.all().aggregate(Max('taskid'))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	next_task_id = next_task_id['taskid__max']
	next_task_id += 1
	try:
		NWTK = Task()
		NWTK.taskid = next_task_id
		NWTK.taskname = taskname
		NWTK.entitytypeid = entitytypeid
		NWTK.entityid = entityid
		NWTK.parentid = taskParentID
		NWTK.taskstatusid = 0
		NWTK.offset = 0
		NWTK.offsettypeid = 1
		NWTK.duration = duration
		NWTK.notes = ''
		NWTK.projectid = projectid
		NWTK.position = position
		NWTK.hidden = 0
		NWTK.bakedstartdate = ''
		NWTK.bakedenddate = ''
		NWTK.originalstartdate = ''
		NWTK.originalenddate = ''
		NWTK.idledays = 0
		NWTK.isclone = 0
		NWTK.isactive = int(prepareSQLString(str(Isactive)))
		NWTK.save()
		taskID = next_task_id
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))

def addAutoTaskWithParentEntityID(projectid,taskname,entitytypeid,entityid,parentid,duration):
	taskid = -1
	error = False
	alreadyExists = False
	try:
		task_obj = Task.objects.get(Q(entitytypeid=entitytypeid) & Q(entityid=entityid))
	except Exception as e:
		error = True
		print '%s (%s)' % (e.message, type(e))
	if task_obj != None:
		error = True
		alreadyExists = True
	if (not error) and (not alreadyExists):
		parentTypeID = ''
		pid = parentid
		active = 1
		if entitytypeid == task_entity_types['ENTITY_TYPE_PROJECT']:
			parentTypeID = 0
		elif entitytypeid == task_entity_types['ENTITY_TYPE_MILESTONE']:
			parentTypeID = task_entity_types['ENTITY_TYPE_MILESTONE']
		elif entitytypeid == task_entity_types['ENTITY_TYPE_SHOT']:
			try:
				shot_obj = Shot.objects.filter(shotid=entityid).values('sequenceid','active')
			except Exception as e:
				print '%s (%s)' % (e.message, type(e))
			if shot_obj != None:
				if shot_obj[0]['sequenceid'] == 0:
					parentTypeID = task_entity_types['ENTITY_TYPE_PROJECT']
					pid = projectid
				else:
					parentTypeID = task_entity_types['ENTITY_TYPE_SEQUENCE']
				if shot_obj[0]['active'] == 0:
					active = 0
		elif entitytypeid == task_entity_types['ENTITY_TYPE_SEQUENCE']:
			parentTypeID = task_entity_types['ENTITY_TYPE_PROJECT']
		elif entitytypeid == task_entity_types['ENTITY_TYPE_BID']:
			parentTypeID = task_entity_types['ENTITY_TYPE_SHOT']
		elif entitytypeid == task_entity_types['ENTITY_TYPE_SERVICE']:
			parentTypeID = task_entity_types['ENTITY_TYPE_BID']
		else:
			parentTypeID = 0
		realParentID = 0
		if (pid != 0) and (pid != -1):
			realParentID = getTaskIDFromEntityTypeAndEntityID(parentTypeID,pid)
		if realParentID == -1:
			realParentID = 0
		if (duration == '') or (duration < 0):
			duration = 1
		return addAutoTask(projectid,taskname,entitytypeid,entityid,realParentID,duration,active)
	return -1

def versionExist(shotid,major,minor,external,view,task):
	try:
		version_exist = Version.objects.get(Q(shotid=shotid) & Q(major=major) & Q(minor=minor) & Q(external=external) & Q(view=view) & Q(task=task))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	if version_exist == None:
		return False
	else:
		return True

def newVersion(shotid,major,minor,external,notes,tags,view,task):
	error = False
	versionID = -1
	creationDate = datetime.date.today()
	extPad = '000'
	majPad = '000'
	minPad = '00'

	if len(external) == 1:
		extPad = extPad[0:2] + external
	elif len(external) == 2:
		extPad = extPad[0:1] + external
	else:
		extPad = external

	if len(major) == 1:
		majPad = majPad[0:2] + major
	elif len(major) == 2:
		majPad = majPad[0:1] + major
	else:
		majPad = major

	if len(minor) == 1:
		minPad = minPad[0:1] + minor
	else:
		minPad = minor

	user = request.user
	if not versionExist(shotid,majPad,minPad,extPad,view,task):
		try:
			next_version_id = Version.objects.all().aggregate(Max('versionid'))
		except Exception as e:
			error = True
			print '%s (%s)' % (e.message, type(e))
		print next_version_id
		if error:
			return versionID
		else:
			versionID = next_version_id['versionid__max']
			versionID += 1
		try:
			NV = Version()
			NV.versionid = versionID
			NV.shotid = shotid
			NV.major = prepareSQLString(majPad)
			NV.minor = prepareSQLString(minPad)
			NV.external = prepareSQLString(extPad)
			NV.notes = prepareSQLString(notes)
			NV.tags = prepareSQLString(tags)
			NV.creationdate = prepareSQLString(creationDate)
			NV.view = prepareSQLString(view)
			NV.task = prepareSQLString(task)
			NV.publishedby = prepareSQLString(user.username)
			NV.save()
		except Exception as e:
			error = False
			print '%s (%s)' % (e.message, type(e))
		if error:
			versionID = -1
			return versionID
		else:
			return versionID
	else:
		return versionID

@login_required
def add_shot(request):
	error = False
	projectid = request.POST.get('projectid')
	try:
		next_shot_id = Shot.objects.all().aggregate(Max('shotid'))
	except Exception as e:
		error = False
		print '%s (%s)' % (e.message, type(e))
	print next_shot_id
	next_shot_id = next_shot_id['shotid__max']
	next_shot_id += 1
	try:
		NWST = Shot()
		NWST.shotid = next_shot_id
		NWST.vfxid = ''
		NWST.externalid = ''
		NWST.shotname = 'NewShot'
		NWST.location = ''
		NWST.cameramotion = ''
		NWST.scenenumber = ''
		NWST.pagenumber = ''
		NWST.frames = 0
		NWST.sequenceid = 0
		NWST.projectid = projectid
		NWST.directornotes = ''
		NWST.shotdescription = ''
		NWST.thumbnail = ''
		NWST.status = 0
		NWST.imageassetid = 0
		NWST.addconsumablesallowance = '1'
		NWST.workedby = ''
		NWST.type = 0
		NWST.lens = ''
		NWST.primarybidnumber = 0
		NWST.vfxtasks = ''
		NWST.isreference = 0
		NWST.sortindex = -1
		NWST.take = 0
		NWST.active = 1
		NWST.save()
	except Exception as e:
		error = False
		print '%s (%s)' % (e.message, type(e))
	if not (error):
		# return render_to_response('addshot_success.html')
		# shotid = getLastInsertID()
		try:
			last_shot_id = Shot.objects.all().aggregate(Max('shotid'))
			addAutoTaskWithParentEntityID(projectid,'',task_entity_types['ENTITY_TYPE_SHOT'],last_shot_id['shotid__max'],projectid,0)
			res = newVersion(last_shot_id['shotid__max'],'000','01','0','main','','','')
			if (res != '-1') or (res != ''):
			# 	NewShotCreated = True
				return render_to_response('addshot_success.html')
			else:
			# 	NewShotCreated = False
				return render_to_response('addshot_error.html')
		except Exception as e:
			print '%s (%s)' % (e.message, type(e))
	else:
		NewShotCreated = False
		return render_to_response('addshot_error.html')

##########################################################
# Theses steps searchs for matches in the table Assets   #
# with parameters such as condition, attribute, projectid#
# using tables ProjectUser and Comments                  #
##########################################################

@login_required
def find_matches(request):
	c = {}
	c.update(csrf(request))
	c['proj_obj'] = proj_obj
	c['shot_obj'] = shot_obj
	return render_to_response('findmatches.html',c)

@login_required
def search_matches(request):
	c = {}
	c.update(csrf(request))
	matches = []
	total = 0
	showing = 0
	# user = request.user
	# args = Q()
	# kwargs = {}
	# cargs = Q()
	# ckwargs = {}
	searchfor = request.POST.get('searchfor')
	condition = request.POST.get('condition')
	attribute = request.POST.get('attribute')
	projectid = int(request.POST.get('projectid'))
	shotid = int(request.POST.get('shotid'))
	fromwhere = int(request.POST.get('fromwhere'))
	howmany = int(request.POST.get('howmany',-1))
	searchParameter = searchfor
	testParameter = ''
	lookingForComments = False
	if attribute == 'File Name':
		testParameter = 'AssetName'
	elif attribute == 'ID':
		testParameter = 'AssetID'
	elif attribute == 'Access':
		testParameter = 'Public'
		searchParameter = str(stringToPermissions(searchfor))
	elif attribute == 'Uploader':
		testParameter = 'uploader'
	elif attribute == 'Upload Date':
		testParameter = 'uploadDate'
	elif attribute == 'Last Modified':
		testParameter = 'TypeID'
		searchParameter = getAssetTypeFromString(searchfor)
	elif attribute == 'Size':
		testParameter = 'Size'
	elif attribute == 'Tags':
		testParameter = 'tags'
	elif attribute == 'Comment Text':
		lookingForComments = True
		testParameter = 'comment'
	elif attribute == 'Comment By':
		lookingForComments = True
		testParameter = 'userID'
	elif attribute == 'Comment Date':
		lookingForComments = True
		testParameter = 'Date'
	testOperator = ''
	matchAtStart = False
	matchAtEnd = False
	if (condition == 'is') or (condition == 'equals'):
		testOperator = '='
	elif condition == 'is less than':
		testOperator = '<'
	elif condition == 'is greater than':
		testOperator = '>'
	elif condition == 'is not':
		testOperator = '<>'
	elif condition == 'contains':
		matchAtStart = True
		matchAtEnd = True
		testOperator = 'LIKE'
	elif condition == 'does not contain':
		matchAtStart = True
		matchAtEnd = True
		testOperator = 'NOT LIKE'
	elif condition == 'starts with':
		matchAtStart = True
		testOperator = 'LIKE'
	elif condition == 'ends with':
		matchAtEnd = True
		testOperator = 'LIKE'
	sql1 = ''
	sqlCount1 = ''
	sql1 = 'SELECT * FROM '
	sqlCount1 = 'SELECT * FROM '
	if not lookingForComments:
		sql1 += 'Assets WHERE '
		sqlCount1 += 'Assets WHERE '
		if projectid != -1:
			# args.add(Q(projectid=projectid),Q.AND)
			# cargs.add(Q(projectid=Count(projectid)),Q.AND)
			sql1 += 'ProjectID = %s AND ' % projectid
			sqlCount1 += 'ProjectID = %s AND ' % projectid
			print 'OVER HERE 1!!!!!!!!!!!!!'
			print sql1
			print sqlCount1
			print '-----------------------------------------------------------------------------------------'
		else:
			# search = Projectuser.objects.filter(userid=user.userid).values_list('projectid')
			# args.add(Q(projectid__in=search),Q.AND)
			# cargs.add(Q(projectid__in=Count(search)),Q.AND)
			userid = "'ndelagarza'"
			# tmp_q = Projectuser.objects.raw('SELECT projectid FROM Projectuser WHERE userid = %s', [userid])
			sql1 += 'Assets.ProjectID IN ( SELECT ProjectID FROM ProjectUser WHERE UserID = %s ) AND ' % userid
			sqlCount1 += 'Assets.ProjectID IN ( SELECT ProjectID FROM ProjectUser WHERE UserID = %s ) AND ' % userid
			print 'OVER HERE 2!!!!!!!!!!!!!'
			print sql1
			print sqlCount1
			print '-----------------------------------------------------------------------------------------'
	else:
		if projectid != -1:
			# args.add(Q(projectid=projectid),Q.AND)
			# cargs.add(Q(projectid=Count(projectid)),Q.AND)
			# search = Comment.objects.values_list('entityid')
			# args.add(Q(assetid__in=search),Q.AND)
			# cargs.add(Q(assetid__in=Count(search)),Q.AND)
			sql1 += 'Assets, Comment WHERE Assets.ProjectID = %s AND Assets.AssetID = Comment.EntityID AND ' % projectid
			sqlCount1 += 'Assets, Comment WHERE Assets.ProjectID = %s AND Assets.AssetID = Comment.EntityID AND ' % projectid
			print 'NO, ITS HERE 1!!!!!!!!!!!!!'
			print sql1
			print sqlCount1
			print '-----------------------------------------------------------------------------------------'
		else:
			# search = Projectuser.objects.filter(userid=user.userid).values_list('projectid')
			# args.add(Q(projectid__in=search),Q.AND)
			# cargs.add(Q(projectid__in=Count(search)),Q.AND)
			# tmp_q = Projectuser.objects.raw('SELECT projectid FROM Projectuser WHERE userid = %s', [userid])
			userid = "'ndelagarza'"
			sql1 += 'Assets, Comment WHERE Assets.ProjectID IN ( SELECT ProjectID FROM ProjectUser WHERE UserID = %s ) AND Assets.AssetID = Comment.EntityID AND ' % userid
			sqlCount1 += 'Assets, Comment WHERE Assets.ProjectID IN ( SELECT ProjectID FROM ProjectUser WHERE UserID = %s ) AND Assets.AssetID = Comment.EntityID AND ' % userid
			print 'NO, ITS HERE 2!!!!!!!!!!!!!'
			print sql1
			print sqlCount1
			print '-----------------------------------------------------------------------------------------'
	sql1 += testParameter + ' ' + testOperator
	sqlCount1 += testParameter + ' ' + testOperator
	print 'testParameter AND testOperator ADDED!!!!!!!!'
	print sql1
	print sqlCount1
	print '-----------------------------------------------------------------------------------------'
	# searchParameter = prepareSQLString(searchParameter)
	# if testOperator == '=':
	# 	kw = '%s__iexact' % testParameter
	# 	kwargs = {kw:searchParameter}
	# 	ckwargs = {kw:models.Count(searchParameter)}
	# elif testOperator == '<':
	# 	kw = '%s__lt' % testParameter
	# 	kwargs = {kw:searchParameter}
	# 	ckwargs = {kw:models.Count(searchParameter)}
	# elif testOperator == '>':
	# 	kw = '%s__gt' % testParameter
	# 	kwargs = {kw:searchParameter}
	# 	ckwargs = {kw:models.Count(searchParameter)}
	# elif testOperator == '!=':
	# 	kw = '%s' % testParameter
	# 	kwargs = {kw:searchParameter}
	# 	ckwargs = {kw:models.Count(searchParameter)}
	# 	iargs = {}
		# kw = Assets.objects.exclude(*iargs,**kwargs)
		# ckw = Assets.objects.exclude(*iargs,**ckwargs)
	# 	args.add(Assets.objects.exclude(*iargs,**kwargs),Q.AND)
	# 	cargs.add(Assets.objects.exclude(*iargs,**ckwargs),Q.AND)
	# elif testOperator == 'like':
	# 	kw = '%s__icontains' % testParameter
	# 	kwargs = {kw:searchParameter}
	# 	ckwargs = {kw:models.Count(searchParameter)}
	# elif testOperator == 'not like':
	# 	kw = '%s__icontains' % testParameter
	# 	kwargs = {kw:searchParameter}
	# 	ckwargs = {kw:models.Count(searchParameter)}
	# 	iargs = {}
		# kw = Assets.objects.exclude(*iargs,**kwargs)
		# ckw = Assets.objects.exclude(*iargs,**ckwargs)
	# 	args.add(Assets.objects.exclude(*iargs,**kwargs),Q.AND)
	# 	cargs.add(Assets.objects.exclude(*iargs,**ckwargs),Q.AND)
	# elif testOperator == 'starts with':
	# 	kw = '%s__startswith' % testParameter
	# 	kwargs = {kw:searchParameter}
	# 	ckwargs = {kw:models.Count(searchParameter)}
	# elif testOperator == 'ends with':
	# 	kw = '%s__endswith' % testParameter
	# 	kwargs = {kw:searchParameter}
	# 	ckwargs = {kw:models.Count(searchParameter)}
	sql2 = ''
	sqlCount2 = ''
	if int(shotid) > 0:
		# cargs.add(Q(shotid=Count(shotid)),Q.AND)
		sql2 += 'AND ShotID = %s ' % shotid
		sqlCount2 += 'AND ShotID = %s ' % shotid
		print 'SHOTID ADDED!!!!!'
		print sql2
		print sqlCount2
		print '-----------------------------------------------------------------------------------------'
	returnAllMatches = False
	if howmany == -1:
		returnAllMatches = True
	if not returnAllMatches:
		# ut = Usertypes.objects.get(usertype=user.usertype)
		ut = Usertypes.objects.get(usertype=1)
		if (ut.typename == 'Administrator') or (ut.typename == 'Capturer'):
			# shid = Assets.objects.filter(shotid=shotid).order_by('shotid')[fromwhere:howmany+fromwhere]
			# args.add(shid,Q.AND)
			sql2 += 'LIMIT %s,%s' % (str(fromwhere),str(howmany))
			print 'OVER HERE 1!!!!!'
			print sql2
			print '-----------------------------------------------------------------------------------------'
		else:
			# if int(shotid) > 0:
			# 	args.add(Q(shotid=shotid),Q.AND)
			# lst = getPermissionsListForUserType(ut)
			# args.add(Assets.objects.filter(public__in=lst).order_by('shotid')[fromwhere:howmany+fromwhere],Q.AND)
			# cargs.add(Q(public__in=Count(lst)),Q.AND)
			lst = getPermissionsListForUserType(ut)
			sql2 += 'AND Assets.Public IN ( %s ) LIMIT %s,%s' % (lst,str(fromwhere),str(howmany))
			sqlCount2 += 'AND Assets.Public IN ( %s )' % lst
			print 'OVER HERE 2!!!!!'
			print sql2
			print sqlCount2
			print '-----------------------------------------------------------------------------------------'
	else:
		# if int(shotid) > 0:
		# 	args.add(Q(shotid=shotid),Q.AND)
		ut = Usertypes.objects.get(usertype=1)
		if (ut.typename != 'Administrator') and (ut.typename != 'Capturer'):
			# lst = getPermissionsListForUserType(ut)
			# args.add(Q(public__in=lst),Q.AND)
			# cargs.add(Q(public__in=Count(lst)),Q.AND)
			lst = getPermissionsListForUserType(ut)
			sql2 += 'AND Assets.Public IN ( %s )' % lst
			sqlCount2 += 'AND Assets.Public IN ( %s )' % lst
			print 'MAYBE HERE!!!!!!!!'
			print sql2
			print sqlCount2
			print '-----------------------------------------------------------------------------------------'
	# print 'SQL NORMAL!!!!!!!!!!'
	# print 'ARGS is %s' % args
	# print type(args)
	# print 'KWARGS is %s' % kwargs
	# print type(kwargs)
	# kw = {}
	# print 'SQL_COUNT NORMAL!!!!!!!!!!'
	# print 'CARGS is %s' % cargs
	# print type(cargs)
	# print 'CKWARGS is %s' % ckwargs
	# print type(ckwargs)
	# ckw = {}
	# print 'RAW SQL'
	# pids = 103
	# sqlraw = 'SELECT * FROM Assets WHERE projectid = %s' % pids
	# ans = Assets.objects.raw(sqlraw)
	# for i in ans:
	# 	print i.projectid

	# sql_args = Assets.objects.filter(*[args],**kw)
	# sqlCount_cargs = Assets.objects.annotate(*[cargs],**kw)

	# sql_kwargs = Assets.objects.filter(*[args],**ckw)
	# sqlCount_ckwargs = Assets.objects.annotate(*[cargs],**ckw)
	print '-----------------------------------------------------------------------------------------'
	sql = ''
	sqlCount = ''
	if matchAtEnd and matchAtStart:
		try:
			sql = Assets.objects.raw(sql1 + ' %s ' + sql2, ["%" + prepareSQLString(searchParameter) + "%"])
			sqlCount = Assets.objects.raw(sqlCount1 + ' %s ' + sqlCount2, ["%" + prepareSQLString(searchParameter) + "%"])
		except Exception as e:
			print '%s (%s)' % (e.message, type(e))
		print '-----------------------------------------------------------------------------------------'
		print sql
		print sqlCount
		print '-----------------------------------------------------------------------------------------'
	elif matchAtEnd:
		try:
			sql = Assets.objects.raw(sql1 + ' %s ' + sql2, ["%" + prepareSQLString(searchParameter)])
			sqlCount = Assets.objects.raw(sqlCount1 + ' %s ' + sqlCount2, ["%" + prepareSQLString(searchParameter)])
		except Exception as e:
			print '%s (%s)' % (e.message, type(e))
		print '-----------------------------------------------------------------------------------------'
		print sql
		print sqlCount
		print '-----------------------------------------------------------------------------------------'
	elif matchAtStart:
		try:
			sql = Assets.objects.raw(sql1 + ' %s ' + sql2, [prepareSQLString(searchParameter) + "%"])
			sqlCount = Assets.objects.raw(sqlCount1 + ' %s ' + sqlCount2, [prepareSQLString(searchParameter) + "%"])
		except Exception as e:
			print '%s (%s)' % (e.message, type(e))
		print '-----------------------------------------------------------------------------------------'
		print sql
		print sqlCount
		print '-----------------------------------------------------------------------------------------'
	else:
		try:
			sql = Assets.objects.raw(sql1 + ' %s ' + sql2, [prepareSQLString(searchParameter)])
			sqlCount = Assets.objects.raw(sqlCount1 + ' %s ' + sqlCount2, [prepareSQLString(searchParameter)])
		except Exception as e:
			print '%s (%s)' % (e.message, type(e))
		print '-----------------------------------------------------------------------------------------'
		print sql
		print sqlCount
		print '-----------------------------------------------------------------------------------------'
	print 'FINAL RAW QUERY!!!!!!!!!!!!'
	print 'SQL %s' % sql
	print 'SQLCOUNT %s' % sqlCount
	print 'FINAL ANSWER IS!!!!!!!!!!!!'
	for i in sql:
		matches.append(i)
		print i
	total = len(list(sqlCount))
	showing = howmany
	print 'Matches %s' % matches
	print 'Total %i' % total
	print 'Showing %i' % showing
	# print sql_args
	# print sqlCount_cargs
	# print sql_kwargs
	# print sqlCount_ckwargs
	c['matches'] = matches
	c['total'] = total
	c['showing'] = showing
	return render_to_response('findmatches_success.html',c)

##########################################################
# Method assign's image to shot                          #
##########################################################

@login_required
def main_image_assign_shot(request):
	c = {}
	c.update(csrf(request))
	c['asse_obj'] = asse_obj
	c['shot_obj'] = shot_obj
	return render_to_response('imageshotmain.html',c)

@login_required
def assign_Image_To_shot(request):
	assetid = int(request.POST.get('assetid'))
	shotid = int(request.POST.get('shotid'))
	try:
		Shot.objects.filter(shotid=shotid).update(imageassetid=assetid)
	except Exception as e:
		error = True
		print '%s (%s)' % (e.message, type(e))