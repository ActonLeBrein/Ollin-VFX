 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import os
import sys
import csv
from django.shortcuts import render_to_response, redirect, render
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from ollinvfx.models import *
from django.core import serializers
from django.db.models import Q
import simplejson
import datetime
import pytz

csv.field_size_limit(sys.maxsize)

# Create your views here.

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

def upload_usertype(request):
	path = get_file_path('UserTypes.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[1] != 'TypeName':
				Is_UT = UserTypes.objects.filter(TypeName = row[1])
				if len(Is_UT) == 0:
					print row
					try:
						UT = UserTypes()
						UT.TypeName = row[1]
						UT.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading user types'
	#return res

def upload_user(request):
	path = get_file_path('User.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'UserID':
				Is_U = User.objects.filter(username = row[0], first_name = row[3], last_name = row[4], email = row[5])
				if len(Is_U) == 0:
					print row
					try:
						U = User()
						U.username = row[0]
						U.password = row[1]
						U.first_name = row[3]
						U.last_name = row[4]
						U.email = row[5]
						U.save()
						try:
							UP = UserProfile()
							new_user = User.objects.get(username = row[0])
							UP.user_id = new_user.id
							UP.UserType_ID_id = int(row[2])
							UP.IsGroup = row[6]
							UP.save()
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save'
							#return res
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading users'
	#return res

def upload_accesscontrolfingerprint(request):
	path = get_file_path('AccessControlFingerprint.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'EnrollID':
				Is_ACF = AccessControlFingerprint.objects.filter(EnrollID = row[0])
				if len(Is_ACF) == 0:
					print row
					try:
						ACF = AccessControlFingerprint()
						ACF.EnrollID = row[0]
						ACF.Finger = row[1]
						ACF.Fingerprint = row[2]
						ACF.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading access control fingerprints'
	#return res

def upload_status(request):
	path = get_file_path('Status.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[1] != 'StatusName':
				Is_S = Status.objects.filter(StatusName = row[1])
				if len(Is_S) == 0:
					print row
					try:
						S = Status()
						S.StatusID = row[0]
						S.StatusName = row[1]
						S.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading status'
	#return res

def upload_accesscontrollog(request):
	path = get_file_path('AccessControlLog.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[1] != 'EventID':
				Is_ACL = AccessControlLog.objects.filter(EventID = row[1])
				if len(Is_ACL) == 0:
					print row
					try:
						ACL = AccessControlLog()
						ACL.EventID = str(row[1])
						ACL.Date = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
						ACL.EnrollID = row[3]
						ACL.Period = row[4]
						ACL.Method = row[5]
						ACL.OverrideAction = row[6]
						ACL.Status_ID_id = row[7]
						ACL.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading access control log'
	#return res

def upload_loginattempt(request):
	path = get_file_path('LoginAttempt.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'UserID':
				try:
					print row
					try:
						LA = LoginAttempt()
						LA.Attempts = row[1]
						LA.LastAttempt = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
						att_user = User.objects.get(username = str(row[0]))
						LA.User_ID_id = att_user.id
						LA.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				except:
					pass
			else:
				pass
	print 'finish uploading login attempts'
	#return res

def upload_usergroup(request):
	path = get_file_path('UserGroup.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[1] != 'UserID':
				try:
					Is_UG = UserGroup.objects.filter(GroupID = row[0])
					if len(Is_UG) == 0:
						print row
						try:
							UG = UserGroup()
							UG.GroupID = row[0]
							UG.save()
							user_group = User.objects.get(username = row[1])
							UG.User_ID.add(user_group.id)
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save %s 1' % row[1]
							#return res
					else:
						print 'in table'
						try:
							UG = UserGroup.objects.get(GroupID = row[0])
							user_group = User.objects.get(username = row[1])
							UG.User_ID.add(user_group.id)
							UG.save()
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save %s 2' % row[1]
							#return res
				except:
					pass
			else:
				pass
	print 'finish uploading user groups'
	#return res

def upload_evaluationround(request):
	path = get_file_path('EvaluationRound.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'EvaluationRoundID':
				try:
					Is_ER = EvaluationRound.objects.filter(EvaluationRoundID = row[0])
					if len(Is_ER) == 0:
						print row
						try:
							ER = EvaluationRound()
							ER.EvaluationRoundID = row[0]
							ER.Date = datetime.datetime.strptime(row[1], "%Y-%m-%d")
							ER.save()
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save'
							#return res
					else:
						pass
				except:
					pass
			else:
				pass
	print 'finish uploading evaluation rounds'
	#return res

def upload_evaluation(request):
	path = get_file_path('Evaluation.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[1] != 'EvaluationID':
				try:
					Is_E = Evaluation.objects.filter(EvaluationID = row[0])
					if len(Is_E) == 0:
						print row
						try:
							E = Evaluation()
							E.EvaluationID = row[0]
							E.Technical = row[4]
							E.TechnicalNotes = row[5]
							E.Professional = row[6]
							E.ProfessionalNotes = row[7]
							E.Teamwork = row[8]
							E.TeamworkNotes = row[9]
							E.ForceEval = row[10]
							E.EvalApplied = row[11]
							E.EvaluationDate = datetime.datetime.strptime(row[12], "%Y-%m-%d %H:%M:%S")
							E.CurrentBoss = row[13]
							user_evaled = UserProfile.objects.get(id = row[2])
							E.Evaluated = user_evaled
							user_evalor = UserProfile.objects.get(id = row[3])
							E.Evaluator = user_evalor
							evalround_id = EvaluationRound.objects.get(EvaluationRoundID = row[1])
							E.EvaluationRound_ID = evalround_id
							E.save()
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save %s' % row[0]
							#return res
					else:
						pass
				except:
					pass
			else:
				pass
	print 'finish uploading evaluations'
	#return res

def upload_entitytype(request):
	path = get_file_path('EntityType.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[1] != 'EntityName':
				Is_ET = EntityType.objects.filter(EntityName = row[1])
				if len(Is_ET) == 0:
					print row
					try:
						ET = EntityType()
						ET.EntityTypeID = row[0]
						ET.EntityName = row[1]
						ET.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading entity types'
	#return res

def upload_comment(request):
	path = get_file_path('Comment.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'CommentID':
				try:
					Is_C = Comment.objects.filter(id = row[0])
					if len(Is_C) == 0:
						print row
						try:
							C = Comment()
							C.Date = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
							C.Comments = row[3]
							C.EntityID = row[5]
							user_comment = User.objects.get(username = row[1])
							up_comment = UserProfile.objects.get(user = user_comment.id)
							C.User_ID = up_comment
							entity_type = EntityType.objects.get(id = row[4])
							C.EntityType_ID = entity_type
							C.save()
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save %s' % row[0]
							#return res
					else:
						pass
				except:
					pass
			else:
				pass
	print 'finish uploading comments'
	#return res

def upload_alarm(request):
	path = get_file_path('Alarm.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'AlarmID':
				try:
					Is_A = Alarm.objects.filter(AlarmID = row[0])
					if len(Is_A) == 0:
						print row
						try:
							A = Alarm()
							A.AlarmID = row[0]
							if len(row[3]) == 10:
								A.Due = datetime.datetime.strptime(row[3], "%Y-%m-%d")
							else:
								A.Due = datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
							A.What = row[4]
							A.Action_ID = row[6]
							A.Mode = row[7]
							if len(row[8]) > 0:
								A.LastFired = datetime.datetime.strptime(row[8], "%Y-%m-%d %H:%M:%S")
							A.EntityID = row[2]
							entity_type = EntityType.objects.get(EntityTypeID = row[1])
							A.EntityType_ID = entity_type
							status_alarm = Status.objects.get(StatusID = row[5])
							A.Status_ID = status_alarm
							A.save()
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save %s' % row[0]
							print row[3]
							print row[8]
							#return res
					else:
						pass
				except:
					pass
			else:
				pass
	print 'finish uploading alarms'
	#return res

def upload_alarmreminder(request):
	path = get_file_path('AlarmReminder.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'AlarmReminderID':
				try:
					Is_AR = Alarm.objects.filter(AlarmID = row[0])
					if len(Is_AR) == 0:
						print row
						try:
							AR = AlarmReminder()
							AR.AlarmReminderID = row[0]
							AR.DaysBefore = row[2]
							AR.Fired = row[3]
							alarm_id = Alarm.objects.get(AlarmID = row[1])
							AR.Alarm_ID = alarm_id
							AR.save()
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save %s' % row[0]
							#return res
					else:
						pass
				except:
					pass
			else:
				pass
	print 'finish uploading alarm reminders'
	#return res

def upload_alarmactionparameter(request):
	path = get_file_path('AlarmActionParameter.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'AlarmID':
				try:
					Is_AAP = AlarmActionParameter.objects.filter(Alarm_ID = row[0])
					if len(Is_AAP) == 0:
						print row
						try:
							AAP = AlarmActionParameter()
							AAP.Parameter = row[1]
							alarm_id = Alarm.objects.get(AlarmID = row[0])
							AAP.Alarm_ID = alarm_id
							AAP.save()
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save %s' % row[0]
							#return res
					else:
						pass
				except:
					pass
			else:
				pass
	print 'finish uploading alarm action parameters'
	#return res

def upload_commands(request):
	path = get_file_path('Commands.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'CommandName':
				Is_C = Commands.objects.filter(CommandName = row[0])
				if len(Is_C) == 0:
					print row
					try:
						C = Commands()
						C.CommandName = row[0]
						C.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading commands'
	#return res

def upload_priviledgesmatrix(request):
	path = get_file_path('PriviledgesMatrix.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'Command':
				try:
					command_id = Commands.objects.get(CommandName = row[0])
					Is_PM = PriviledgesMatrix.objects.filter(Commands_ID = command_id.id)
					if len(Is_PM) == 0:
						print row
						try:
							PM = PriviledgesMatrix()
							PM.P1 = row[1]
							PM.P2 = row[2]
							PM.P3 = row[3]
							PM.P4 = row[4]
							PM.P5 = row[5]
							PM.P6 = row[6]
							PM.P7 = row[7]
							PM.P8 = row[8]
							command_id = Commands.objects.get(CommandName = row[0])
							PM.Commands_ID = command_id
							PM.save()
						except Exception as e:
							print '%s (%s)' % (e.message, type(e))
							res = False
							print 'could not save %s' % row[0]
							#return res
					else:
						pass
				except:
					pass
			else:
				pass
	print 'finish uploading priviledges matrix'
	#return res

def upload_commandrelations(request):
	path = get_file_path('CommandRelations.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'Command':
				print row
				try:
					CR = CommandRelations()
					command_id = Commands.objects.get(CommandName = row[0])
					CR.Command = command_id
					relatedto_id = Commands.objects.get(CommandName = row[1])
					CR.RelatedTo = relatedto_id
					CR.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading commands relations'
	#return res

def upload_extendedpermissions(request):
	path = get_file_path('ExtendedPermissions.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'Command':
				Is_EP = ExtendedPermissions.objects.filter(User_ID = row[1])
				if len(Is_EP) == 0:
					print row
					try:
						EP = ExtendedPermissions()
						EP.Action = row[2]
						command_id = Commands.objects.get(CommandName = row[0])
						EP.Command_ID = command_id
						user_id = User.objects.get(username = row[1])
						user_id = UserProfile.objects.get(user = user_id.id)
						EP.User_ID = user_id
						EP.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading extended permissions'
	#return res

def upload_notification(request):
	path = get_file_path('Notification.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'NotificationID':
				Is_N = Notification.objects.filter(NotificationID = row[0])
				if len(Is_N) == 0:
					print row
					try:
						N = Notification()
						N.AlreadyRead = row[1]
						N.TypeID = row[3]
						N.From = row[4]
						N.AddressedTo = row[5]
						N.Subject = row[6]
						N.Body = row[7]
						N.BodyHTML = row[8]
						N.DateTime = datetime.datetime.strptime(row[9], "%Y-%m-%d %H:%M:%S")
						status_not = Status.objects.get(StatusID = row[2])
						N.Status_ID = status_not
						N.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading notifications'
	#return res

def upload_notificationmetadata(request):
	path = get_file_path('NotificationMetadata.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ID':
				Is_NM = NotificationMetadata.objects.filter(ID = row[0])
				if len(Is_NM) == 0:
					print row
					try:
						NM = NotificationMetadata()
						NM.MetadataName = row[2]
						NM.MetadataValue = row[3]
						notification_id = Notification.objects.get(NotificationID = row[1])
						NM.Notification_ID = notification_id
						NM.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading notification metadatas'
	#return res

def upload_project(request):
	path = get_file_path('Project.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ProjectID':
				Is_P = Project.objects.filter(ProjectID = row[0])
				if len(Is_P) == 0:
					print row
					try:
						P = Project()
						P.ProjectID = row[0]
						P.ProjectName = row[1]
						P.ProjectNickname = row[2]
						P.Director = row[3]
						P.Producer = row[4]
						P.Studio = row[5]
						P.ConsumableAllowance = row[6]
						P.Contingency = row[7]
						if not row[8] == 'NULL':
							P.Thumbnail = row[8]
						if not row[9] == 'NULL':
							P.ImageAssetID = row[9]
						P.OldStructure = row[10]
						P.Active = row[11]
						if not row[12] == 'NULL':
							P.CreationDate = datetime.datetime.strptime(row[12], "%Y-%m-%d %H:%M:%S")
						P.RestrictShotsToAssignedUsers = row[13]
						if not (row[14] == 'NULL' or len(row[14]) == 0):
							P.StartDate = datetime.datetime.strptime(row[14], "%Y-%m-%d")
						P.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading projects'
	#return res

def upload_milestone(request):
	path = get_file_path('Milestone.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'MilestoneID':
				Is_M = Milestone.objects.filter(MilestoneID = row[0])
				if len(Is_M) == 0:
					print row
					try:
						M = Milestone()
						M.MilestoneID = row[0]
						M.Name = row[3]
						if not len(row[1]) == 0:
							M.Date = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
						project_id = Project.objects.get(ProjectID = row[2])
						M.Project_ID = project_id
						M.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading milestoness'
	#return res

def upload_incomingfile(request):
	path = get_file_path('IncomingFile.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'IncomingFileID':
				Is_IF = IncomingFile.objects.filter(IncomingFileID = row[0])
				if len(Is_IF) == 0:
					print row
					try:
						IF = IncomingFile()
						IF.IncomingFileID = row[0]
						if not len(row[2]) == 0:
							IF.Date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
						IF.Sender = row[3]
						IF.AddressedTo = row[4]
						IF.SourcePath = row[5]
						IF.FinalPath = row[6]
						IF.Description = row[7]
						IF.Tags = row[8]
						IF.Area = row[9]
						IF.Media = row[10]
						project_id = Project.objects.get(ProjectID = row[1])
						IF.Project_ID = project_id
						IF.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading incomingfiles'
	#return res

def upload_projectuser(request):
	path = get_file_path('ProjectUser.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'UserID':
				try:
					print row
					PU = ProjectUser()
					project_id = Project.objects.get(ProjectID = row[1])
					PU.Project_ID = project_id
					user_id = User.objects.get(username = row[0])
					user_id = UserProfile.objects.get(user = user_id.id)
					PU.User_ID = user_id
					PU.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading project users'
	#return res

def upload_playlist(request):
	path = get_file_path('Playlist.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'PlaylistID':
				Is_PL = Playlist.objects.filter(PlaylistID = row[0])
				if len(Is_PL) == 0:
					print row
					try:
						PL = Playlist()
						PL.PlaylistID = row[0]
						PL.PlaylistName = row[2]
						if not len(row[3]) == 0:
							PL.PlaylistXML = row[3]
						if not len(row[4]) == 0:
							PL.AutoUpdate = row[4]
						project_id = Project.objects.get(ProjectID = row[1])
						PL.Project_ID = project_id
						PL.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading playlists'
	#return res

def upload_rateset(request):
	path = get_file_path('RateSet.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'RateSetID':
				Is_RS = RateSet.objects.filter(RateSetID = row[0])
				if len(Is_RS) == 0:
					print row
					try:
						RS = RateSet()
						RS.RateSetID = row[0]
						RS.RateSetNumber = row[2]
						RS.RateSetName = row[3]
						if not len(row[4]) == 0:
							RS.RateSetNotes = row[4]
						RS.RateSetCreationDate = datetime.datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S")
						RS.RateSetLastModification = datetime.datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S")
						RS.RateSetConsumableAllowance = row[7]
						RS.RateSetContingency = row[8]
						RS.RateSetExtra = row[9]
						if not (len(row[10]) == 0 or row[10] == 'NULL'):
							RS.RateSetExtraIT = row[10]
						project_id = Project.objects.get(ProjectID = row[1])
						RS.Project_ID = project_id
						RS.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading ratesets'
	#return res

def upload_harddiskstatus(request):
	path = get_file_path('HardDiskStatus.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'HardDiskStatusID':
				Is_HDS = HardDiskStatus.objects.filter(HardDiskStatusID = row[0])
				if len(Is_HDS) == 0:
					print row
					try:
						HDS = HardDiskStatus()
						HDS.HardDiskStatusID = row[0]
						HDS.HardDiskStatusName = row[1]
						HDS.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading hard disk status'
	#return res

def upload_harddiskregister(request):
	path = get_file_path('HardDiskRegister.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'HardDiskRegisterID':
				Is_HDR = HardDiskRegister.objects.filter(HardDiskRegisterID = row[0])
				if len(Is_HDR) == 0:
					print row
					try:
						HDR = HardDiskRegister()
						HDR.HardDiskRegisterID = row[0]
						if not len(row[3]) == 0:
							HDR.SerialNumber = row[3]
						HDR.HardDiskNumber = row[4]
						if not len(row[5]) == 0:
							HDR.HardDiskName = row[5]
						if not len(row[6]) == 0:
							HDR.FromAddress = row[6]
						if not len(row[7]) == 0:
							HDR.ContentOnArrival = row[7]
						if not len(row[8]) == 0:
							HDR.ArrivalDate = datetime.datetime.strptime(row[8], "%Y-%m-%d")
						if not len(row[9]) == 0:
							HDR.ContentOnExit = row[9]
						if not len(row[10]) == 0:
							HDR.ExitDate = datetime.datetime.strptime(row[10], "%Y-%m-%d")
						if not len(row[11]) == 0:
							HDR.Notes = row[11]
						harddiskstatus_id = HardDiskStatus.objects.get(HardDiskStatusID = row[2])
						HDR.HardDiskStatus_ID = harddiskstatus_id
						project_id = Project.objects.get(ProjectID = row[1])
						HDR.Project_ID = project_id
						HDR.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading hard disk registrations'
	#return res

def upload_uploadcontrol(request):
	path = get_file_path('UploadControl.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'UploadControlID':
				Is_UC = UploadControl.objects.filter(UploadControlID = row[0])
				if len(Is_UC) == 0:
					print row
					try:
						UC = UploadControl()
						UC.UploadControlID = row[0]
						if not len(row[3]) == 0:
							UC.Filename = row[3]
						UC.Path = row[4]
						UC.Date = datetime.datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S")
						UC.Password = row[6]
						project_id = Project.objects.get(ProjectID = row[1])
						UC.Project_ID = project_id
						user_id = User.objects.get(username = row[2])
						user_id = UserProfile.objects.get(user = user_id.id)
						UC.User_ID = user_id
						UC.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading upload controls'
	#return res

def upload_storageuse(request):
	path = get_file_path('StorageUse.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[1] != 'ProjectNickname':
				Is_SU = StorageUse.objects.filter(VersionNumber = row[3])
				if len(Is_SU) == 0:
					print row
					try:
						SU = StorageUse()
						SU.ProjectNickname = row[1]
						SU.VFXID = row[2]
						SU.VersionNumber = row[3]
						SU.Size = row[4]
						project_id = Project.objects.get(ProjectNickname = row[1])
						SU.Project_ID = project_id
						user_id = User.objects.get(username = row[0])
						user_id = UserProfile.objects.get(user = user_id.id)
						SU.User_ID = user_id
						SU.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading storage use'
	#return res

def upload_servicetype(request):
	path = get_file_path('ServiceType.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ServiceTypeID':
				Is_ST = ServiceType.objects.filter(ServiceTypeName = row[1])
				if len(Is_ST) == 0:
					print row
					try:
						ST = ServiceType()
						ST.ServiceTypeName = row[1]
						ST.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading service types'
	#return res

def upload_service(request):
	path = get_file_path('Service.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ServiceID':
				Is_S = Service.objects.filter(ServiceName = row[1])
				if len(Is_S) == 0:
					print row
					try:
						S = Service()
						S.ServiceID = row[0]
						S.ServiceName = row[1]
						if not row[2] == 'NULL':
							S.CostPerDay = row[2]
						servicetype_id = ServiceType.objects.get(id = row[3])
						S.ServiceType_ID = servicetype_id
						S.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading services'
	#return res

def upload_servicehistogramcolor(request):
	path = get_file_path('ServiceHistogramColor.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ServiceHistogramColorID':
				Is_SHC = ServiceHistogramColor.objects.filter(ServiceHistogramColorID = row[0])
				if len(Is_SHC) == 0:
					print row
					try:
						SHC = ServiceHistogramColor()
						SHC.ServiceHistogramColorID = row[0]
						SHC.R = row[2]
						SHC.G = row[3]
						SHC.B = row[4]
						service_id = Service.objects.get(ServiceID = row[1])
						SHC.Service_ID = service_id
						SHC.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading service histogram colors'
	#return res

def upload_projectservice(request):
	path = get_file_path('ProjectService.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ProjectServiceID':
				try:
					print row
					PS = ProjectService()
					PS.ProjectServiceID = row[0]
					if not row[3] == 'NULL':
						PS.Rate = row[3]
					PS.RateSetNumber = row[4]
					project_id = Project.objects.get(ProjectID = row[1])
					PS.Project_ID = project_id
					service_id = Service.objects.get(ServiceID = row[2])
					PS.Service_ID = service_id
					PS.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading project services'
	#return res

def upload_projecttaskservice(request):
	path = get_file_path('ProjectTaskService.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ProjectTaskServiceID':
				try:
					print row
					PTS = ProjectTaskService()
					PTS.ProjectTaskServiceID = row[0]
					PTS.Slots = row[3]
					project_id = Project.objects.get(ProjectID = row[1])
					PTS.Project_ID = project_id
					service_id = Service.objects.get(ServiceID = row[2])
					PTS.Service_ID = service_id
					PTS.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading project task services'
	#return res

def upload_assettype(request):
	path = get_file_path('AssetType.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'AssetTypeID':
				Is_AT = AssetType.objects.filter(AssetTypeName = row[1])
				if len(Is_AT) == 0:
					print row
					try:
						AT = AssetType()
						AT.AssetTypeID = row[0]
						AT.AssetTypeName = row[1]
						AT.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading asset types'
	#return res

def upload_sequencialidgenerator(request):
	path = get_file_path('Sequence.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'SequenceID':
				Is_SIG = SequencialIDGenerator.objects.filter(SIG_id = row[0])
				if len(Is_SIG) == 0:
					print row
					try:
						SIG = SequencialIDGenerator()
						SIG.SIG_id = row[0]
						SIG.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save'
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading sequencial id generators'
	#return res

def upload_sequence(request):
	path = get_file_path('Sequence.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'SequenceID':
				Is_S = Sequence.objects.filter(SequencialIDGenerator_ID = row[0])
				if len(Is_S) == 0:
					print row
					try:
						S = Sequence()
						if not len(row[1]) == 0:
							S.SequenceName = row[1]
						if not row[3] == 'NULL':
							S.SequenceNickname = row[3]
						project_id = Project.objects.get(ProjectID = row[2])
						S.Project_ID = project_id
						sequencialidgenerator_id = SequencialIDGenerator.objects.get(SIG_id = row[0])
						S.SequencialIDGenerator_ID = sequencialidgenerator_id
						S.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading sequences'
	#return res

def upload_shot(request):
	path = get_file_path('Shot.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotID':
				Is_S = Shot.objects.filter(ShotID = row[0])
				if len(Is_S) == 0:
					print row
					try:
						S = Shot()
						S.ShotID = row[0]
						S.VFXID = row[1]
						if not row[2] == 'NULL':
							S.ExternalID = row[2]
						S.ShotName = row[3]
						if not row[4] == 'NULL':
							S.Location = row[4]
						if not row[5] == 'NULL':
							S.CameraMotion = row[5]
						if not row[6] == 'NULL':
							S.SceneNumber = row[6]
						if not row[7] == 'NULL':
							S.PageNumber = row[7]
						S.Frames = row[8]
						if not row[11] == 'NULL':
							S.DirectorNotes = row[11]
						if not row[12] == 'NULL':
							S.ShotDescription = row[12]
						if not row[13] == 'NULL':
							S.Thumbnail = row[13]
						if not row[15] == 'NULL':
							S.ImageAssetID = row[15]
						S.AddConsumablesAllowance = row[16]
						if not row[17] == 'NULL':
							S.WorkedeBy = row[17]
						S.Type = row[18]
						if not row[19] == 'NULL':
							S.Lens = row[19]
						S.PrimaryBidNumber = row[20]
						if not row[21] == 'NULL':
							S.VFXTasks = row[21]
						if not row[22] == 'NULL':
							S.IsReference = row[22]
						if not row[23] == 'NULL':
							S.SortIndex = row[23]
						if not row[24] == 'NULL':
							S.Take = row[24]
						S.Active = row[25]
						project_id = Project.objects.get(ProjectID = row[10])
						S.Project_ID = project_id
						sequence_id = Sequence.objects.get(SequencialIDGenerator_ID = row[9])
						S.Sequence_ID = sequence_id
						status_id = Status.objects.get(StatusID = row[14])
						S.Status_ID = status_id
						S.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading shots'
	#return res

def upload_bid(request):
	path = get_file_path('Bid.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'BidID':
				Is_B = Bid.objects.filter(BidID = row[0])
				if len(Is_B) == 0:
					print row
					try:
						B = Bid()
						B.BidID = row[0]
						B.BidName = row[3]
						B.BidDate = datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
						if not (row[5] == 'NULL' or len(row[5]) == 0):
							B.BidNotes = row[5]
						B.BidLastModification = datetime.datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S")
						if not row[7] == 'NULL':
							B.AddConsumablesAllowance = row[7]
						B.BidNumber = row[8]
						B.RateSetNumber = row[9]
						B.HideInCalendar = row[10]
						project_id = Project.objects.get(ProjectID = row[2])
						B.Project_ID = project_id
						shot_id = Shot.objects.get(ShotID = row[1])
						B.Shot_ID = shot_id
						B.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading bids'
	#return res

def upload_assets(request):
	path = get_file_path('Assets.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'AssetID':
				Is_A = Assets.objects.filter(AssetID = row[0])
				if len(Is_A) == 0:
					print row
					try:
						A = Assets()
						A.AssetID = row[0]
						A.AssetName = row[1]
						if not (row[2] == 'NULL' or len(row[2]) == 0):
							A.Notes = row[2]
						if not row[3] == 'NULL':
							A.Path = row[3]
						A.Size = row[6]
						A.UploadDate = datetime.datetime.strptime(row[8], "%Y-%m-%d %H:%M:%S")
						if not row[9] == 'NULL':
							A.Public = row[9]
						if not (row[10] == 'NULL' or len(row[10]) == 0):
							A.Tags = row[10]
						A.Parent = row[11]
						A.LastModified = datetime.datetime.strptime(row[12], "%Y-%m-%d %H:%M:%S")
						if not row[14] == 'NULL':
							A.OnCloud = row[14]
						if not row[15] == 'NULL':
							A.CloudStatus = row[15]
						assettype_id = AssetType.objects.get(AssetTypeID = row[5])
						A.AssetType_ID = assettype_id
						project_id = Project.objects.get(ProjectID = row[4])
						A.Project_ID = project_id
						shot_id = Shot.objects.get(ShotID = row[13])
						A.Shot_ID = shot_id
						user_id = User.objects.get(username = row[7])
						user_id = UserProfile.objects.get(user = user_id.id)
						A.User_ID_Uploader = user_id
						A.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading assets'
	#return res

def upload_transfer(request):
	path = get_file_path('Transfer.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'TransferID':
				Is_T = Transfer.objects.filter(TransferID = row[0])
				if len(Is_T) == 0:
					print row
					try:
						T = Transfer()
						T.TransferID = row[0]
						T.Date = datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
						if not row[5] == 'NULL':
							T.IP = row[5]
						T.Type = row[2]
						assets_id = Assets.objects.get(AssetID = row[1])
						T.Assets_ID = assets_id
						user_id = User.objects.get(username = row[3])
						user_id = UserProfile.objects.get(user = user_id.id)
						T.User_ID = user_id
						T.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading transfers'
	#return res

def upload_assetpriviledges(request):
	path = get_file_path('AssetPriviledges.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'UserType':
				try:
					print row
					AP = AssetPriviledges()
					assets_id = Assets.objects.get(AssetID = row[1])
					AP.Assets_ID = assets_id
					usertype_id = UserTypes.objects.get(id = row[0])
					AP.UserTypes_ID = usertype_id
					AP.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading asset privileges'
	#return res

def upload_deletedassets(request):
	path = get_file_path('DeletedAssets.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'DeletedAssetID':
				Is_DA = DeletedAssets.objects.filter(DeletedAssetID = row[0])
				if len(Is_DA) == 0:
					print row
					try:
						DA = DeletedAssets()
						DA.DeletedAssetID = row[0]
						DA.AssetName = row[2]
						if not len(row[3]) == 0:
							DA.Notes = row[3]
						if not len(row[4]) == 0:
							DA.Path = row[4]
						DA.AssetType = row[6]
						DA.Size = row[7]
						DA.UploadDate = datetime.datetime.strptime(row[9], "%Y-%m-%d %H:%M:%S")
						DA.Public = row[10]
						if not len(row[11]) == 0:
							DA.Tags = row[11]
						assets_id = Assets.objects.get(AssetID = row[1])
						DA.Assets_ID = assets_id
						project_id = Project.objects.get(ProjectID = row[5])
						DA.Project_ID = project_id
						user_id = User.objects.get(username = row[8])
						user_id = UserProfile.objects.get(user = user_id.id)
						DA.User_ID_Uploader = user_id
						DA.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading deleted assets'
	#return res

def upload_downloadcontrols(request):
	path = get_file_path('DownloadControl.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'DownloadControlID':
				Is_DC = DownloadControl.objects.filter(DownloadControlID = row[0])
				if len(Is_DC) == 0:
					print row
					try:
						DC = DownloadControl()
						DC.DownloadControlID = row[0]
						DC.Path = row[3]
						DC.Date = datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
						assets_id = Assets.objects.get(AssetID = row[2])
						DC.Assets_ID = assets_id
						user_id = User.objects.get(username = row[1])
						user_id = UserProfile.objects.get(user = user_id.id)
						DC.User_ID = user_id
						DC.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading download controls'
	#return res

def upload_shotsservice(request):
	path = get_file_path('ShotsService.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotsServiceID':
				try:
					print row
					SS = ShotsService()
					SS.ShotServiceID = row[0]
					SS.Days = row[4]
					SS.BidNumber = row[5]
					project_id = Project.objects.get(ProjectID = row[2])
					SS.Project_ID = project_id
					service_id = Service.objects.get(ServiceID = row[3])
					SS.Service_ID = service_id
					shot_id = Shot.objects.get(ShotID = row[1])
					SS.Shot_ID = shot_id
					SS.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading shots services'
	#return res

def upload_shotsassets(request):
	path = get_file_path('ShotsAssets.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotsAssetsID':
				try:
					print row
					SA = ShotsAssets()
					SA.ShotsAssetsID = row[0]
					assets_id = Assets.objects.get(AssetID = row[2])
					SA.Assets_ID = assets_id
					project_id = Project.objects.get(ProjectID = row[3])
					SA.Project_ID = project_id
					shot_id = Shot.objects.get(ShotID = row[1])
					SA.Shot_ID = shot_id
					SA.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading shots assets'
	#return res

def upload_shotstatuslog(request):
	path = get_file_path('ShotStatusLog.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotStatusLogID':
				try:
					print row
					SSL = ShotStatusLog()
					SSL.FromStatus = row[3]
					SSL.ToStatus = row[4]
					SSL.Date = datetime.datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S")
					project_id = Project.objects.get(ProjectID = row[1])
					SSL.Project_ID = project_id
					shot_id = Shot.objects.get(ShotID = row[2])
					SSL.Shot_ID = shot_id
					user_id = User.objects.get(username = row[5])
					user_id = UserProfile.objects.get(user = user_id.id)
					SSL.User_ID = user_id
					SSL.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading shots status logs'
	#return res

def upload_shotdelivery(request):
	path = get_file_path('ShotDelivery.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotDeliveryID':
				try:
					print row
					SD = ShotDelivery()
					SD.VFXID = row[3]
					SD.ShotName = row[4]
					SD.ReviewDate = datetime.datetime.strptime(row[6], "%Y-%m-%d")
					SD.InternalComments = row[7]
					if not len(row[8]) == 0:
						SD.ClientComments = row[8]
					SD.InternalVersion = row[9]
					SD.ClientVersion = row[10]
					SD.Work = row[11]
					SD.Stereo = row[12]
					project_id = Project.objects.get(ProjectID = row[1])
					SD.Project_ID = project_id
					shot_id = Shot.objects.get(ShotID = row[2])
					SD.Shot_ID = shot_id
					status_id = Status.objects.get(StatusID = row[5])
					SD.Status_ID = status_id
					SD.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading shot deliverys'
	#return res

def upload_shotgroup(request):
	path = get_file_path('ShotGroup.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotGroupID':
				Is_SG = ShotGroup.objects.filter(ShotGroupID = row[0])
				if len(Is_SG) == 0:
					print row
					try:
						SG = ShotGroup()
						SG.ShotGroupID = row[0]
						SG.ShotGroupName = row[1]
						if not len(row[2]) == 0:
							SG.ShotGroupNotes = row[2]
						project_id = Project.objects.get(ProjectID = row[3])
						SG.Project_ID = project_id
						SG.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading shot groups'
	#return res

def upload_shotgroupshotid(request):
	path = get_file_path('ShotGroupShotID.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotGroupID':
				try:
					print row
					SGSI = ShotGroupShotID()
					shotgroup_id = ShotGroup.objects.get(ShotGroupID = row[0])
					SGSI.ShotGroup_ID = shotgroup_id
					shot_id = Shot.objects.get(ShotID = row[1])
					SGSI.Shot_ID = shot_id
					SGSI.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading shot group shot ids'
	#return res

def upload_shotgrouptentpole(request):
	path = get_file_path('ShotGroupTentpole.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotGroupID':
				try:
					print row
					SGT = ShotGroupTentpole()
					shotgroup_id = ShotGroup.objects.get(ShotGroupID = row[0])
					SGT.ShotGroup_ID = shotgroup_id
					shot_id = Shot.objects.get(ShotID = row[1])
					SGT.Shot_ID = shot_id
					SGT.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading shot group tentpoles'
	#return res

def upload_shotuser(request):
	path = get_file_path('ShotUser.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'UserID':
				try:
					print row
					SU = ShotUser()
					shot_id = Shot.objects.get(ShotID = row[1])
					SU.Shot_ID = shot_id
					user_id = User.objects.get(username = row[0])
					user_id = UserProfile.objects.get(user = user_id.id)
					SU.User_ID = user_id
					SU.save()
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					res = False
					print 'could not save %s' % row[0]
					#return res
			else:
				pass
	print 'finish uploading shot users'
	#return res

def upload_selectionset(request):
	path = get_file_path('SelectionSet.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'SelectionSetID':
				Is_SS = SelectionSet.objects.filter(SelectionSetID = row[0])
				if len(Is_SS) == 0:
					print row
					try:
						SS = SelectionSet()
						SS.SelectionSetID = row[0]
						if not len(row[1]) == 0:
							SS.SelectionSetName = row[1]
						project_id = Project.objects.get(ProjectID = row[2])
						SS.Project_ID = project_id
						SS.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading selection sets'
	#return res

def upload_shotselectionset(request):
	path = get_file_path('ShotSelectionSet.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotSelectionSetID':
				Is_SSS = ShotSelectionSet.objects.filter(ShotSelectionSetID = row[0])
				if len(Is_SSS) == 0:
					print row
					try:
						SSS = ShotSelectionSet()
						SSS.ShotSelectionSetID = row[0]
						selectionset_id = SelectionSet.objects.get(SelectionSetID = row[1])
						SSS.SelectionSet_ID = selectionset_id
						shot_id = Shot.objects.get(ShotID = row[2])
						SSS.Shot_ID = shot_id
						SSS.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading shot selection sets'
	#return res

def upload_customshotfield(request):
	path = get_file_path('CustomShotField.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'CustomShotFieldID':
				Is_CSF = CustomShotField.objects.filter(CustomShotFieldID = row[0])
				if len(Is_CSF) == 0:
					print row
					try:
						CSF = CustomShotField()
						CSF.CustomShotFieldID = row[0]
						CSF.FieldName = row[1]
						if not (len(row[2]) == 0 or row[2] == 'NULL'):
							CSF.DefaultValue = row[2]
						project_id = Project.objects.get(ProjectID = row[1])
						CSF.Project_ID = project_id
						CSF.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading custom shot field'
	#return res

def upload_shotcustomshotfield(request):
	path = get_file_path('ShotCustomShotField.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'ShotCustomShotFieldID':
				Is_SCSF = ShotCustomShotField.objects.filter(ShotCustomShotFieldID = row[0])
				if len(Is_SCSF) == 0:
					print row
					try:
						SCSF = ShotCustomShotField()
						SCSF.ShotSelectionSetID = row[0]
						if not len(row[1]) == 0:
							SCSF.Value = row[1]
						customshotfield_id = CustomShotField.objects.get(CustomShotFieldID = row[1])
						SCSF.CustomShotField_ID = customshotfield_id
						shot_id = Shot.objects.get(ShotID = row[2])
						SCSF.Shot_ID = shot_id
						SCSF.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading shot custom shot fields'
	#return res

def upload_version(request):
	path = get_file_path('Version.csv')
	res = True
	print 'path is %s' % path
	with open(path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] != 'VersionID':
				Is_V = Version.objects.filter(VersionID = row[0])
				if len(Is_V) == 0:
					print row
					try:
						V = Version()
						V.VersionID = row[0]
						V.Major = row[2]
						V.Minor = row[3]
						V.External = row[4]
						if not len(row[5]) == 0:
							V.Notes = row[5]
						if not len(row[6]) == 0:
							V.Tags = row[6]
						V.CreationDate = datetime.datetime.strptime(row[7], "%Y-%m-%d")
						if not row[8] == 'NULL':
							V.View = row[8]
						if not row[9] == 'NULL':
							V.Task = row[9]
						if not row[10] == 'NULL':
							V.PublishedBy = row[10]
						shot_id = Shot.objects.get(ShotID = row[1])
						V.Shot_ID = shot_id
						V.save()
					except Exception as e:
						print '%s (%s)' % (e.message, type(e))
						res = False
						print 'could not save %s' % row[0]
						#return res
				else:
					pass
			else:
				pass
	print 'finish uploading versions'
	#return res

def upload_all(request):
	if not upload_usertype():
		print 'error at upload_usertype'
	elif not upload_user():
		print 'error at upload_user'
	elif not upload_accesscontrolfingerprint():
		print 'error at upload_accesscontrolfingerprint'
	elif not upload_status():
		print 'error at upload_status'
	elif not upload_accesscontrollog():
		print 'error at upload_accesscontrollog'
	elif not upload_loginattempt():
		print 'error at upload_loginattempt'
	else:
		print 'DONE!!!!!!!!! ñ_ñ'