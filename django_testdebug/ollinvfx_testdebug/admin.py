from django.contrib import admin
from ollinvfx_testdebug.models import *
# Register your models here.

class UsertypesAdmin(admin.ModelAdmin):
	list_display = ['usertype', 'typename']
	search_fields = ['usertype', 'typename']
	list_filter = ['usertype', 'typename']
admin.site.register(Usertypes, UsertypesAdmin)

class UserAdmin(admin.ModelAdmin):
	list_display = ['userid', 'firstname', 'lastname', 'email', 'isgroup', 'usertype']
	search_fields = ['userid', 'firstname', 'lastname', 'email', 'isgroup', 'usertype']
	list_filter = ['userid', 'firstname', 'lastname', 'email', 'isgroup', 'usertype']
admin.site.register(User, UserAdmin)

class AccesscontrolfingerprintAdmin(admin.ModelAdmin):
	list_display = ['enrollid', 'finger', 'fingerprint']
	search_fields = ['enrollid', 'finger', 'fingerprint']
	list_filter = ['enrollid', 'finger', 'fingerprint']
admin.site.register(Accesscontrolfingerprint, AccesscontrolfingerprintAdmin)

class StatusAdmin(admin.ModelAdmin):
	list_display = ['status', 'statusname']
	search_fields = ['status', 'statusname']
	list_filter = ['status', 'statusname']
admin.site.register(Status, StatusAdmin)

class AccesscontrollogAdmin(admin.ModelAdmin):
	list_display = ['eventid', 'date', 'enrollid', 'period', 'method', 'overrideaction', 'status']
	search_fields = ['eventid', 'date', 'enrollid', 'period', 'method', 'overrideaction', 'status']
	list_filter = ['eventid', 'date', 'enrollid', 'period', 'method', 'overrideaction']
admin.site.register(Accesscontrollog, AccesscontrollogAdmin)

class LoginattemptAdmin(admin.ModelAdmin):
	list_display = ['id', 'userid', 'attempts', 'lastattempt']
	search_fields = ['id', 'userid', 'attempts', 'lastattempt']
	list_filter = ['id', 'userid', 'attempts', 'lastattempt']
admin.site.register(Loginattempt, LoginattemptAdmin)

class UsergroupAdmin(admin.ModelAdmin):
	list_display = ['groupid', 'userid']
	search_fields = ['groupid', 'userid']
	list_filter = ['groupid', 'userid']
admin.site.register(Usergroup, UsergroupAdmin)

class EvaluationroundAdmin(admin.ModelAdmin):
	list_display = ['evaluationroundid', 'date']
	search_fields = ['evaluationroundid', 'date']
	list_filter = ['evaluationroundid', 'date']
admin.site.register(Evaluationround, EvaluationroundAdmin)

class EvaluationAdmin(admin.ModelAdmin):
	list_display = ['evaluationid', 'technical', 'professional', 'teamwork', 'forceeval', 'evalapplied', 'evaluationdate', 'currentboss', 'evaluated', 'evaluator', 'roundid']
	search_fields = ['evaluationid', 'technical', 'professional', 'teamwork', 'forceeval', 'evalapplied', 'evaluationdate', 'currentboss', 'evaluated', 'evaluator', 'roundid']
	list_filter = ['evaluationid', 'technical', 'professional', 'teamwork', 'forceeval', 'evalapplied', 'evaluationdate', 'currentboss', 'evaluated', 'evaluator', 'roundid']
admin.site.register(Evaluation, EvaluationAdmin)

class EntitytypeAdmin(admin.ModelAdmin):
	list_display = ['entitytypeid', 'entityname']
	search_fields = ['entitytypeid', 'entityname']
	list_filter = ['entitytypeid', 'entityname']
admin.site.register(Entitytype, EntitytypeAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ['commentid', 'date', 'entityid', 'entitytypeid', 'userid']
	search_fields = ['commentid', 'date', 'entityid', 'entitytypeid', 'userid']
	list_filter = ['commentid', 'date', 'entityid', 'entitytypeid', 'userid']
admin.site.register(Comment, CommentAdmin)

class AlarmAdmin(admin.ModelAdmin):
	list_display = ['alarmid', 'entityid', 'due', 'what', 'actionid', 'mode', 'lastfired', 'entitytypeid', 'status']
	search_fields = ['alarmid', 'entityid', 'due', 'what', 'actionid', 'mode', 'lastfired', 'entitytypeid', 'status']
	list_filter = ['alarmid', 'entityid', 'due', 'what', 'actionid', 'mode', 'lastfired', 'entitytypeid', 'status']
admin.site.register(Alarm, AlarmAdmin)

class AlarmreminderAdmin(admin.ModelAdmin):
	list_display = ['alarmreminderid', 'daysbefore', 'fired', 'alarmid']
	search_fields = ['alarmreminderid', 'daysbefore', 'fired', 'alarmid']
	list_filter = ['alarmreminderid', 'daysbefore', 'fired', 'alarmid']
admin.site.register(Alarmreminder, AlarmreminderAdmin)

class AlarmactionparameterAdmin(admin.ModelAdmin):
	list_display = ['id', 'alarmid', 'parameter']
	search_fields = ['id', 'alarmid', 'parameter']
	list_filter = ['id', 'alarmid', 'parameter']
admin.site.register(Alarmactionparameter, AlarmactionparameterAdmin)

class CommandsAdmin(admin.ModelAdmin):
	list_display = ['commandname']
	search_fields = ['commandname']
	list_filter = ['commandname']
admin.site.register(Commands, CommandsAdmin)

class PriviledgesmatrixAdmin(admin.ModelAdmin):
	list_display = ['command', 'number_1', 'number_2', 'number_3', 'number_4', 'number_5', 'number_6', 'number_7', 'number_8']
	search_fields = ['command', 'number_1', 'number_2', 'number_3', 'number_4', 'number_5', 'number_6', 'number_7', 'number_8']
	list_filter = ['command', 'number_1', 'number_2', 'number_3', 'number_4', 'number_5', 'number_6', 'number_7', 'number_8']
admin.site.register(Priviledgesmatrix, PriviledgesmatrixAdmin)

class CommandrelationsAdmin(admin.ModelAdmin):
	list_display = ['id', 'command', 'relatedto']
	search_fields = ['id', 'command', 'relatedto']
	list_filter = ['id', 'command', 'relatedto']
admin.site.register(Commandrelations, CommandrelationsAdmin)

class ExtendedpermissionsAdmin(admin.ModelAdmin):
	list_display = ['action', 'command', 'userid']
	search_fields = ['action', 'command', 'userid']
	list_filter = ['action', 'command', 'userid']
admin.site.register(Extendedpermissions, ExtendedpermissionsAdmin)

class NotificationAdmin(admin.ModelAdmin):
	list_display = ['notificationid', 'alreadyread', 'typeid', 'from_field', 'addressedto', 'subject', 'datetime', 'status']
	search_fields = ['notificationid', 'alreadyread', 'typeid', 'from_field', 'addressedto', 'subject', 'datetime', 'status']
	list_filter = ['notificationid', 'alreadyread', 'typeid', 'from_field', 'addressedto', 'subject', 'datetime', 'status']
admin.site.register(Notification, NotificationAdmin)

class NotificationmetadataAdmin(admin.ModelAdmin):
	list_display = ['id', 'notificationid', 'metadataname', 'metadatavalue']
	search_fields = ['id', 'notificationid', 'metadataname', 'metadatavalue']
	list_filter = ['id', 'notificationid', 'metadataname', 'metadatavalue']
admin.site.register(Notificationmetadata, NotificationmetadataAdmin)

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['projectid', 'projectname', 'projectnickname', 'director', 'producer', 'studio', 'consumableallowance', 'contingency', 'imageassetid', 'active', 'creationdate', 'restrictshotstoassignedusers', 'startdate']
	search_fields = ['projectid', 'projectname', 'projectnickname', 'director', 'producer', 'studio', 'consumableallowance', 'contingency', 'imageassetid', 'active', 'creationdate', 'restrictshotstoassignedusers', 'startdate']
	list_filter = ['projectid', 'projectname', 'projectnickname', 'director', 'producer', 'studio', 'consumableallowance', 'contingency', 'imageassetid', 'active', 'creationdate', 'restrictshotstoassignedusers', 'startdate']
admin.site.register(Project, ProjectAdmin)

class MilestoneAdmin(admin.ModelAdmin):
	list_display = ['milestoneid', 'name', 'date', 'projectid']
	search_fields = ['milestoneid', 'name', 'date', 'projectid']
	list_filter = ['milestoneid', 'name', 'date', 'projectid']
admin.site.register(Milestone, MilestoneAdmin)

class IncomingfileAdmin(admin.ModelAdmin):
	list_display = ['incomingfileid', 'date', 'sender', 'addressedto', 'sourcepath', 'finalpath', 'area', 'media', 'projectid']
	search_fields = ['incomingfileid', 'date', 'sender', 'addressedto', 'sourcepath', 'finalpath', 'area', 'media', 'projectid']
	list_filter = ['incomingfileid', 'date', 'sender', 'addressedto', 'sourcepath', 'finalpath', 'area', 'media', 'projectid']
admin.site.register(Incomingfile, IncomingfileAdmin)

class ProjectuserAdmin(admin.ModelAdmin):
	list_display = ['id', 'projectid', 'userid']
	search_fields = ['id', 'projectid', 'userid']
	list_filter = ['id', 'projectid', 'userid']
admin.site.register(Projectuser, ProjectuserAdmin)

class PlaylistAdmin(admin.ModelAdmin):
	list_display = ['playlistid', 'playlistname', 'autoupdate', 'projectid']
	search_fields = ['playlistid', 'playlistname', 'autoupdate', 'projectid']
	list_filter = ['playlistid', 'playlistname', 'autoupdate', 'projectid']
admin.site.register(Playlist, PlaylistAdmin)

class RatesetAdmin(admin.ModelAdmin):
	list_display = ['ratesetid', 'ratesetnumber', 'ratesetname', 'ratesetcreationdate', 'ratesetlastmodification', 'ratesetconsumableallowance', 'ratesetcontingency', 'ratesetextra', 'ratesetextrait', 'projectid']
	search_fields = ['ratesetid', 'ratesetnumber', 'ratesetname', 'ratesetcreationdate', 'ratesetlastmodification', 'ratesetconsumableallowance', 'ratesetcontingency', 'ratesetextra', 'ratesetextrait', 'projectid']
	list_filter = ['ratesetid', 'ratesetnumber', 'ratesetname', 'ratesetcreationdate', 'ratesetlastmodification', 'ratesetconsumableallowance', 'ratesetcontingency', 'ratesetextra', 'ratesetextrait', 'projectid']
admin.site.register(Rateset, RatesetAdmin)

class HarddiskstatusAdmin(admin.ModelAdmin):
	list_display = ['harddiskstatusid', 'harddiskstatusname']
	search_fields = ['harddiskstatusid', 'harddiskstatusname']
	list_filter = ['harddiskstatusid', 'harddiskstatusname']
admin.site.register(Harddiskstatus, HarddiskstatusAdmin)

class HarddiskregisterAdmin(admin.ModelAdmin):
	list_display = ['harddiskregisterid', 'serialnumber', 'harddisknumber', 'harddiskname', 'fromaddress', 'contentonarrival', 'arrivaldate', 'contentonexit', 'exitdate', 'projectid', 'statusid']
	search_fields = ['harddiskregisterid', 'serialnumber', 'harddisknumber', 'harddiskname', 'fromaddress', 'contentonarrival', 'arrivaldate', 'contentonexit', 'exitdate', 'projectid', 'statusid']
	list_filter = ['harddiskregisterid', 'serialnumber', 'harddisknumber', 'harddiskname', 'fromaddress', 'contentonarrival', 'arrivaldate', 'contentonexit', 'exitdate', 'projectid', 'statusid']
admin.site.register(Harddiskregister, HarddiskregisterAdmin)

class UploadcontrolAdmin(admin.ModelAdmin):
	list_display = ['uploadcontrolid', 'filename', 'path', 'date', 'projectid', 'userid']
	search_fields = ['uploadcontrolid', 'filename', 'path', 'date', 'projectid', 'userid']
	list_filter = ['uploadcontrolid', 'filename', 'path', 'date', 'projectid', 'userid']
admin.site.register(Uploadcontrol, UploadcontrolAdmin)

class ServicetypeAdmin(admin.ModelAdmin):
	list_display = ['servicetypeid', 'servicetypename']
	search_fields = ['servicetypeid', 'servicetypename']
	list_filter = ['servicetypeid', 'servicetypename']
admin.site.register(Servicetype, ServicetypeAdmin)

class ServiceAdmin(admin.ModelAdmin):
	list_display = ['serviceid', 'servicename', 'costperday', 'servicetypeid']
	search_fields = ['serviceid', 'servicename', 'costperday', 'servicetypeid']
	list_filter = ['serviceid', 'servicename', 'costperday', 'servicetypeid']
admin.site.register(Service, ServiceAdmin)

class ServicehistogramcolorAdmin(admin.ModelAdmin):
	list_display = ['servicehistogramcolorid', 'r', 'g', 'b', 'serviceid']
	search_fields = ['servicehistogramcolorid', 'r', 'g', 'b', 'serviceid']
	list_filter = ['servicehistogramcolorid', 'r', 'g', 'b', 'serviceid']
admin.site.register(Servicehistogramcolor, ServicehistogramcolorAdmin)

class ProjectserviceAdmin(admin.ModelAdmin):
	list_display = ['projectserviceid', 'rate', 'ratesetnumber', 'projectid', 'serviceid']
	search_fields = ['projectserviceid', 'rate', 'ratesetnumber', 'projectid', 'serviceid']
	list_filter = ['projectserviceid', 'rate', 'ratesetnumber', 'projectid', 'serviceid']
admin.site.register(Projectservice, ProjectserviceAdmin)

class ProjecttaskserviceAdmin(admin.ModelAdmin):
	list_display = ['projecttaskserviceid', 'slots', 'projectid', 'serviceid']
	search_fields = ['projecttaskserviceid', 'slots', 'projectid', 'serviceid']
	list_filter = ['projecttaskserviceid', 'slots', 'projectid', 'serviceid']
admin.site.register(Projecttaskservice, ProjecttaskserviceAdmin)

class AssettypeAdmin(admin.ModelAdmin):
	list_display = ['assettypeid', 'assettypename']
	search_fields = ['assettypeid', 'assettypename']
	list_filter = ['assettypeid', 'assettypename']
admin.site.register(Assettype, AssettypeAdmin)

class SequencialidgeneratorAdmin(admin.ModelAdmin):
	list_display = ['id']
	search_fields = ['id']
	list_filter = ['id']
admin.site.register(Sequencialidgenerator, SequencialidgeneratorAdmin)

class SequenceAdmin(admin.ModelAdmin):
	list_display = ['sequenceid', 'sequencename', 'sequencenickname', 'projectid']
	search_fields = ['sequenceid', 'sequencename', 'sequencenickname', 'projectid']
	list_filter = ['sequenceid', 'sequencename', 'sequencenickname', 'projectid']
admin.site.register(Sequence, SequenceAdmin)

class ShotAdmin(admin.ModelAdmin):
	list_display = ['shotid', 'vfxid', 'externalid', 'shotname', 'location', 'cameramotion', 'scenenumber', 'pagenumber', 'frames', 'imageassetid', 'workedby', 'type', 'lens', 'primarybidnumber', 'vfxtasks', 'isreference', 'sortindex', 'take', 'active', 'projectid', 'sequenceid', 'status']
	search_fields = ['shotid', 'vfxid', 'externalid', 'shotname', 'location', 'cameramotion', 'scenenumber', 'pagenumber', 'frames', 'imageassetid', 'workedby', 'type', 'lens', 'primarybidnumber', 'vfxtasks', 'isreference', 'sortindex', 'take', 'active', 'projectid', 'sequenceid', 'status']
	list_filter = ['shotid', 'vfxid', 'externalid', 'shotname', 'location', 'cameramotion', 'scenenumber', 'pagenumber', 'frames', 'imageassetid', 'workedby', 'type', 'lens', 'primarybidnumber', 'vfxtasks', 'isreference', 'sortindex', 'take', 'active', 'projectid', 'sequenceid', 'status']
admin.site.register(Shot, ShotAdmin)

class BidAdmin(admin.ModelAdmin):
	list_display = ['bidid', 'bidname', 'biddate', 'bidlastmodification', 'addconsumablesallowance', 'bidnumber', 'ratesetnumber', 'hideincalendar', 'projectid', 'shotid']
	search_fields = ['bidid', 'bidname', 'biddate', 'bidlastmodification', 'addconsumablesallowance', 'bidnumber', 'ratesetnumber', 'hideincalendar', 'projectid', 'shotid']
	list_filter = ['bidid', 'bidname', 'biddate', 'bidlastmodification', 'addconsumablesallowance', 'bidnumber', 'ratesetnumber', 'hideincalendar', 'projectid', 'shotid']
admin.site.register(Bid, BidAdmin)

class AssetsAdmin(admin.ModelAdmin):
	list_display = ['assetid', 'assetname', 'path', 'size', 'uploaddate', 'public', 'parent', 'lastmodified', 'oncloud', 'cloudstatus', 'projectid', 'shotid', 'typeid', 'uploader']
	search_fields = ['assetid', 'assetname', 'path', 'size', 'uploaddate', 'public', 'parent', 'lastmodified', 'oncloud', 'cloudstatus', 'projectid', 'shotid', 'typeid', 'uploader']
	list_filter = ['assetid', 'assetname', 'path', 'size', 'uploaddate', 'public', 'parent', 'lastmodified', 'oncloud', 'cloudstatus', 'projectid', 'shotid', 'typeid', 'uploader']
admin.site.register(Assets, AssetsAdmin)

class TransferAdmin(admin.ModelAdmin):
	list_display = ['transferid', 'type', 'date', 'ip', 'assetid', 'userid']
	search_fields = ['transferid', 'type', 'date', 'ip', 'assetid', 'userid']
	list_filter = ['transferid', 'type', 'date', 'ip', 'assetid', 'userid']
admin.site.register(Transfer, TransferAdmin)

class AssetpriviledgesAdmin(admin.ModelAdmin):
	list_display = ['id', 'assetid', 'usertype']
	search_fields = ['id', 'assetid', 'usertype']
	list_filter = ['id', 'assetid', 'usertype']
admin.site.register(Assetpriviledges, AssetpriviledgesAdmin)

class DeletedassetsAdmin(admin.ModelAdmin):
	list_display = ['deletedassetid', 'assetname', 'typeid', 'size', 'uploaddate', 'public', 'assetid', 'projectid', 'uploader']
	search_fields = ['deletedassetid', 'assetname', 'typeid', 'size', 'uploaddate', 'public', 'assetid', 'projectid', 'uploader']
	list_filter = ['deletedassetid', 'assetname', 'typeid', 'size', 'uploaddate', 'public', 'assetid', 'projectid', 'uploader']
admin.site.register(Deletedassets, DeletedassetsAdmin)

class DownloadcontrolAdmin(admin.ModelAdmin):
	list_display = ['downloadcontrolid', 'path', 'date', 'assetid', 'userid']
	search_fields = ['downloadcontrolid', 'path', 'date', 'assetid', 'userid']
	list_filter = ['downloadcontrolid', 'path', 'date', 'assetid', 'userid']
admin.site.register(Downloadcontrol, DownloadcontrolAdmin)

class ShotsserviceAdmin(admin.ModelAdmin):
	list_display = ['shotserviceid', 'days', 'bidnumber', 'projectid', 'serviceid', 'shotid']
	search_fields = ['shotserviceid', 'days', 'bidnumber', 'projectid', 'serviceid', 'shotid']
	list_filter = ['shotserviceid', 'days', 'bidnumber', 'projectid', 'serviceid', 'shotid']
admin.site.register(Shotsservice, ShotsserviceAdmin)

class ShotsassetsAdmin(admin.ModelAdmin):
	list_display = ['shotsassetsid', 'assetid', 'projectid', 'shotid']
	search_fields = ['shotsassetsid', 'assetid', 'projectid', 'shotid']
	list_filter = ['shotsassetsid', 'assetid', 'projectid', 'shotid']
admin.site.register(Shotsassets, ShotsassetsAdmin)

class ShotstatuslogAdmin(admin.ModelAdmin):
	list_display = ['shotstatuslogid', 'fromstatus', 'tostatus', 'date', 'projectid', 'shotid', 'userid']
	search_fields = ['shotstatuslogid', 'fromstatus', 'tostatus', 'date', 'projectid', 'shotid', 'userid']
	list_filter = ['shotstatuslogid', 'fromstatus', 'tostatus', 'date', 'projectid', 'shotid', 'userid']
admin.site.register(Shotstatuslog, ShotstatuslogAdmin)

class ShotdeliveryAdmin(admin.ModelAdmin):
	list_display = ['shotdeliveryid', 'vfxid', 'shotname', 'reviewdate', 'internalversion', 'clientversion', 'work', 'stereo', 'projectid', 'shotid', 'status']
	search_fields = ['shotdeliveryid', 'vfxid', 'shotname', 'reviewdate', 'internalversion', 'clientversion', 'work', 'stereo', 'projectid', 'shotid', 'status']
	list_filter = ['shotdeliveryid', 'vfxid', 'shotname', 'reviewdate', 'internalversion', 'clientversion', 'work', 'stereo', 'projectid', 'shotid', 'status']
admin.site.register(Shotdelivery, ShotdeliveryAdmin)

class ShotgroupAdmin(admin.ModelAdmin):
	list_display = ['shotgroupid', 'shotgroupname', 'projectid']
	search_fields = ['shotgroupid', 'shotgroupname', 'projectid']
	list_filter = ['shotgroupid', 'shotgroupname', 'projectid']
admin.site.register(Shotgroup, ShotgroupAdmin)

class ShotgroupshotidAdmin(admin.ModelAdmin):
	list_display = ['id', 'shotgroupid', 'shotid']
	search_fields = ['id', 'shotgroupid', 'shotid']
	list_filter = ['id', 'shotgroupid', 'shotid']
admin.site.register(Shotgroupshotid, ShotgroupshotidAdmin)

class ShotgrouptentpoleAdmin(admin.ModelAdmin):
	list_display = ['id', 'shotgroupid', 'shotid']
	search_fields = ['id', 'shotgroupid', 'shotid']
	list_filter = ['id', 'shotgroupid', 'shotid']
admin.site.register(Shotgrouptentpole, ShotgrouptentpoleAdmin)

class ShotuserAdmin(admin.ModelAdmin):
	list_display = ['id', 'shotid', 'userid']
	search_fields = ['id', 'shotid', 'userid']
	list_filter = ['id', 'shotid', 'userid']
admin.site.register(Shotuser, ShotuserAdmin)

class SelectionsetAdmin(admin.ModelAdmin):
	list_display = ['selectionsetid', 'selectionsetname', 'projectid']
	search_fields = ['selectionsetid', 'selectionsetname', 'projectid']
	list_filter = ['selectionsetid', 'selectionsetname', 'projectid']
admin.site.register(Selectionset, SelectionsetAdmin)

class ShotselectionsetAdmin(admin.ModelAdmin):
	list_display = ['shotselectionsetid', 'selectionsetid', 'shotid']
	search_fields = ['shotselectionsetid', 'selectionsetid', 'shotid']
	list_filter = ['shotselectionsetid', 'selectionsetid', 'shotid']
admin.site.register(Shotselectionset, ShotselectionsetAdmin)

class CustomshotfieldAdmin(admin.ModelAdmin):
	list_display = ['customshotfieldid', 'fieldname', 'defaultvalue', 'projectid']
	search_fields = ['customshotfieldid', 'fieldname', 'defaultvalue', 'projectid']
	list_filter = ['customshotfieldid', 'fieldname', 'defaultvalue', 'projectid']
admin.site.register(Customshotfield, CustomshotfieldAdmin)

class ShotcustomshotfieldAdmin(admin.ModelAdmin):
	list_display = ['shotcustomshotfieldid', 'value', 'customshotfieldid', 'shotid']
	search_fields = ['shotcustomshotfieldid', 'value', 'customshotfieldid', 'shotid']
	list_filter = ['shotcustomshotfieldid', 'value', 'customshotfieldid', 'shotid']
admin.site.register(Shotcustomshotfield, ShotcustomshotfieldAdmin)

class VersionAdmin(admin.ModelAdmin):
	list_display = ['versionid', 'major', 'minor', 'external', 'view', 'task', 'publishedby', 'shotid']
	search_fields = ['versionid', 'major', 'minor', 'external', 'view', 'task', 'publishedby', 'shotid']
	list_filter = ['versionid', 'major', 'minor', 'external', 'view', 'task', 'publishedby', 'shotid']
admin.site.register(Version, VersionAdmin)

class VersionassetAdmin(admin.ModelAdmin):
	list_display = ['versionassetid', 'assetid', 'versionid']
	search_fields = ['versionassetid', 'assetid', 'versionid']
	list_filter = ['versionassetid', 'assetid', 'versionid']
admin.site.register(Versionasset, VersionassetAdmin)

class ScriptAdmin(admin.ModelAdmin):
	list_display = ['scriptid', 'scriptname', 'majorversion', 'minorversion', 'task', 'stask', 'projectid', 'shotid', 'userid']
	search_fields = ['scriptid', 'scriptname', 'majorversion', 'minorversion', 'task', 'stask', 'projectid', 'shotid', 'userid']
	list_filter = ['scriptid', 'scriptname', 'majorversion', 'minorversion', 'task', 'stask', 'projectid', 'shotid', 'userid']
admin.site.register(Script, ScriptAdmin)

class PublishjobAdmin(admin.ModelAdmin):
	list_display = ['jobid', 'creationdate', 'publishdate', 'publishtype', 'createdby', 'scriptid', 'status']
	search_fields = ['jobid', 'creationdate', 'publishdate', 'publishtype', 'createdby', 'scriptid', 'status']
	list_filter = ['jobid', 'creationdate', 'publishdate', 'publishtype', 'createdby', 'scriptid', 'status']
admin.site.register(Publishjob, PublishjobAdmin)

class LineupAdmin(admin.ModelAdmin):
	list_display = ['lineupid', 'creationdate', 'name', 'camera', 'tstop', 'framesize', 'cutlengthframes', 'inframe', 'intc', 'outframe', 'outtc', 'frameswithhandles', 'inframewithhandles', 'intcwithhandles', 'outframewithhandles', 'outtcwithhandles', 'rawmediastart', 'rawmediaend', 'rawmediaduration', 'rawmediastartframe', 'rawmediaendframe', 'rawmediadurationframes', 'editorialname', 'edlpull', 'format', 'iso', 'kelvin', 'lens', 'reel', 'reelid', 'scene', 'setup', 'shootdate', 'shootday', 'shuttleangle', 'shutterspeed', 'stabilizecurvessent', 'take', 'tint', 'createdby', 'projectid', 'shotid']
	search_fields = ['lineupid', 'creationdate', 'name', 'camera', 'tstop', 'framesize', 'cutlengthframes', 'inframe', 'intc', 'outframe', 'outtc', 'frameswithhandles', 'inframewithhandles', 'intcwithhandles', 'outframewithhandles', 'outtcwithhandles', 'rawmediastart', 'rawmediaend', 'rawmediaduration', 'rawmediastartframe', 'rawmediaendframe', 'rawmediadurationframes', 'editorialname', 'edlpull', 'format', 'iso', 'kelvin', 'lens', 'reel', 'reelid', 'scene', 'setup', 'shootdate', 'shootday', 'shuttleangle', 'shutterspeed', 'stabilizecurvessent', 'take', 'tint', 'createdby', 'projectid', 'shotid']
	list_filter = ['lineupid', 'creationdate', 'name', 'camera', 'tstop', 'framesize', 'cutlengthframes', 'inframe', 'intc', 'outframe', 'outtc', 'frameswithhandles', 'inframewithhandles', 'intcwithhandles', 'outframewithhandles', 'outtcwithhandles', 'rawmediastart', 'rawmediaend', 'rawmediaduration', 'rawmediastartframe', 'rawmediaendframe', 'rawmediadurationframes', 'editorialname', 'edlpull', 'format', 'iso', 'kelvin', 'lens', 'reel', 'reelid', 'scene', 'setup', 'shootdate', 'shootday', 'shuttleangle', 'shutterspeed', 'stabilizecurvessent', 'take', 'tint', 'createdby', 'projectid', 'shotid']
admin.site.register(Lineup, LineupAdmin)

class SalarygeneraldataAdmin(admin.ModelAdmin):
	list_display = ['maxsalaryinc', 'cpimx', 'cpiusa', 'cpiadjuststrategy']
	search_fields = ['maxsalaryinc', 'cpimx', 'cpiusa', 'cpiadjuststrategy']
	list_filter = ['maxsalaryinc', 'cpimx', 'cpiusa', 'cpiadjuststrategy']
admin.site.register(Salarygeneraldata, SalarygeneraldataAdmin)

class SalarystructureAdmin(admin.ModelAdmin):
	list_display = ['salarystructureid', 'salaryname', 'salarydefinition', 'salarymidrange', 'levelincrease', 'currencytype', 'salary1', 'salary2', 'salary3', 'salary4', 'salary5', 'salary6', 'salary7', 'salary8', 'salary9']
	search_fields = ['salarystructureid', 'salaryname', 'salarydefinition', 'salarymidrange', 'levelincrease', 'currencytype', 'salary1', 'salary2', 'salary3', 'salary4', 'salary5', 'salary6', 'salary7', 'salary8', 'salary9']
	list_filter = ['salarystructureid', 'salaryname', 'salarydefinition', 'salarymidrange', 'levelincrease', 'currencytype', 'salary1', 'salary2', 'salary3', 'salary4', 'salary5', 'salary6', 'salary7', 'salary8', 'salary9']
admin.site.register(Salarystructure, SalarystructureAdmin)

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['departmentid', 'departmentname', 'departmentheadid']
	search_fields = ['departmentid', 'departmentname', 'departmentheadid']
	list_filter = ['departmentid', 'departmentname', 'departmentheadid']
admin.site.register(Department, DepartmentAdmin)

class AssociateAdmin(admin.ModelAdmin):
	list_display = ['associateid', 'firstname', 'lastname', 'active', 'currentsalary', 'lastincrease', 'lastcolincrease', 'increaseapply', 'bossid', 'firsthired', 'title', 'address', 'phone', 'alloweddaysperyear', 'departmentid', 'salarystructureid', 'userid']
	search_fields = ['associateid', 'firstname', 'lastname', 'active', 'currentsalary', 'lastincrease', 'lastcolincrease', 'increaseapply', 'bossid', 'firsthired', 'title', 'address', 'phone', 'alloweddaysperyear', 'departmentid', 'salarystructureid', 'userid']
	list_filter = ['associateid', 'firstname', 'lastname', 'active', 'currentsalary', 'lastincrease', 'lastcolincrease', 'increaseapply', 'bossid', 'firsthired', 'title', 'address', 'phone', 'alloweddaysperyear', 'departmentid', 'salarystructureid', 'userid']
admin.site.register(Associate, AssociateAdmin)

class Coladmin(admin.ModelAdmin):
	list_display = ['colid', 'name', 'year', 'col']
	search_fields = ['colid', 'name', 'year', 'col']
	list_filter = ['colid', 'name', 'year', 'col']
admin.site.register(Col, Coladmin)

class MeritpercentagesAdmin(admin.ModelAdmin):
	list_display = ['salaryquartile', 'rate0', 'rate1', 'rate2', 'rate3', 'rate4']
	search_fields = ['salaryquartile', 'rate0', 'rate1', 'rate2', 'rate3', 'rate4']
	list_filter = ['salaryquartile', 'rate0', 'rate1', 'rate2', 'rate3', 'rate4']
admin.site.register(Meritpercentages, MeritpercentagesAdmin)

class AssociatesalaryhistoryAdmin(admin.ModelAdmin):
	list_display = ['associatesalaryhistoryid', 'salarymoddate', 'oldsalary', 'newsalary', 'newsalarystructureid', 'performancerating', 'costofliving', 'meritincrease', 'meritamount', 'promotionbonus', 'promotionbonusamount', 'salaryenddate', 'associateid', 'costofliving', 'salaryquartile', 'salarystructureid', 'updatedby']
	search_fields = ['associatesalaryhistoryid', 'salarymoddate', 'oldsalary', 'newsalary', 'newsalarystructureid', 'performancerating', 'costofliving', 'meritincrease', 'meritamount', 'promotionbonus', 'promotionbonusamount', 'salaryenddate', 'associateid', 'costofliving', 'salaryquartile', 'salarystructureid', 'updatedby']
	list_filter = ['associatesalaryhistoryid', 'salarymoddate', 'oldsalary', 'newsalary', 'newsalarystructureid', 'performancerating', 'costofliving', 'meritincrease', 'meritamount', 'promotionbonus', 'promotionbonusamount', 'salaryenddate', 'associateid', 'costofliving', 'salaryquartile', 'salarystructureid', 'updatedby']
admin.site.register(Associatesalaryhistory, AssociatesalaryhistoryAdmin)

class VacationperiodAdmin(admin.ModelAdmin):
	list_display = ['vacationperiodid', 'startdate', 'enddate', 'alloweddays', 'number', 'associateid']
	search_fields = ['vacationperiodid', 'startdate', 'enddate', 'alloweddays', 'number', 'associateid']
	list_filter = ['vacationperiodid', 'startdate', 'enddate', 'alloweddays', 'number', 'associateid']
admin.site.register(Vacationperiod, VacationperiodAdmin)

class VacationeventAdmin(admin.ModelAdmin):
	list_display = ['vacationeventid', 'startdate', 'enddate', 'days', 'daysbeforeevent', 'periodid']
	search_fields = ['vacationeventid', 'startdate', 'enddate', 'days', 'daysbeforeevent', 'periodid']
	list_filter = ['vacationeventid', 'startdate', 'enddate', 'days', 'daysbeforeevent', 'periodid']
admin.site.register(Vacationevent, VacationeventAdmin)

class AccesscontrolAdmin(admin.ModelAdmin):
	list_display = ['accesscontrolid', 'enrollid', 'cardid', 'priviledge', 'associateid']
	search_fields = ['accesscontrolid', 'enrollid', 'cardid', 'priviledge', 'associateid']
	list_filter = ['accesscontrolid', 'enrollid', 'cardid', 'priviledge', 'associateid']
admin.site.register(Accesscontrol, AccesscontrolAdmin)

class ContracteventAdmin(admin.ModelAdmin):
	list_display = ['contracteventid', 'startdate', 'durationindays', 'alloweddays', 'currentsalary', 'title', 'byproject', 'valid', 'associateid', 'departmentid', 'salarystructureid']
	search_fields = ['contracteventid', 'startdate', 'durationindays', 'alloweddays', 'currentsalary', 'title', 'byproject', 'valid', 'associateid', 'departmentid', 'salarystructureid']
	list_filter = ['contracteventid', 'startdate', 'durationindays', 'alloweddays', 'currentsalary', 'title', 'byproject', 'valid', 'associateid', 'departmentid', 'salarystructureid']
admin.site.register(Contractevent, ContracteventAdmin)

class InventoryAdmin(admin.ModelAdmin):
	list_display = ['itemid', 'type', 'indate', 'name', 'distributor', 'condition', 'location', 'cost', 'serial', 'barcode', 'internalbarcode', 'departmentid']
	search_fields = ['itemid', 'type', 'indate', 'name', 'distributor', 'condition', 'location', 'cost', 'serial', 'barcode', 'internalbarcode', 'departmentid']
	list_filter = ['itemid', 'type', 'indate', 'name', 'distributor', 'condition', 'location', 'cost', 'serial', 'barcode', 'internalbarcode', 'departmentid']
admin.site.register(Inventory, InventoryAdmin)

class AccesscontroldeviceAdmin(admin.ModelAdmin):
	list_display = ['deviceid', 'devicename', 'ip', 'port', 'isssr', 'isusb', 'readscards', 'readsfingerprints']
	search_fields = ['deviceid', 'devicename', 'ip', 'port', 'isssr', 'isusb', 'readscards', 'readsfingerprints']
	list_filter = ['deviceid', 'devicename', 'ip', 'port', 'isssr', 'isusb', 'readscards', 'readsfingerprints']
admin.site.register(Accesscontroldevice, AccesscontroldeviceAdmin)

class TaskstatusAdmin(admin.ModelAdmin):
	list_display = ['taskstatusid', 'taskstatusname']
	search_fields = ['taskstatusid', 'taskstatusname']
	list_filter = ['taskstatusid', 'taskstatusname']
admin.site.register(Taskstatus, TaskstatusAdmin)

class TaskentitytypeAdmin(admin.ModelAdmin):
	list_display = ['entitytypeid', 'entity']
	search_fields = ['entitytypeid', 'entity']
	list_filter = ['entitytypeid', 'entity']
admin.site.register(Taskentitytype, TaskentitytypeAdmin)

class TaskAdmin(admin.ModelAdmin):
	list_display = ['taskid', 'taskname', 'entityid', 'parentid', 'offset', 'offsettypeid', 'duration', 'position', 'hidden', 'bakedstartdate', 'bakedenddate', 'originalstartdate', 'originalenddate', 'idledays', 'isclone', 'isactive', 'entitytypeid', 'projectid', 'taskstatusid']
	search_fields = ['taskid', 'taskname', 'entityid', 'parentid', 'offset', 'offsettypeid', 'duration', 'position', 'hidden', 'bakedstartdate', 'bakedenddate', 'originalstartdate', 'originalenddate', 'idledays', 'isclone', 'isactive', 'entitytypeid', 'projectid', 'taskstatusid']
	list_filter = ['taskid', 'taskname', 'entityid', 'parentid', 'offset', 'offsettypeid', 'duration', 'position', 'hidden', 'bakedstartdate', 'bakedenddate', 'originalstartdate', 'originalenddate', 'idledays', 'isclone', 'isactive', 'entitytypeid', 'projectid', 'taskstatusid']
admin.site.register(Task, TaskAdmin)

class TaskartistAdmin(admin.ModelAdmin):
	list_display = ['id', 'taskid', 'userid']
	search_fields = ['id', 'taskid', 'userid']
	list_filter = ['id', 'taskid', 'userid']
admin.site.register(Taskartist, TaskartistAdmin)

class TaskdependenciesAdmin(admin.ModelAdmin):
	list_display = ['dependencyid', 'taskid']
	search_fields = ['dependencyid', 'taskid']
	list_filter = ['dependencyid', 'taskid']
admin.site.register(Taskdependencies, TaskdependenciesAdmin)

class StorageuseAdmin(admin.ModelAdmin):
	list_display = ['id', 'userid','projectnickname', 'vfxid', 'versionnumber', 'size']
	search_fields = ['id', 'userid','projectnickname', 'vfxid', 'versionnumber', 'size']
	list_filter = ['id', 'userid','projectnickname', 'vfxid', 'versionnumber', 'size']
admin.site.register(Storageuse, StorageuseAdmin)

class WorkdaycalendarAdmin(admin.ModelAdmin):
	list_display = ['workdaycalendarid', 'type', 'date']
	search_fields = ['workdaycalendarid', 'type', 'date']
	list_filter = ['workdaycalendarid', 'type', 'date']
admin.site.register(Workdaycalendar, WorkdaycalendarAdmin)

class SqliteStat1Admin(admin.ModelAdmin):
	list_display = ['tbl', 'idx', 'stat']
	search_fields = ['tbl', 'idx', 'stat']
	list_filter = ['tbl', 'idx', 'stat']
admin.site.register(SqliteStat1, SqliteStat1Admin)