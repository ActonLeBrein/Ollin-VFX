# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from compositekey import db

class Usertypes(models.Model):
    usertype = models.AutoField(primary_key=True, blank=False, null=False, db_column='UserType') # Field name made lowercase.
    typename = models.CharField(max_length=765, db_column='TypeName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'UserTypes'

    def __unicode__(self):
        return u'%s, %s' % (self.usertype, self.typename)

class User(models.Model):
    userid = models.CharField(max_length=135, primary_key=True, blank=False, null=False, db_column='UserID') # Field name made lowercase.
    password = models.CharField(max_length=765, db_column='Password', blank=True) # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True) # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True) # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True) # Field name made lowercase.
    isgroup = models.IntegerField(null=True, db_column='IsGroup', blank=True) # Field name made lowercase.
    usertype = models.IntegerField(null=True, db_column='UserType', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'User'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.userid, self.firstname, self.lastname, self.email, self.isgroup, self.usertype_id)

class Accesscontrolfingerprint(models.Model):
    enrollid = models.IntegerField(primary_key=True, unique=True, db_column='EnrollID') # Field name made lowercase.
    finger = models.IntegerField(null=True, db_column='Finger', blank=True) # Field name made lowercase.
    fingerprint = models.TextField(db_column='Fingerprint', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AccessControlFingerprint'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.enrollid, self.finger, self.fingerprint)

class Status(models.Model):
    status = models.IntegerField(primary_key=True, blank=False, null=False, db_column='Status') # Field name made lowercase.
    statusname = models.TextField(db_column='StatusName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Status'

    def __unicode__(self):
        return u'%s, %s' % (self.status, self.statusname)

class Accesscontrollog(models.Model):
    eventid = models.CharField(primary_key=True, max_length=150, unique=True, db_column='EventID') # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase.
    enrollid = models.IntegerField(null=True, db_column='EnrollID', blank=True) # Field name made lowercase.
    period = models.IntegerField(null=True, db_column='Period', blank=True) # Field name made lowercase.
    method = models.IntegerField(null=True, db_column='Method', blank=True) # Field name made lowercase.
    overrideaction = models.IntegerField(null=True, db_column='OverrideAction', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='Status', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AccessControlLog'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.eventid, self.date, self.enrollid, self.period, self.method, self.status)

"Houston we have a Many To Many (M2M) problem!!!!"
### SOLVED ###
class Loginattempt(models.Model):
    id = db.MultiFieldPK('userid', 'lastattempt', 'attempts')
    attempts = models.IntegerField(null=True, db_column='Attempts', blank=True) # Field name made lowercase.
    lastattempt = models.CharField(max_length=135, db_column='LastAttempt', blank=True) # Field name made lowercase.
    userid = models.CharField(max_length=135, unique=True, db_column='UserID') # Field name made lowercase.
    class Meta:
        db_table = u'LoginAttempt'

    def __unicode__(self):
        return u'%s' % (self.id)

class Usergroup(models.Model):
    groupid = models.CharField(primary_key=True, max_length=255, db_column='GroupID') # Field name made lowercase.
    userid = models.CharField(max_length=765, db_column='UserID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'UserGroup'

    """def get_members(self):
        return "\n".join([p.User.userid+', ' for p in self.userid.all()])"""

    def __unicode__(self):
        return u'%s, %s' % (self.groupid, self.userid)

class Evaluationround(models.Model):
    evaluationroundid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='EvaluationRoundID') # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'EvaluationRound'

    def __unicode__(self):
        return u'%s, %s' % (self.evaluationroundid, self.date)

class Evaluation(models.Model):
    evaluationid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='EvaluationID') # Field name made lowercase.
    technical = models.TextField(db_column='Technical', blank=True) # Field name made lowercase.
    technicalnotes = models.TextField(db_column='TechnicalNotes', blank=True) # Field name made lowercase.
    professional = models.TextField(db_column='Professional', blank=True) # Field name made lowercase.
    professionalnotes = models.TextField(db_column='ProfessionalNotes', blank=True) # Field name made lowercase.
    teamwork = models.TextField(db_column='Teamwork', blank=True) # Field name made lowercase.
    teamworknotes = models.TextField(db_column='TeamworkNotes', blank=True) # Field name made lowercase.
    forceeval = models.TextField(db_column='ForceEval', blank=True) # Field name made lowercase.
    evalapplied = models.TextField(db_column='EvalApplied', blank=True) # Field name made lowercase.
    evaluationdate = models.TextField(db_column='EvaluationDate', blank=True) # Field name made lowercase.
    currentboss = models.CharField(max_length=135, db_column='CurrentBoss', blank=True) # Field name made lowercase.
    evaluated = models.IntegerField(null=True, db_column='Evaluated', blank=True) # Field name made lowercase.
    evaluator = models.IntegerField(null=True, db_column='Evaluator', blank=True) # Field name made lowercase.
    roundid = models.IntegerField(null=True, db_column='RoundID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Evaluation'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.evaluationid, self.evaluated, self.evaluator, self.roundid, self.currentboss, self.evaluationdate)

class Entitytype(models.Model):
    entitytypeid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='EntityTypeID') # Field name made lowercase.
    entityname = models.TextField(db_column='EntityName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'EntityType'

    def __unicode__(self):
        return u'%s, %s' % (self.entitytypeid, self.entityname)

class Comment(models.Model):
    commentid = models.IntegerField(primary_key=True, db_column='CommentID') # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase.
    comment = models.TextField(blank=True)
    entityid = models.IntegerField(null=True, db_column='EntityID', blank=True) # Field name made lowercase.
    entitytypeid = models.IntegerField(null=True, db_column='EntityTypeID', blank=True) # Field name made lowercase.
    userid = models.TextField(db_column='userID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Comment'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.commentid, self.entityid, self.date, self.comment)

class Alarm(models.Model):
    alarmid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='AlarmID') # Field name made lowercase.
    entityid = models.IntegerField(null=True, db_column='EntityID', blank=True) # Field name made lowercase.
    due = models.TextField(db_column='Due', blank=True) # Field name made lowercase.
    what = models.TextField(db_column='What', blank=True) # Field name made lowercase.
    actionid = models.IntegerField(null=True, db_column='ActionID', blank=True) # Field name made lowercase.
    mode = models.IntegerField(null=True, db_column='Mode', blank=True) # Field name made lowercase.
    lastfired = models.TextField(db_column='LastFired', blank=True) # Field name made lowercase.
    entitytypeid = models.IntegerField(null=True, db_column='EntityTypeID', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='Status', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Alarm'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s, %s' % (self.alarmid, self.due, self.what, self.status, self.actionid, self.mode, self.lastfired)

class Alarmreminder(models.Model):
    alarmreminderid = models.IntegerField(primary_key=True, db_column='AlarmReminderID') # Field name made lowercase.
    daysbefore = models.IntegerField(null=True, db_column='DaysBefore', blank=True) # Field name made lowercase.
    fired = models.IntegerField(null=True, db_column='Fired', blank=True) # Field name made lowercase.
    alarmid = models.IntegerField(null=True, db_column='AlarmID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AlarmReminder'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.alarmreminderid, self.daysbefore, self.fired)

"Houston we have a WEIRD problem!!!!"
### SOLVED ###
class Alarmactionparameter(models.Model):
    id = db.MultiFieldPK('alarmid', 'parameter')
    alarmid = models.IntegerField(db_column='AlarmID') # Field name made lowercase.
    parameter = models.TextField(db_column='Parameter') # Field name made lowercase.
    class Meta:
        db_table = u'AlarmActionParameter'

    def __unicode__(self):
        return u'%s' % (self.id)


class Commands(models.Model):
    commandname = models.CharField(primary_key=True, max_length=135, db_column='CommandName') # Field name made lowercase.
    class Meta:
        db_table = u'Commands'

    def __unicode__(self):
        return u'%s' % (self.commandname)

class Priviledgesmatrix(models.Model):
    command = models.CharField(max_length=255, primary_key=True, db_column='Command') # Field name made lowercase.
    number_1 = models.IntegerField(null=True, db_column=u'1', blank=True) # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.IntegerField(null=True, db_column=u'2', blank=True) # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.IntegerField(null=True, db_column=u'3', blank=True) # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.IntegerField(null=True, db_column=u'4', blank=True) # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.IntegerField(null=True, db_column=u'5', blank=True) # Field renamed because it wasn't a valid Python identifier.
    number_6 = models.IntegerField(null=True, db_column=u'6', blank=True) # Field renamed because it wasn't a valid Python identifier.
    number_7 = models.IntegerField(null=True, db_column=u'7', blank=True) # Field renamed because it wasn't a valid Python identifier.
    number_8 = models.IntegerField(null=True, db_column=u'8', blank=True) # Field renamed because it wasn't a valid Python identifier.
    class Meta:
        db_table = u'PriviledgesMatrix'

    def __unicode__(self):
        return u'%s' % (self.command)

"Houston we have another WEIRD problem!!!!"
### SOLVED ###
class Commandrelations(models.Model):
    id = db.MultiFieldPK('command', 'relatedto')
    command = models.CharField(max_length=135, db_column='Command') # Field name made lowercase.
    relatedto = models.CharField(max_length=135, db_column='RelatedTo') # Field name made lowercase.
    class Meta:
        db_table = u'CommandRelations'

    def __unicode__(self):
        return u'%s' % (self.id)

class Extendedpermissions(models.Model):
    command = models.TextField(db_column='Command', blank=True) # Field name made lowercase.
    userid = models.TextField(db_column='UserID', blank=True) # Field name made lowercase.
    action = models.IntegerField(primary_key=True, db_column='Action') # Field name made lowercase.
    class Meta:
        db_table = u'ExtendedPermissions'

    def __unicode__(self):
        return u'%s, %s' % (self.action)

class Notification(models.Model):
    notificationid = models.IntegerField(primary_key=True, db_column='NotificationID') # Field name made lowercase.
    alreadyread = models.IntegerField(null=True, db_column='AlreadyRead', blank=True) # Field name made lowercase.
    typeid = models.IntegerField(null=True, db_column='TypeID', blank=True) # Field name made lowercase.
    from_field = models.TextField(db_column='From', blank=True) # Field name made lowercase. Field renamed because it was a Python reserved word.
    addressedto = models.TextField(db_column='AddressedTo', blank=True) # Field name made lowercase.
    subject = models.TextField(db_column='Subject', blank=True) # Field name made lowercase.
    body = models.TextField(db_column='Body', blank=True) # Field name made lowercase.
    bodyhtml = models.TextField(db_column='BodyHTML', blank=True) # Field name made lowercase.
    datetime = models.TextField(db_column='DateTime', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='Status', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Notification'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s, %s' % (self.notificationid, self.alreadyread, self.status_ID, self.typeid, self.from_field, self.addressedto, self.datetime)

class Notificationmetadata(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ID') # Field name made lowercase.
    notificationid = models.IntegerField(null=True, db_column='NotificationID', blank=True) # Field name made lowercase.
    metadataname = models.TextField(db_column='MetadataName', blank=True) # Field name made lowercase.
    metadatavalue = models.TextField(db_column='MetadataValue', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'NotificationMetadata'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.id, self.MetadataName, self.MetadataValue)

class Project(models.Model):
    projectid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ProjectID') # Field name made lowercase.
    projectname = models.TextField(db_column='ProjectName', blank=True) # Field name made lowercase.
    projectnickname = models.TextField(db_column='ProjectNickname', blank=True) # Field name made lowercase.
    director = models.TextField(db_column='Director', blank=True) # Field name made lowercase.
    producer = models.TextField(db_column='Producer', blank=True) # Field name made lowercase.
    studio = models.TextField(db_column='Studio', blank=True) # Field name made lowercase.
    consumableallowance = models.TextField(db_column='ConsumableAllowance', blank=True) # Field name made lowercase.
    contingency = models.FloatField(null=True, db_column='Contingency', blank=True) # Field name made lowercase.
    thumbnail = models.CharField(max_length=765, db_column='Thumbnail', blank=True) # Field name made lowercase.
    imageassetid = models.IntegerField(null=True, db_column='ImageAssetID', blank=True) # Field name made lowercase.
    oldstructure = models.IntegerField(null=True, db_column='OldStructure', blank=True) # Field name made lowercase.
    active = models.IntegerField(null=True, db_column='Active', blank=True) # Field name made lowercase.
    creationdate = models.TextField(db_column='CreationDate', blank=True) # Field name made lowercase.
    restrictshotstoassignedusers = models.IntegerField(null=True, db_column='RestrictShotsToAssignedUsers', blank=True) # Field name made lowercase.
    startdate = models.TextField(db_column='StartDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Project'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.projectid, self.projectname, self.projectnickname, self.director, self.producer, self.studio)

class Milestone(models.Model):
    milestoneid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='MilestoneID') # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True) # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Milestone'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.milestoneid, self.name, self.date)

class Incomingfile(models.Model):
    incomingfileid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='IncomingFileID') # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase.
    sender = models.TextField(db_column='Sender', blank=True) # Field name made lowercase.
    addressedto = models.TextField(db_column='AddressedTo', blank=True) # Field name made lowercase.
    sourcepath = models.TextField(db_column='SourcePath', blank=True) # Field name made lowercase.
    finalpath = models.TextField(db_column='FinalPath', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    tags = models.TextField(db_column='Tags', blank=True) # Field name made lowercase.
    area = models.TextField(db_column='Area', blank=True) # Field name made lowercase.
    media = models.TextField(db_column='Media', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IncomingFile'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.incomingfileid, self.date, self.sender, self.addressedto, self.area, self.media)

"And yet Houston we have another WEIRD problem!!!!"
### SOLVED ###
class Projectuser(models.Model):
    id = db.MultiFieldPK('userid', 'projectid')
    userid = models.CharField(max_length=765, db_column='UserID', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ProjectUser'

    def __unicode__(self):
        return u'%s' % (self.id)

class Playlist(models.Model):
    playlistid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='PlaylistID') # Field name made lowercase.
    playlistname = models.TextField(db_column='PlaylistName', blank=True) # Field name made lowercase.
    playlistxml = models.TextField(db_column='PlaylistXML', blank=True) # Field name made lowercase.
    autoupdate = models.TextField(db_column='AutoUpdate', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Playlist'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.playlistid, self.playlistname, self.playlistxml, self.autoupdate)

class Rateset(models.Model):
    ratesetid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='RateSetID') # Field name made lowercase.
    ratesetnumber = models.IntegerField(null=True, db_column='RateSetNumber', blank=True) # Field name made lowercase.
    ratesetname = models.TextField(db_column='RateSetName', blank=True) # Field name made lowercase.
    ratesetnotes = models.TextField(db_column='RateSetNotes', blank=True) # Field name made lowercase.
    ratesetcreationdate = models.TextField(db_column='RateSetCreationDate', blank=True) # Field name made lowercase.
    ratesetlastmodification = models.TextField(db_column='RateSetLastModification', blank=True) # Field name made lowercase.
    ratesetconsumableallowance = models.TextField(db_column='RateSetConsumableAllowance', blank=True) # Field name made lowercase.
    ratesetcontingency = models.TextField(db_column='RateSetContingency', blank=True) # Field name made lowercase.
    ratesetextra = models.TextField(db_column='RateSetExtra', blank=True) # Field name made lowercase.
    ratesetextrait = models.TextField(db_column='RateSetExtraIT', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RateSet'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.ratesetid, self.ratesetnumber, self.ratesetname, self.ratesetcreationdate, self.ratesetlastmodification)

class Harddiskstatus(models.Model):
    harddiskstatusid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='HardDiskStatusID') # Field name made lowercase.
    harddiskstatusname = models.TextField(db_column='HardDiskStatusName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'HardDiskStatus'

    def __unicode__(self):
        return u'%s, %s' % (self.harddiskstatusid, self.harddiskstatusname)

class Harddiskregister(models.Model):
    harddiskregisterid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='HardDiskRegisterID') # Field name made lowercase.
    serialnumber = models.TextField(db_column='SerialNumber', blank=True) # Field name made lowercase.
    harddisknumber = models.IntegerField(null=True, db_column='HardDiskNumber', blank=True) # Field name made lowercase.
    harddiskname = models.TextField(db_column='HardDiskName', blank=True) # Field name made lowercase.
    fromaddress = models.TextField(db_column='FromAddress', blank=True) # Field name made lowercase.
    contentonarrival = models.TextField(db_column='ContentOnArrival', blank=True) # Field name made lowercase.
    arrivaldate = models.TextField(db_column='ArrivalDate', blank=True) # Field name made lowercase.
    contentonexit = models.TextField(db_column='ContentOnExit', blank=True) # Field name made lowercase.
    exitdate = models.TextField(db_column='ExitDate', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    statusid = models.IntegerField(null=True, db_column='StatusID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'HardDiskRegister'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.harddiskregisterid, self.serialnumber, self.harddisknumber, self.harddiskname, self.fromaddress)

class Uploadcontrol(models.Model):
    uploadcontrolid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='UploadControlID') # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True) # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True) # Field name made lowercase.
    date = models.DateTimeField(null=True, db_column='Date', blank=True) # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    userid = models.CharField(max_length=765, db_column='UserID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'UploadControl'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.uploadcontrolid, self.filename, self.path, self.date)

class Servicetype(models.Model):
    servicetypeid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ServiceTypeID') # Field name made lowercase.
    servicetypename = models.TextField(db_column='ServiceTypeName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ServiceType'

    def __unicode__(self):
        return u'%s, %s' % (self.servicetypeid, self.servicetypename)

class Service(models.Model):
    serviceid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ServiceID') # Field name made lowercase.
    servicename = models.TextField(db_column='ServiceName', blank=True) # Field name made lowercase.
    costperday = models.FloatField(null=True, db_column='CostPerDay', blank=True) # Field name made lowercase.
    servicetypeid = models.IntegerField(null=True, db_column='ServiceTypeID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Service'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.serviceid, self.servicename, self.costperday)

class Servicehistogramcolor(models.Model):
    servicehistogramcolorid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ServiceHistogramColorID') # Field name made lowercase.
    r = models.IntegerField(null=True, db_column='R', blank=True) # Field name made lowercase.
    g = models.IntegerField(null=True, db_column='G', blank=True) # Field name made lowercase.
    b = models.IntegerField(null=True, db_column='B', blank=True) # Field name made lowercase.
    serviceid = models.IntegerField(null=True, db_column='ServiceID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ServiceHistogramColor'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.servicehistogramcolorid, self.r, self.g, self.b)

class Projectservice(models.Model):
    projectserviceid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ProjectServiceID') # Field name made lowercase.
    rate = models.TextField(db_column='Rate', blank=True) # Field name made lowercase.
    ratesetnumber = models.IntegerField(null=True, db_column='RateSetNumber', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    serviceid = models.IntegerField(null=True, db_column='ServiceID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ProjectService'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.projectserviceid, self.rate, self.ratesetnumber)

class Projecttaskservice(models.Model):
    projecttaskserviceid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ProjectTaskServiceID') # Field name made lowercase.
    slots = models.IntegerField(null=True, db_column='Slots', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    serviceid = models.IntegerField(null=True, db_column='ServiceID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ProjectTaskService'

    def __unicode__(self):
        return u'%s, %s' % (self.projecttaskserviceid, self.slots)

class Assettype(models.Model):
    assettypeid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='AssetTypeID') # Field name made lowercase.
    assettypename = models.TextField(db_column='AssetTypeName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AssetType'

    def __unicode__(self):
        return u'%s, %s' % (self.assettypeid, self.assettypename)

class Sequencialidgenerator(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, editable=False)
    class Meta:
        db_table = u'SequencialIDGenerator'

    def __unicode__(self):
        return u'%s' % (self.id)

class Sequence(models.Model):
    sequenceid = models.IntegerField(primary_key=True, db_column='SequenceID') # Field name made lowercase.
    sequencename = models.TextField(db_column='SequenceName', blank=True) # Field name made lowercase.
    sequencenickname = models.TextField(db_column='SequenceNickname', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Sequence'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.sequenceid, self.sequencename, self.sequencenickname)

class Shot(models.Model):
    shotid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ShotID') # Field name made lowercase.
    vfxid = models.TextField(db_column='VFXID', blank=True) # Field name made lowercase.
    externalid = models.TextField(db_column='ExternalID', blank=True) # Field name made lowercase.
    shotname = models.TextField(db_column='ShotName', blank=True) # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True) # Field name made lowercase.
    cameramotion = models.TextField(db_column='CameraMotion', blank=True) # Field name made lowercase.
    scenenumber = models.TextField(db_column='SceneNumber', blank=True) # Field name made lowercase.
    pagenumber = models.TextField(db_column='PageNumber', blank=True) # Field name made lowercase.
    frames = models.IntegerField(null=True, db_column='Frames', blank=True) # Field name made lowercase.
    directornotes = models.TextField(db_column='DirectorNotes', blank=True) # Field name made lowercase.
    shotdescription = models.TextField(db_column='ShotDescription', blank=True) # Field name made lowercase.
    thumbnail = models.TextField(db_column='Thumbnail', blank=True) # Field name made lowercase.
    imageassetid = models.IntegerField(null=True, db_column='ImageAssetID', blank=True) # Field name made lowercase.
    addconsumablesallowance = models.TextField(db_column='AddConsumablesAllowance', blank=True) # Field name made lowercase.
    workedby = models.TextField(db_column='WorkedBy', blank=True) # Field name made lowercase.
    type = models.IntegerField(null=True, db_column='Type', blank=True) # Field name made lowercase.
    lens = models.TextField(db_column='Lens', blank=True) # Field name made lowercase.
    primarybidnumber = models.IntegerField(null=True, db_column='PrimaryBidNumber', blank=True) # Field name made lowercase.
    vfxtasks = models.TextField(db_column='VFXTasks', blank=True) # Field name made lowercase.
    isreference = models.IntegerField(null=True, db_column='IsReference', blank=True) # Field name made lowercase.
    sortindex = models.IntegerField(null=True, db_column='SortIndex', blank=True) # Field name made lowercase.
    take = models.IntegerField(null=True, db_column='Take', blank=True) # Field name made lowercase.
    active = models.IntegerField(null=True, db_column='Active', blank=True) # Field name made lowercase.
    projectid = models.TextField(db_column='ProjectID', blank=True) # Field name made lowercase.
    sequenceid = models.IntegerField(null=True, db_column='SequenceID', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='Status', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Shot'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.shotid, self.vfxid, self.shotname, self.scenenumber)

class Bid(models.Model):
    bidid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='BidID') # Field name made lowercase.
    bidname = models.TextField(db_column='BidName', blank=True) # Field name made lowercase.
    biddate = models.TextField(db_column='BidDate', blank=True) # Field name made lowercase.
    bidnotes = models.TextField(db_column='BidNotes', blank=True) # Field name made lowercase.
    bidlastmodification = models.TextField(db_column='BidLastModification', blank=True) # Field name made lowercase.
    addconsumablesallowance = models.IntegerField(null=True, db_column='AddConsumablesAllowance', blank=True) # Field name made lowercase.
    bidnumber = models.IntegerField(null=True, db_column='BidNumber', blank=True) # Field name made lowercase.
    ratesetnumber = models.IntegerField(null=True, db_column='RateSetNumber', blank=True) # Field name made lowercase.
    hideincalendar = models.IntegerField(null=True, db_column='HideInCalendar', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Bid'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.bidid, self.bidnumber, self.bidname, self.biddate, self.bidlastmodification)

class Assets(models.Model):
    assetid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='AssetID') # Field name made lowercase.
    assetname = models.TextField(db_column='AssetName', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True) # Field name made lowercase.
    size = models.BigIntegerField(null=True, db_column='Size', blank=True) # Field name made lowercase.
    uploaddate = models.TextField(db_column='uploadDate', blank=True) # Field name made lowercase.
    public = models.IntegerField(null=True, db_column='Public', blank=True) # Field name made lowercase.
    tags = models.TextField(blank=True)
    parent = models.IntegerField(null=True, blank=True)
    lastmodified = models.TextField(db_column='lastModified', blank=True) # Field name made lowercase.
    oncloud = models.IntegerField(null=True, db_column='OnCloud', blank=True) # Field name made lowercase.
    cloudstatus = models.IntegerField(null=True, db_column='CloudStatus', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    typeid = models.IntegerField(null=True, db_column='TypeID', blank=True) # Field name made lowercase.
    uploader = models.TextField(blank=True)
    class Meta:
        db_table = u'Assets'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s, %s' % (self.assetid, self.assetname, self.path, self.size, self.public, self.uploaddate, self.lastmodified)

class Transfer(models.Model):
    transferid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='TransferID') # Field name made lowercase.
    type = models.IntegerField(null=True, db_column='Type', blank=True) # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase.
    ip = models.CharField(max_length=135, db_column='IP', blank=True) # Field name made lowercase.
    assetid = models.IntegerField(null=True, db_column='AssetID', blank=True) # Field name made lowercase.
    userid = models.TextField(db_column='UserID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Transfer'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.transferid, self.type, self.ip, self.date)

"And yet Houston we have another WEIRD problem again!!!!"
### SOLVED ###
class Assetpriviledges(models.Model):
    id = db.MultiFieldPK('assetid', 'usertype')
    assetid = models.IntegerField(db_column='AssetID') # Field name made lowercase.
    usertype = models.IntegerField(null=True, db_column='UserType', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AssetPriviledges'

    def __unicode__(self):
        return u'%s' % (self.id)

class Deletedassets(models.Model):
    deletedassetid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='DeletedAssetID') # Field name made lowercase.
    assetname = models.TextField(db_column='AssetName', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True) # Field name made lowercase.
    typeid = models.IntegerField(null=True, db_column='TypeID', blank=True) # Field name made lowercase.
    size = models.IntegerField(null=True, db_column='Size', blank=True) # Field name made lowercase.
    uploaddate = models.TextField(db_column='uploadDate', blank=True) # Field name made lowercase.
    public = models.IntegerField(null=True, db_column='Public', blank=True) # Field name made lowercase.
    tags = models.TextField(blank=True)
    assetid = models.IntegerField(null=True, db_column='AssetID', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    uploader = models.TextField(blank=True)
    class Meta:
        db_table = u'DeletedAssets'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.deletedassetid, self.assetname, self.path, self.size, self.public, self.uploaddate)

class Downloadcontrol(models.Model):
    downloadcontrolid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='DownloadControlID') # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True) # Field name made lowercase.
    date = models.DateTimeField(null=True, db_column='Date', blank=True) # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True) # Field name made lowercase.
    assetid = models.IntegerField(null=True, db_column='AssetID', blank=True) # Field name made lowercase.
    userid = models.CharField(max_length=765, db_column='UserID') # Field name made lowercase.
    class Meta:
        db_table = u'DownloadControl'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.downloadcontrolid, self.path, self.date)

class Shotsservice(models.Model):
    shotserviceid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ShotServiceID') # Field name made lowercase.
    days = models.TextField(db_column='Days', blank=True) # Field name made lowercase.
    bidnumber = models.IntegerField(null=True, db_column='BidNumber', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    serviceid = models.IntegerField(null=True, db_column='ServiceID', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ShotsService'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.shotserviceid, self.days, self.bidnumber)

class Shotsassets(models.Model):
    shotsassetsid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ShotsAssetsID') # Field name made lowercase.
    assetid = models.IntegerField(null=True, db_column='AssetID', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ShotsAssets'

    def __unicode__(self):
        return u'%s' % (self.shotsassetsid)

class Shotstatuslog(models.Model):
    shotstatuslogid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ShotStatusLogID') # Field name made lowercase.
    fromstatus = models.TextField(db_column='FromStatus', blank=True) # Field name made lowercase.
    tostatus = models.TextField(db_column='ToStatus', blank=True) # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    userid = models.TextField(db_column='UserID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ShotStatusLog'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.shotstatuslogid, self.fromstatus, self.tostatus, self.date)

class Shotdelivery(models.Model):
    shotdeliveryid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ShotDeliveryID') # Field name made lowercase.
    vfxid = models.CharField(max_length=135, db_column='VFXID', blank=True) # Field name made lowercase.
    shotname = models.CharField(max_length=135, db_column='ShotName', blank=True) # Field name made lowercase.
    reviewdate = models.DateField(null=True, db_column='ReviewDate', blank=True) # Field name made lowercase.
    internalcomments = models.TextField(db_column='InternalComments', blank=True) # Field name made lowercase.
    clientcomments = models.TextField(db_column='ClientComments', blank=True) # Field name made lowercase.
    internalversion = models.CharField(max_length=135, db_column='InternalVersion', blank=True) # Field name made lowercase.
    clientversion = models.CharField(max_length=135, db_column='ClientVersion', blank=True) # Field name made lowercase.
    work = models.CharField(max_length=135, db_column='Work', blank=True) # Field name made lowercase.
    stereo = models.CharField(max_length=135, db_column='Stereo', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='Status', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ShotDelivery'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.shotdeliveryid, self.vfxid, self.shotname, self.reviewdate)

class Shotgroup(models.Model):
    shotgroupid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ShotGroupID') # Field name made lowercase.
    shotgroupname = models.CharField(max_length=135, db_column='ShotGroupName', blank=True) # Field name made lowercase.
    shotgroupnotes = models.TextField(db_column='ShotGroupNotes', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ShotGroup'

    def __unicode__(self):
        return u'%s, %s' % (self.shotgroupid, self.shotgroupname)

"And yet Houston we have another freaking WEIRD problem again!!!!"
### SOLVED ###
class Shotgroupshotid(models.Model):
    id = db.MultiFieldPK('shotgroupid', 'shotid')
    shotgroupid = models.IntegerField(db_column='ShotGroupID') # Field name made lowercase.
    shotid = models.IntegerField(db_column='ShotID') # Field name made lowercase.
    class Meta:
        db_table = u'ShotGroupShotID'

    def __unicode__(self):
        return u'%s' % (self.id)

"Houston we have a HUGE problem!!!!"
### SOLVED ###
class Shotgrouptentpole(models.Model):
    id = db.MultiFieldPK('shotgroupid', 'shotid')
    shotgroupid = models.IntegerField(db_column='ShotGroupID') # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ShotGroupTentpole'

    def __unicode__(self):
        return u'%s' % (self.id)

"Houston we have another BADASS problem!!!!"
### SOLVED ###
class Shotuser(models.Model):
    id = db.MultiFieldPK('shotid', 'userid')
    shotid = models.IntegerField(db_column='ShotID') # Field name made lowercase.
    userid = models.CharField(max_length=765, db_column='UserID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ShotUser'

    def __unicode__(self):
        return u'%s' % (self.id)

class Selectionset(models.Model):
    selectionsetid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='SelectionSetID') # Field name made lowercase.
    selectionsetname = models.TextField(db_column='SelectionSetName', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SelectionSet'

    def __unicode__(self):
        return u'%s, %s' % (self.selectionsetid, self.selectionsetname)

class Shotselectionset(models.Model):
    shotselectionsetid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ShotSelectionSetID') # Field name made lowercase.
    selectionsetid = models.IntegerField(null=True, db_column='SelectionSetID', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ShotSelectionSet'

    def __unicode__(self):
        return u'%s' % (self.shotselectionsetid)

class Customshotfield(models.Model):
    customshotfieldid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='CustomShotFieldID') # Field name made lowercase.
    fieldname = models.TextField(db_column='FieldName') # Field name made lowercase.
    defaultvalue = models.TextField(db_column='DefaultValue', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(db_column='ProjectID') # Field name made lowercase.
    class Meta:
        db_table = u'CustomShotField'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.customshotfieldid, self.fieldname, self.defaultvalue)

class Shotcustomshotfield(models.Model):
    shotcustomshotfieldid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ShotCustomShotFieldID') # Field name made lowercase.
    value = models.TextField(db_column='Value') # Field name made lowercase.
    customshotfieldid = models.IntegerField(db_column='CustomShotFieldID') # Field name made lowercase.
    shotid = models.IntegerField(db_column='ShotID') # Field name made lowercase.
    class Meta:
        db_table = u'ShotCustomShotField'

    def __unicode__(self):
        return u'%s, %s' % (self.shotcustomshotfieldid, self.value)

class Version(models.Model):
    versionid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='VersionID') # Field name made lowercase.
    major = models.TextField(db_column='Major', blank=True) # Field name made lowercase.
    minor = models.TextField(db_column='Minor', blank=True) # Field name made lowercase.
    external = models.TextField(db_column='External', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    tags = models.TextField(db_column='Tags', blank=True) # Field name made lowercase.
    view = models.TextField(db_column='View', blank=True) # Field name made lowercase.
    task = models.TextField(db_column='Task', blank=True) # Field name made lowercase.
    publishedby = models.TextField(db_column='PublishedBy', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Version'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.versionid, self.major, self.minor, self.external, self.creationdate)

class Versionasset(models.Model):
    versionassetid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='VersionAssetID') # Field name made lowercase.
    assetid = models.IntegerField(null=True, db_column='AssetID', blank=True) # Field name made lowercase.
    versionid = models.IntegerField(null=True, db_column='VersionID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'VersionAsset'

    def __unicode__(self):
        return u'%s' % (self.versionassetid)

class Script(models.Model):
    scriptid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ScriptID') # Field name made lowercase.
    scriptname = models.TextField(db_column='ScriptName', blank=True) # Field name made lowercase.
    majorversion = models.CharField(max_length=15, db_column='MajorVersion', blank=True) # Field name made lowercase.
    minorversion = models.CharField(max_length=15, db_column='MinorVersion', blank=True) # Field name made lowercase.
    task = models.CharField(max_length=135, db_column='Task', blank=True) # Field name made lowercase.
    stask = models.CharField(max_length=135, db_column='STask', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    userid = models.CharField(max_length=135, db_column='UserID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Script'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.scriptid, self.scriptname, self.majorversion, self.minorversion, self.task)

class Publishjob(models.Model):
    jobid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='JobID') # Field name made lowercase.
    creationdate = models.CharField(max_length=135, db_column='CreationDate', blank=True) # Field name made lowercase.
    publishdate = models.CharField(max_length=135, db_column='PublishDate', blank=True) # Field name made lowercase.
    publishtype = models.CharField(max_length=135, db_column='PublishType', blank=True) # Field name made lowercase.
    createdby = models.CharField(max_length=135, db_column='CreatedBy', blank=True) # Field name made lowercase.
    scriptid = models.IntegerField(null=True, db_column='ScriptID', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='Status', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'PublishJob'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.jobid, self.createdby, self.publishtype, self.creationdate, self.publishdate)

class Lineup(models.Model):
    lineupid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='LineUpID') # Field name made lowercase.
    creationdate = models.TextField(db_column='CreationDate', blank=True) # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True) # Field name made lowercase.
    camera = models.TextField(db_column='Camera', blank=True) # Field name made lowercase.
    tstop = models.TextField(db_column='TStop', blank=True) # Field name made lowercase.
    framesize = models.TextField(db_column='FrameSize', blank=True) # Field name made lowercase.
    cutlengthframes = models.TextField(db_column='CutLengthFrames', blank=True) # Field name made lowercase.
    inframe = models.TextField(db_column='InFrame', blank=True) # Field name made lowercase.
    intc = models.TextField(db_column='InTC', blank=True) # Field name made lowercase.
    outframe = models.TextField(db_column='OutFrame', blank=True) # Field name made lowercase.
    outtc = models.TextField(db_column='OutTC', blank=True) # Field name made lowercase.
    frameswithhandles = models.TextField(db_column='FramesWithHandles', blank=True) # Field name made lowercase.
    inframewithhandles = models.TextField(db_column='InFrameWithHandles', blank=True) # Field name made lowercase.
    intcwithhandles = models.TextField(db_column='InTCWithHandles', blank=True) # Field name made lowercase.
    outframewithhandles = models.TextField(db_column='OutFrameWithHandles', blank=True) # Field name made lowercase.
    outtcwithhandles = models.TextField(db_column='OutTCWithHandles', blank=True) # Field name made lowercase.
    rawmediastart = models.TextField(db_column='RawMediaStart', blank=True) # Field name made lowercase.
    rawmediaend = models.TextField(db_column='RawMediaEnd', blank=True) # Field name made lowercase.
    rawmediaduration = models.TextField(db_column='RawMediaDuration', blank=True) # Field name made lowercase.
    rawmediastartframe = models.TextField(db_column='RawMediaStartFrame', blank=True) # Field name made lowercase.
    rawmediaendframe = models.TextField(db_column='RawMediaEndFrame', blank=True) # Field name made lowercase.
    rawmediadurationframes = models.TextField(db_column='RawMediaDurationFrames', blank=True) # Field name made lowercase.
    editorialname = models.TextField(db_column='EditorialName', blank=True) # Field name made lowercase.
    edlpull = models.TextField(db_column='EDLPull', blank=True) # Field name made lowercase.
    elementdescription = models.TextField(db_column='ElementDescription', blank=True) # Field name made lowercase.
    format = models.TextField(db_column='Format', blank=True) # Field name made lowercase.
    iso = models.TextField(db_column='ISO', blank=True) # Field name made lowercase.
    kelvin = models.TextField(db_column='Kelvin', blank=True) # Field name made lowercase.
    lens = models.TextField(db_column='Lens', blank=True) # Field name made lowercase.
    reel = models.TextField(db_column='Reel', blank=True) # Field name made lowercase.
    reelid = models.TextField(db_column='ReelID', blank=True) # Field name made lowercase.
    scene = models.TextField(db_column='Scene', blank=True) # Field name made lowercase.
    scenedescription = models.TextField(db_column='SceneDescription', blank=True) # Field name made lowercase.
    setup = models.TextField(db_column='Setup', blank=True) # Field name made lowercase.
    shootdate = models.TextField(db_column='ShootDate', blank=True) # Field name made lowercase.
    shootday = models.TextField(db_column='ShootDay', blank=True) # Field name made lowercase.
    shotdescription = models.TextField(db_column='ShotDescription', blank=True) # Field name made lowercase.
    shuttleangle = models.TextField(db_column='ShuttleAngle', blank=True) # Field name made lowercase.
    shutterspeed = models.TextField(db_column='ShutterSpeed', blank=True) # Field name made lowercase.
    slugline = models.TextField(db_column='SlugLine', blank=True) # Field name made lowercase.
    speed = models.TextField(db_column='Speed', blank=True) # Field name made lowercase.
    stabilizecurvessent = models.IntegerField(null=True, db_column='StabilizeCurvesSent', blank=True) # Field name made lowercase.
    take = models.TextField(db_column='Take', blank=True) # Field name made lowercase.
    tint = models.TextField(db_column='Tint', blank=True) # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    shotid = models.IntegerField(null=True, db_column='ShotID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Lineup'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.lineupid, self.name, self.camera, self.creationdate)

class Salarygeneraldata(models.Model):
    maxsalaryinc = models.TextField(primary_key=True, blank=False, null=False, editable=True, db_column='MaxSalaryInc') # Field name made lowercase.
    cpimx = models.FloatField(null=True, db_column='CPIMX', blank=True) # Field name made lowercase.
    cpiusa = models.FloatField(null=True, db_column='CPIUSA', blank=True) # Field name made lowercase.
    cpiadjuststrategy = models.IntegerField(null=True, db_column='CPIAdjustStrategy', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SalaryGeneralData'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.maxsalaryinc, self.cpimx, self.cpiusa, self.cpiadjuststrategy)

class Salarystructure(models.Model):
    salarystructureid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='SalaryStructureID') # Field name made lowercase.
    salaryname = models.TextField(db_column='SalaryName', blank=True) # Field name made lowercase.
    salarydefinition = models.TextField(db_column='SalaryDefinition', blank=True) # Field name made lowercase.
    salarymidrange = models.FloatField(null=True, db_column='SalaryMidRange', blank=True) # Field name made lowercase.
    levelincrease = models.FloatField(null=True, db_column='LevelIncrease', blank=True) # Field name made lowercase.
    currencytype = models.IntegerField(null=True, db_column='CurrencyType', blank=True) # Field name made lowercase.
    salary1 = models.FloatField(null=True, db_column='Salary1', blank=True) # Field name made lowercase.
    salary2 = models.FloatField(null=True, db_column='Salary2', blank=True) # Field name made lowercase.
    salary3 = models.FloatField(null=True, db_column='Salary3', blank=True) # Field name made lowercase.
    salary4 = models.FloatField(null=True, db_column='Salary4', blank=True) # Field name made lowercase.
    salary5 = models.FloatField(null=True, db_column='Salary5', blank=True) # Field name made lowercase.
    salary6 = models.FloatField(null=True, db_column='Salary6', blank=True) # Field name made lowercase.
    salary7 = models.FloatField(null=True, db_column='Salary7', blank=True) # Field name made lowercase.
    salary8 = models.FloatField(null=True, db_column='Salary8', blank=True) # Field name made lowercase.
    salary9 = models.FloatField(null=True, db_column='Salary9', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SalaryStructure'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.salarystructureid, self.salaryname, self.salarydefinition, self.salarymidrange, self.levelincrease, self.currencytype)

class Department(models.Model):
    departmentid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='DepartmentID') # Field name made lowercase.
    departmentname = models.TextField(db_column='DepartmentName', blank=True) # Field name made lowercase.
    departmentheadid = models.IntegerField(null=True, db_column='DepartmentHeadID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Department'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.departmentid, self.departmentname, self.departmentheadid)

class Associate(models.Model):
    associateid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='AssociateID') # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True) # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True) # Field name made lowercase.
    active = models.IntegerField(null=True, db_column='Active', blank=True) # Field name made lowercase.
    currentsalary = models.FloatField(null=True, db_column='CurrentSalary', blank=True) # Field name made lowercase.
    lastincrease = models.TextField(db_column='LastIncrease', blank=True) # Field name made lowercase.
    lastcolincrease = models.TextField(db_column='LastCOLIncrease', blank=True) # Field name made lowercase.
    increaseapply = models.IntegerField(null=True, db_column='IncreaseApply', blank=True) # Field name made lowercase.
    bossid = models.IntegerField(null=True, db_column='BossID', blank=True) # Field name made lowercase.
    firsthired = models.TextField(db_column='FirstHired', blank=True) # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True) # Field name made lowercase.
    jobdescription = models.TextField(db_column='JobDescription', blank=True) # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True) # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True) # Field name made lowercase.
    alloweddaysperyear = models.FloatField(null=True, db_column='AllowedDaysPerYear', blank=True) # Field name made lowercase.
    departmentid = models.IntegerField(null=True, db_column='DepartmentID', blank=True) # Field name made lowercase.
    salarystructureid = models.IntegerField(null=True, db_column='SalaryStructureID', blank=True) # Field name made lowercase.
    userid = models.TextField(db_column='UserID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Associate'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.associateid, self.firstname, self.lastname, self.title, self.active, self.currentsalary, self.lastincrease, self.lastcolincrease, self.firsthired)

class Col(models.Model):
    colid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='COLID') # Field name made lowercase.
    name = models.CharField(max_length=135, db_column='Name', blank=True) # Field name made lowercase.
    year = models.CharField(max_length=135, db_column='Year', blank=True) # Field name made lowercase.
    col = models.FloatField(null=True, db_column='COL', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'COL'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.colid, self.name, self.year, self.col)

class Meritpercentages(models.Model):
    salaryquartile = models.TextField(primary_key=True, db_column='SalaryQuartile') # Field name made lowercase.
    rate0 = models.FloatField(null=True, db_column='Rate0', blank=True) # Field name made lowercase.
    rate1 = models.FloatField(null=True, db_column='Rate1', blank=True) # Field name made lowercase.
    rate2 = models.FloatField(null=True, db_column='Rate2', blank=True) # Field name made lowercase.
    rate3 = models.FloatField(null=True, db_column='Rate3', blank=True) # Field name made lowercase.
    rate4 = models.FloatField(null=True, db_column='Rate4', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'MeritPercentages'

    def __unicode__(self):
        return u'%s, %s' % (self.id, self.salaryquartile)

class Associatesalaryhistory(models.Model):
    associatesalaryhistoryid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='AssociateSalaryHistoryID') # Field name made lowercase.
    salarymoddate = models.TextField(db_column='SalaryModDate', blank=True) # Field name made lowercase.
    oldsalary = models.FloatField(null=True, db_column='OldSalary', blank=True) # Field name made lowercase.
    newsalary = models.FloatField(null=True, db_column='NewSalary', blank=True) # Field name made lowercase.
    newsalarystructureid = models.IntegerField(null=True, db_column='NewSalaryStructureID', blank=True) # Field name made lowercase.
    performancerating = models.TextField(db_column='PerformanceRating', blank=True) # Field name made lowercase.
    meritincrease = models.FloatField(null=True, db_column='MeritIncrease', blank=True) # Field name made lowercase.
    meritamount = models.FloatField(null=True, db_column='MeritAmount', blank=True) # Field name made lowercase.
    promotionbonus = models.FloatField(null=True, db_column='PromotionBonus', blank=True) # Field name made lowercase.
    promotionbonusamount = models.FloatField(null=True, db_column='PromotionBonusAmount', blank=True) # Field name made lowercase.
    salaryenddate = models.TextField(db_column='SalaryEndDate', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    associateid = models.IntegerField(null=True, db_column='AssociateID', blank=True) # Field name made lowercase.
    costofliving = models.FloatField(null=True, db_column='CostOfLiving', blank=True) # Field name made lowercase.
    salaryquartile = models.IntegerField(null=True, db_column='SalaryQuartile', blank=True) # Field name made lowercase.
    salarystructureid = models.IntegerField(null=True, db_column='SalaryStructureID', blank=True) # Field name made lowercase.
    updatedby = models.CharField(max_length=135, db_column='UpdatedBy', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AssociateSalaryHistory'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.associatesalaryhistoryid, self.salarymoddate, self.oldsalary, self.newsalary, self.updatedby)

class Vacationperiod(models.Model):
    vacationperiodid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='VacationPeriodID') # Field name made lowercase.
    startdate = models.TextField(db_column='StartDate', blank=True) # Field name made lowercase.
    enddate = models.TextField(db_column='EndDate', blank=True) # Field name made lowercase.
    alloweddays = models.FloatField(null=True, db_column='AllowedDays', blank=True) # Field name made lowercase.
    number = models.IntegerField(null=True, db_column='Number', blank=True) # Field name made lowercase.
    associateid = models.IntegerField(null=True, db_column='AssociateID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'VacationPeriod'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.vacationperiodid,self.startdate, self.enddate, self.alloweddays, self.number)

class Vacationevent(models.Model):
    vacationeventid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='VacationEventID') # Field name made lowercase.
    startdate = models.TextField(db_column='StartDate', blank=True) # Field name made lowercase.
    enddate = models.TextField(db_column='EndDate', blank=True) # Field name made lowercase.
    days = models.FloatField(null=True, db_column='Days', blank=True) # Field name made lowercase.
    daysbeforeevent = models.FloatField(null=True, db_column='DaysBeforeEvent', blank=True) # Field name made lowercase.
    periodid = models.IntegerField(null=True, db_column='PeriodID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'VacationEvent'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.vacationeventid, self.periodid, self.StartDate, self.EndDate, self.Days, self.DaysBeforeEvent)

class Accesscontrol(models.Model):
    accesscontrolid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='AccessControlID') # Field name made lowercase.
    enrollid = models.IntegerField(null=True, db_column='EnrollID', blank=True) # Field name made lowercase.
    cardid = models.TextField(db_column='CardID', blank=True) # Field name made lowercase.
    priviledge = models.IntegerField(null=True, db_column='Priviledge', blank=True) # Field name made lowercase.
    associateid = models.IntegerField(null=True, db_column='AssociateID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AccessControl'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.accesscontrolid, self.enrollid, self.cardid, self.priviledge)

class Contractevent(models.Model):
    contracteventid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ContractEventID') # Field name made lowercase.
    startdate = models.TextField(db_column='StartDate', blank=True) # Field name made lowercase.
    durationindays = models.IntegerField(null=True, db_column='DurationInDays', blank=True) # Field name made lowercase.
    alloweddays = models.FloatField(null=True, db_column='AllowedDays', blank=True) # Field name made lowercase.
    currentsalary = models.FloatField(null=True, db_column='CurrentSalary', blank=True) # Field name made lowercase.
    jobdescription = models.TextField(db_column='JobDescription', blank=True) # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True) # Field name made lowercase.
    byproject = models.IntegerField(null=True, db_column='ByProject', blank=True) # Field name made lowercase.
    valid = models.IntegerField(null=True, db_column='Valid', blank=True) # Field name made lowercase.
    associateid = models.IntegerField(null=True, db_column='AssociateID', blank=True) # Field name made lowercase.
    departmentid = models.IntegerField(null=True, db_column='DepartmentID', blank=True) # Field name made lowercase.
    salarystructureid = models.IntegerField(null=True, db_column='SalaryStructureID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ContractEvent'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.contracteventid, self.startdate, self.durationindays, self.alloweddays, self.currentsalary, self.title)

class Inventory(models.Model):
    itemid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='ItemID') # Field name made lowercase.
    type = models.IntegerField(null=True, db_column='Type', blank=True) # Field name made lowercase.
    indate = models.TextField(db_column='InDate', blank=True) # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    distributor = models.TextField(db_column='Distributor', blank=True) # Field name made lowercase.
    condition = models.TextField(db_column='Condition', blank=True) # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True) # Field name made lowercase.
    cost = models.FloatField(null=True, db_column='Cost', blank=True) # Field name made lowercase.
    serial = models.TextField(db_column='Serial', blank=True) # Field name made lowercase.
    barcode = models.TextField(db_column='BarCode', blank=True) # Field name made lowercase.
    internalbarcode = models.TextField(db_column='InternalBarCode', blank=True) # Field name made lowercase.
    departmentid = models.IntegerField(null=True, db_column='DepartmentID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inventory'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.itemid, self.type, self.indate, self.name, self.distributor, self.condition, self.location, self.cost, self.serial)

class Accesscontroldevice(models.Model):
    deviceid = models.IntegerField(primary_key=True, db_column='DeviceID') # Field name made lowercase.
    devicename = models.TextField(db_column='DeviceName', blank=True) # Field name made lowercase.
    ip = models.TextField(db_column='IP', blank=True) # Field name made lowercase.
    port = models.IntegerField(null=True, db_column='Port', blank=True) # Field name made lowercase.
    isssr = models.IntegerField(null=True, db_column='IsSSR', blank=True) # Field name made lowercase.
    isusb = models.IntegerField(null=True, db_column='IsUSB', blank=True) # Field name made lowercase.
    readscards = models.IntegerField(null=True, db_column='ReadsCards', blank=True) # Field name made lowercase.
    readsfingerprints = models.IntegerField(null=True, db_column='ReadsFingerprints', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AccessControlDevice'

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.deviceid, self.devicename, self.ip, self.port)

class Taskstatus(models.Model):
    taskstatusid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='TaskStatusID') # Field name made lowercase.
    taskstatusname = models.TextField(db_column='TaskStatusName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TaskStatus'

    def __unicode__(self):
        return u'%s, %s' % (self.taskstatusid, self.taskstatusname)

class Taskentitytype(models.Model):
    entitytypeid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='EntityTypeID') # Field name made lowercase.
    entity = models.TextField(db_column='Entity', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TaskEntityType'

    def __unicode__(self):
        return u'%s, %s' % (self.entitytypeid, self.entity)

class Task(models.Model):
    taskid = models.IntegerField(primary_key=True, blank=False, null=False, db_column='TaskID') # Field name made lowercase.
    taskname = models.TextField(db_column='TaskName', blank=True) # Field name made lowercase.
    entityid = models.IntegerField(null=True, db_column='EntityID', blank=True) # Field name made lowercase.
    parentid = models.IntegerField(null=True, db_column='ParentID', blank=True) # Field name made lowercase.
    offset = models.TextField(db_column='Offset', blank=True) # Field name made lowercase.
    offsettypeid = models.IntegerField(null=True, db_column='OffsetTypeID', blank=True) # Field name made lowercase.
    duration = models.TextField(db_column='Duration', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    position = models.IntegerField(null=True, blank=True)
    hidden = models.IntegerField(null=True, blank=True)
    bakedstartdate = models.TextField(db_column='BakedStartDate', blank=True) # Field name made lowercase.
    bakedenddate = models.TextField(db_column='BakedEndDate', blank=True) # Field name made lowercase.
    originalstartdate = models.TextField(db_column='OriginalStartDate', blank=True) # Field name made lowercase.
    originalenddate = models.TextField(db_column='OriginalEndDate', blank=True) # Field name made lowercase.
    idledays = models.IntegerField(null=True, db_column='IdleDays', blank=True) # Field name made lowercase.
    isclone = models.IntegerField(null=True, db_column='IsClone', blank=True) # Field name made lowercase.
    isactive = models.IntegerField(null=True, db_column='IsActive', blank=True) # Field name made lowercase.
    entitytypeid = models.IntegerField(null=True, db_column='EntityTypeID', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    taskstatusid = models.IntegerField(null=True, db_column='TaskStatusID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Task'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.taskid, self.taskname, self.offset, self.duration, self.originalstartdate, self.originalenddate)

"Houston we have got to do SOMETHING WITH THESE problems!!!!"
### SOLVED ###
class Taskartist(models.Model):
    id = db.MultiFieldPK('taskid', 'userid')
    taskid = models.IntegerField(db_column='TaskID') # Field name made lowercase.
    userid = models.TextField(db_column='UserID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TaskArtist'

    def __unicode__(self):
        return u'%s' % (self.id)

class Taskdependencies(models.Model):
    dependencyid = models.IntegerField(primary_key=True, db_column='DependencyID') # Field name made lowercase.
    taskid = models.IntegerField(null=True, db_column='TaskID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TaskDependencies'

    def __unicode__(self):
        return u'%s' % (self.dependencyid)

class Workdaycalendar(models.Model):
    workdaycalendarid = models.IntegerField(primary_key=True, db_column='WorkdayCalendarID') # Field name made lowercase.
    type = models.IntegerField(db_column='Type') # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'WorkdayCalendar'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.workdaycalendarid, self.type, self.date)

class SqliteStat1(models.Model):
    tbl = models.TextField(primary_key=True)
    idx = models.TextField(blank=True)
    stat = models.TextField(blank=True)
    class Meta:
        db_table = u'sqlite_stat1'

    def __unicode__(self):
        return u'%s, %s, %s' % (self.tbl, self.idx, self.stat)

