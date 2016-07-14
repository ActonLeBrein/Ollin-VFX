from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class UserTypes(models.Model):
	TypeName = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s' % (self.TypeName)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	UserType_ID = models.ForeignKey(UserTypes)
	IsGroup = models.IntegerField()

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.user.username, self.user.first_name, self.user.last_name, self.user.email, self.UserType_ID)

class AccessControlFingerprint(models.Model):
	EnrollID = models.IntegerField()
	Finger = models.IntegerField()
	Fingerprint = models.CharField(max_length=1000)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.EnrollID, self.Finger, self.Fingerprint)

class Status(models.Model):
	StatusID = models.IntegerField(primary_key=True, blank=False, null=False)
	StatusName = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s' % (self.StatusName)

class AccessControlLog(models.Model):
	EventID = models.CharField(max_length=100, blank=False, null=False)
	Date = models.DateTimeField()
	EnrollID = models.IntegerField()
	Period = models.IntegerField()
	Method = models.IntegerField()
	OverrideAction = models.IntegerField()
	Status_ID = models.ForeignKey(Status)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.Date = datetime.date.today()
					return super(AccessControlLog, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s' % (self.EventID, self.Date, self.EnrollID, self.Period, self.Method, self.Status)

class LoginAttempt(models.Model):
	Attempts = models.IntegerField()
	LastAttempt = models.DateTimeField()
	User_ID = models.ForeignKey(UserProfile)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.LastAttempt = datetime.date.today()
					self.LastAttempt = datetime.date.today()
					return super(LoginAttempt, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s' % (self.Attempts, self.LastAttempt)

class UserGroup(models.Model):
	GroupID = models.CharField(primary_key=True, blank=False, null=False, max_length=100)
	User_ID = models.ManyToManyField(UserProfile)

	def get_members(self):
		return "\n".join([p.user.username+', ' for p in self.User_ID.all()])

	def __unicode__(self):
		return u'%s' % (self.GroupID)

class EvaluationRound(models.Model):
	EvaluationRoundID = models.IntegerField(primary_key=True, blank=False, null=False)
	Date = models.DateField()

	def __unicode__(self):
		return u'%s, %s' % (self.EvaluationRoundID, self.Date)

class Evaluation(models.Model):
	EvaluationID = models.IntegerField(primary_key=True, blank=False, null=False)
	Technical = models.IntegerField()
	TechnicalNotes = models.TextField()
	Professional = models.IntegerField()
	ProfessionalNotes = models.TextField()
	Teamwork = models.IntegerField()
	TeamworkNotes = models.TextField()
	ForceEval = models.IntegerField()
	EvalApplied = models.IntegerField()
	EvaluationDate = models.DateTimeField()
	CurrentBoss = models.CharField(max_length=100)
	Evaluated = models.ForeignKey(UserProfile, related_name='Evaluated')
	Evaluator = models.ForeignKey(UserProfile, related_name='Evaluator')
	EvaluationRound_ID = models.ForeignKey(EvaluationRound)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.Evaluated, self.Evaluator, self.RoundID, self.CurrentBoss, self.EvaluationDate)

class EntityType(models.Model):
	EntityTypeID = models.IntegerField(primary_key=True, blank=False, null=False)
	EntityName = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s' % (self.EntityName)

class Comment(models.Model):
	Date = models.DateTimeField()
	Comments = models.TextField()
	EntityID = models.IntegerField()
	EntityType_ID = models.ForeignKey(EntityType)
	User_ID = models.ForeignKey(UserProfile)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.Date = datetime.date.today()
					return super(Comment, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s' % (self.Entity_ID, self.Date, self.Comments)

class Alarm(models.Model):
	AlarmID = models.IntegerField(primary_key=True, blank=False, null=False)
	Due = models.DateTimeField()
	What = models.CharField(max_length=100)
	Action_ID = models.IntegerField()
	Mode = models.IntegerField()
	LastFired = models.DateTimeField(blank=True, null=True)
	EntityID = models.IntegerField()
	EntityType_ID = models.ForeignKey(EntityType)
	Status_ID = models.ForeignKey(Status)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.LastFired = datetime.date.today()
					self.LastFired = datetime.datetime.today()
					return super(Alarm, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s, %s' % (self.AlarmID, self.Due, self.What, self.Status_ID, self.Action_ID, self.Mode, self.LastFired)

class AlarmReminder(models.Model):
	AlarmReminderID = models.IntegerField(primary_key=True, blank=False, null=False)
	DaysBefore = models.IntegerField()
	Fired = models.IntegerField()
	Alarm_ID = models.ForeignKey(Alarm)

	def __unicode__(self):
		return u'%s, %s' % (self.DaysBefore, self.Fired)

class AlarmActionParameter(models.Model):
	Parameter = models.CharField(max_length=100)
	Alarm_ID = models.ForeignKey(Alarm)

	def __unicode__(self):
		return u'%s' % (self.Parameter)

class Commands(models.Model):
	CommandName = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s' % (self.CommandName)

class PriviledgesMatrix(models.Model):
	Commands_ID = models.ForeignKey(Commands, primary_key=True, max_length=100, blank=False, null=False)
	P1 = models.IntegerField()
	P2 = models.IntegerField()
	P3 = models.IntegerField()
	P4 = models.IntegerField()
	P5 = models.IntegerField()
	P6 = models.IntegerField()
	P7 = models.IntegerField()
	P8 = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.Command)

class CommandRelations(models.Model):
	Command = models.ForeignKey(Commands, related_name='Command')
	RelatedTo = models.ForeignKey(Commands, related_name='RelatedTo')

	class Meta:
		unique_together = ('Command', 'RelatedTo')

	def __unicode__(self):
		return u'%s, %s' % (self.Command, self.RelatedTo)

class ExtendedPermissions(models.Model):
	Action = models.IntegerField()
	Commands_ID = models.ForeignKey(Commands)
	User_ID = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return u'%s' % (self.Action)

class Notification(models.Model):
	NotificationID = models.AutoField(primary_key=True, blank=False, null=False, editable=False)
	AlreadyRead = models.IntegerField()
	From = models.CharField(max_length=100)
	AddressedTo = models.CharField(max_length=100)
	TypeID = models.IntegerField()
	Subject = models.CharField(max_length=500)
	Body = models.TextField()
	BodyHTML = models.TextField()
	DateTime = models.DateTimeField()
	Status_ID = models.ForeignKey(Status)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.DateTime = datetime.datetime.today()
					return super(Notification, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s, %s' % (self.NotificationID, self.AlreadyRead, self.Status_ID, self.TypeID, self.From, self.AddressedTo, self.DateTime)

class NotificationMetadata(models.Model):
	ID = models.AutoField(primary_key=True, blank=False, null=False, editable=False)
	MetadataName = models.CharField(max_length=100)
	MetadataValue = models.CharField(max_length=100, blank=True, null=True)
	Notification_ID = models.ForeignKey(Notification)

	def __unicode__(self):
		return u'%s, %s' % (self.MetadataName, self.MetadataValue)

class Project(models.Model):
	ProjectID = models.IntegerField(primary_key=True, blank=False, null=False)
	ProjectName = models.CharField(max_length=100)
	ProjectNickname = models.CharField(max_length=100, blank=True, null=True)
	Director = models.CharField(max_length=100, blank=True, null=True)
	Producer = models.CharField(max_length=100, blank=True, null=True)
	Studio = models.CharField(max_length=100, blank=True, null=True)
	ConsumableAllowance = models.CharField(max_length=100)
	Contingency = models.FloatField()
	Thumbnail = models.TextField(blank=True, null=True)
	ImageAssetID = models.IntegerField(blank=True, null=True)
	OldStructure = models.IntegerField()
	Active = models.IntegerField()
	CreationDate = models.DateTimeField(blank=True, null=True)
	RestrictShotsToAssignedUsers = models.IntegerField()
	StartDate = models.DateField(blank=True, null=True)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.CreationDate = datetime.date.today()
					self.StartDate = datetime.datetime.today()
					return super(Project, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s' % (self.ProjectID, self.ProjectName, self.ProjectNickname, self.Director, self.Producer, self.Studio)

class Milestone(models.Model):
	MilestoneID = models.IntegerField(primary_key=True, blank=False, null=False)
	Name = models.CharField(max_length=100)
	Date = models.DateTimeField(blank=True, null=True)
	Project_ID = models.ForeignKey(Project)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.MilestoneID, self.Name, self.Date)

class IncomingFile(models.Model):
	IncomingFileID = models.IntegerField(primary_key=True, blank=False, null=False)
	Date = models.DateField()
	Sender = models.CharField(max_length=100)
	AddressedTo = models.CharField(max_length=200)
	SourcePath = models.CharField(max_length=200)
	FinalPath = models.CharField(max_length=200)
	Description = models.TextField()
	Tags = models.TextField()
	Area = models.CharField(max_length=100)
	Media = models.CharField(max_length=100)
	Project_ID = models.ForeignKey(Project)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.Date = datetime.date.today()
					return super(IncomingFile, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s' % (self.IncomingFileID, self.Date, self.Sender, self.AddressedTo, self.Area, self.Media)

class ProjectUser(models.Model):
	Project_ID = models.ForeignKey(Project)
	User_ID = models.ForeignKey(UserProfile)

class Playlist(models.Model):
	PlaylistID = models.IntegerField(primary_key=True, blank=False, null=False)
	PlaylistName = models.CharField(max_length=100)
	PlaylistXML = models.TextField(blank=True, null=True)
	AutoUpdate = models.CharField(max_length=100, blank=True, null=True)
	Project_ID = models.ForeignKey(Project)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.PlaylistName, self.PlaylistXML, self.AutoUpdate)

class RateSet(models.Model):
	RateSetID = models.IntegerField(primary_key=True, blank=False, null=False)
	RateSetNumber = models.IntegerField()
	RateSetName = models.CharField(max_length=100)
	RateSetNotes = models.TextField(blank=True, null=True)
	RateSetCreationDate = models.DateTimeField()
	RateSetLastModification = models.DateTimeField()
	RateSetConsumableAllowance = models.FloatField()
	RateSetContingency = models.FloatField()
	RateSetExtra = models.FloatField()
	RateSetExtraIT = models.IntegerField(blank=True, null=True)
	Project_ID = models.ForeignKey(Project)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.RateSetCreationDate = datetime.date.today()
					self.RateSetLastModification = datetime.datetime.today()
					return super(RateSet, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.RateSetNumber, self.RateSetName, self.RateSetCreationDate, self.RateSetLastModification)

class HardDiskStatus(models.Model):
	HardDiskStatusID = models.IntegerField(primary_key=True, blank=False, null=False)
	HardDiskStatusName = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s, %s' % (self.HardDiskStatusID, self.HardDiskStatusName)

class HardDiskRegister(models.Model):
	HardDiskRegisterID = models.IntegerField(primary_key=True, blank=False, null=False)
	SerialNumber = models.CharField(max_length=100, blank=True, null=True)
	HardDiskNumber = models.IntegerField()
	HardDiskName = models.CharField(max_length=100, blank=True, null=True)
	FromAddress = models.CharField(max_length=100, blank=True, null=True)
	ContentOnArrival = models.CharField(max_length=100, blank=True, null=True)
	ArrivalDate = models.DateField(blank=True, null=True)
	ContentOnExit = models.CharField(max_length=100, blank=True, null=True)
	ExitDate = models.DateField(blank=True, null=True)
	Notes = models.TextField(blank=True, null=True)
	HardDiskStatus_ID = models.ForeignKey(HardDiskStatus)
	Project_ID = models.ForeignKey(Project)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.SerialNumber, self.HardDiskNumber, self.HardDiskName, self.FromAddress)

class UploadControl(models.Model):
	UploadControlID = models.IntegerField(primary_key=True, blank=False, null=False)
	Filename = models.CharField(max_length=200, blank=True, null=True)
	Path = models.TextField()
	Date = models.DateTimeField()
	Password = models.CharField(max_length=100)
	Project_ID = models.ForeignKey(Project)
	User_ID = models.ForeignKey(UserProfile)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.Date = datetime.datetime.today()
					return super(UploadControl, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.UploadControlID, self.Filename, self.Path, self.Date)

class StorageUse(models.Model):
	ProjectNickname = models.CharField(max_length=100)
	VFXID = models.CharField(max_length=100)
	VersionNumber = models.CharField(max_length=100)
	Size = models.BigIntegerField()
	Project_ID = models.ForeignKey(Project)
	User_ID = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.ProjectNickname, self.VFXID, self.VersionNumber, self.Size)

class ServiceType(models.Model):
	ServiceTypeName = models.CharField(max_length=100)
	
	def __unicode__(self):
		return u'%s' % (self.ServiceTypeName)

class Service(models.Model):
	ServiceID = models.IntegerField(primary_key=True, blank=False, null=False)
	ServiceName = models.CharField(max_length=100)
	CostPerDay = models.FloatField(blank=True, null=True)
	ServiceType_ID = models.ForeignKey(ServiceType)
	
	def __unicode__(self):
		return u'%s, %s, %s' % (self.ServiceID, self.ServiceName, self.CostPerDay)

class ServiceHistogramColor(models.Model):
	ServiceHistogramColorID = models.IntegerField(primary_key=True, blank=False, null=False)
	R = models.IntegerField()
	G = models.IntegerField()
	B = models.IntegerField()
	Service_ID = models.ForeignKey(Service)
	
	def __unicode__(self):
		return u'%s, %s, %s' % (self.R, self.G, self.B)

class ProjectService(models.Model):
	ProjectServiceID = models.IntegerField(primary_key=True, blank=False, null=False)
	Rate = models.FloatField(blank=True, null=True)
	RateSetNumber = models.IntegerField()
	Project_ID = models.ForeignKey(Project)
	Service_ID = models.ForeignKey(Service)
	
	def __unicode__(self):
		return u'%s, %s' % (self.Rate, self.RateSetNumber)

class ProjectTaskService(models.Model):
	ProjectTaskServiceID = models.IntegerField(primary_key=True, blank=False, null=False)
	Slots = models.IntegerField()
	Project_ID = models.ForeignKey(Project)
	Service_ID = models.ForeignKey(Service)

	def __unicode__(self):
		return u'%s, %s' % (self.ProjectTaskServiceID, self.Slots)

class AssetType(models.Model):
	AssetTypeID = models.IntegerField(primary_key=True, blank=False, null=False)
	AssetTypeName = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s, %s' % (self.AssetTypeID, self.AssetTypeName)

class SequencialIDGenerator(models.Model):
	SIG_id = models.IntegerField(primary_key=True, blank=False, null=False, editable=False)
	
	def __unicode__(self):
		return u'%s' % (self.SIG_id)

class Sequence(models.Model):
	SequenceName = models.CharField(max_length=100, blank=True, null=True)
	SequenceNickname = models.CharField(max_length=100, blank=True, null=True)
	Project_ID = models.ForeignKey(Project)
	SequencialIDGenerator_ID = models.OneToOneField(SequencialIDGenerator, primary_key=True, blank=False, null=False)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.SequencialIDGenerator_ID, self.SequenceName, self.SequenceNickname)

class Shot(models.Model):
	ShotID = models.IntegerField(primary_key=True, blank=False, null=False)
	VFXID = models.CharField(max_length=100)
	ExternalID = models.CharField(max_length=100, blank=True, null=True)
	ShotName = models.CharField(max_length=100)
	Location = models.CharField(max_length=100, blank=True, null=True)
	CameraMotion = models.CharField(max_length=100, blank=True, null=True)
	SceneNumber = models.CharField(max_length=100, blank=True, null=True)
	PageNumber = models.CharField(max_length=100, blank=True, null=True)
	Frames = models.IntegerField()
	DirectorNotes = models.TextField(blank=True, null=True)
	ShotDescription = models.TextField(blank=True, null=True)
	Thumbnail = models.TextField(blank=True, null=True)
	ImageAssetID = models.IntegerField(blank=True, null=True)
	AddConsumablesAllowance = models.CharField(max_length=100)
	WorkedeBy = models.CharField(max_length=100, blank=True, null=True)
	Type = models.IntegerField()
	Lens = models.CharField(max_length=100, blank=True, null=True)
	PrimaryBidNumber = models.IntegerField()
	VFXTasks = models.TextField(blank=True, null=True)
	IsReference = models.IntegerField(blank=True, null=True)
	SortIndex = models.IntegerField(blank=True, null=True)
	Take = models. IntegerField(blank=True, null=True)
	Active = models.IntegerField()
	Project_ID = models.ForeignKey(Project)
	Sequence_ID = models.ForeignKey(Sequence)
	Status_ID = models.ForeignKey(Status)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.ShotID, self.VFXID, self.ShotName, self.SceneNumber)

class Bid(models.Model):
	BidID = models.IntegerField(primary_key=True, blank=False, null=False)
	BidName = models.CharField(max_length=100)
	BidDate = models.DateTimeField()
	BidNotes = models.TextField(blank=True, null=True)
	BidLastModification = models.DateTimeField()
	AddConsumablesAllowance = models.IntegerField(blank=True, null=True)
	BidNumber = models.IntegerField()
	RateSetNumber = models.IntegerField()
	HideInCalendar = models.IntegerField()
	Project_ID = models.ForeignKey(Project)
	Shot_ID = models.ForeignKey(Shot)

	'''def save(self, *args, **kwargs):
					if not self.BidNumber:
						self.BidDate = datetime.date.today()
					self.BidLastModification = datetime.datetime.today()
					return super(Bid, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.BidID, self.BidNumber, self.BidName, self.BidDate, self.BidLastModification)

class Assets(models.Model):
	AssetID = models.IntegerField(primary_key=True, blank=False, null=False)
	AssetName = models.CharField(max_length=100)
	Notes = models.TextField(blank=True, null=True)
	Path = models.TextField(blank=True, null=True)
	Size = models.BigIntegerField()
	UploadDate = models.DateTimeField()
	Public = models.IntegerField(blank=True, null=True)
	Tags = models.TextField(blank=True, null=True)
	Parent = models.IntegerField()
	LastModified = models.DateTimeField()
	OnCloud = models.IntegerField(blank=True, null=True)
	CloudStatus = models.IntegerField(blank=True, null=True)
	AssetType_ID = models.ForeignKey(AssetType)
	Project_ID = models.ForeignKey(Project)
	Shot_ID = models.ForeignKey(Shot)
	User_ID_Uploader = models.ForeignKey(UserProfile)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.UploadDate = datetime.date.today()
					self.LastModified = datetime.datetime.today()
					return super(Assets, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s, %s' % (self.AssetID, self.AssetName, self.Path, self.Size, self.Public, self.UploadDate, self.LastModified)

class Transfer(models.Model):
	TransferID = models.IntegerField(primary_key=True, blank=False, null=False)
	Date = models.DateTimeField()
	IP = models.CharField(max_length=100, blank=True, null=True)
	Type = models.IntegerField()
	Assets_ID = models.OneToOneField(Assets)
	User_ID = models.ForeignKey(UserProfile)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.Date = datetime.date.today()
					return super(Transfer, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.TransferID, self.Type, self.IP, self.Date)

class AssetPriviledges(models.Model):
	Assets_ID = models.ForeignKey(Assets)
	UserTypes_ID = models.ForeignKey(UserTypes)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.id, self.Assets_ID, self.UserTypes_ID)

class DeletedAssets(models.Model):
	DeletedAssetID = models.IntegerField(primary_key=True, blank=False, null=False)
	AssetName = models.CharField(max_length=100)
	Notes = models.TextField(blank=True, null=True)
	Path = models.TextField(blank=True, null=True)
	AssetType = models.IntegerField()
	Size = models.BigIntegerField()
	UploadDate = models.DateField()
	Public = models.IntegerField()
	Tags = models.TextField(blank=True, null=True)
	Assets_ID = models.ForeignKey(Assets)
	Project_ID = models.ForeignKey(Project)
	User_ID_Uploader = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s' % (self.AssetName, self.Path, self.Size, self.Public, self.UploadDate, self.astModified)

class DownloadControl(models.Model):
	DownloadControlID = models.IntegerField(primary_key=True, blank=False, null=False)
	Path = models.TextField()
	Date = models.DateTimeField()
	Password = models.CharField(max_length=100)
	Assets_ID = models.ForeignKey(Assets)
	User_ID = models.ForeignKey(UserProfile)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.Date = datetime.date.today()
					return super(DownloadControl, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s' % (self.DownloadControlID, self.Path, self.Date)

class ShotsService(models.Model):
	ShotServiceID = models.IntegerField(primary_key=True, blank=False, null=False)
	Days = models.FloatField()
	BidNumber = models.IntegerField()
	Project_ID = models.ForeignKey(Project)
	Service_ID = models.ForeignKey(Service)
	Shot_ID = models.ForeignKey(Shot)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.ShotServiceID, self.Days, self.BidNumber)

class ShotsAssets(models.Model):
	ShotsAssetsID = models.IntegerField(primary_key=True, blank=False, null=False)
	Assets_ID = models.ForeignKey(Assets)
	Project_ID = models.ForeignKey(Project)
	Shot_ID = models.ForeignKey(Shot)

class ShotStatusLog(models.Model):
	FromStatus = models.CharField(max_length=100)
	ToStatus = models.CharField(max_length=100)
	Date = models.DateTimeField()
	Project_ID = models.ForeignKey(Project)
	Shot_ID = models.ForeignKey(Shot)
	User_ID = models.ForeignKey(UserProfile)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.Date = datetime.date.today()
					return super(ShotStatusLog, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.id, self.FromStatus, self.ToStatus, self.Date)

class ShotDelivery(models.Model):
	VFXID = models.CharField(max_length=100)
	ShotName = models.CharField(max_length=100)
	ReviewDate = models.DateField()
	InternalComments = models.TextField()
	ClientComments = models.TextField(blank=True, null=True)
	InternalVersion = models.CharField(max_length=100)
	ClientVersion = models.CharField(max_length=100)
	Work = models.CharField(max_length=100)
	Stereo = models.CharField(max_length=100)
	Project_ID = models.ForeignKey(Project)
	Shot_ID = models.ForeignKey(Shot)
	Status_ID = models.ForeignKey(Status)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.id, self.VFXID, self.ShotName, self.Status, self.ReviewDate)

class ShotGroup(models.Model):
	ShotGroupID = models.IntegerField(primary_key=True, blank=False, null=False)
	ShotGroupName = models.CharField(max_length=100)
	ShotGroupNotes = models.TextField()
	Project_ID = models.ForeignKey(Project)

	def __unicode__(self):
		return u'%s, %s' % (self.ShotGroupID, self.ShotGroupName)

class ShotGroupShotID(models.Model):
	Shot_ID = models.ForeignKey(Shot)
	ShotGroup_ID = models.ForeignKey(ShotGroup)

	def __unicode__(self):
		return u'%s' % (self.id)

class ShotGroupTentpole(models.Model):
	Shot_ID = models.ForeignKey(Shot)
	ShotGroup_ID = models.ForeignKey(ShotGroup)

	def __unicode__(self):
		return u'%s' % (self.id)

class ShotUser(models.Model):
	Shot_ID = models.ForeignKey(Shot)
	User_ID = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return u'%s' % (self.id)

class SelectionSet(models.Model):
	SelectionSetID = models.IntegerField(primary_key=True, blank=False, null=False)
	SelectionSetName = models.CharField(max_length=100)
	Project_ID = models.ForeignKey(Project)

	def __unicode__(self):
		return u'%s, %s' % (self.SelectionSetID, self.SelectionSetName)

class ShotSelectionSet(models.Model):
	ShotSelectionSetID = models.IntegerField(primary_key=True, blank=False, null=False)
	SelectionSet_ID = models.ForeignKey(SelectionSet)
	Shot_ID = models.ForeignKey(Shot)

	def __unicode__(self):
		return u'%s' % (self.ShotSelectionSetID)

class CustomShotField(models.Model):
	CustomShotFieldID = models.IntegerField(primary_key=True, blank=False, null=False)
	FieldName = models.CharField(max_length=100, blank=False, null= False)
	DefaultValue = models.CharField(max_length=100, blank=True, null=True)
	Project_ID = models.ForeignKey(Project)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.CustomShotFieldID, self.FieldName, self.DefaultValue)

class ShotCustomShotField(models.Model):
	ShotCustomShotFieldID = models.IntegerField(primary_key=True, blank=False, null=False)
	Value = models.CharField(max_length=100, blank=True, null=True)
	CustomShotField_ID = models.ForeignKey(CustomShotField)
	Shot_ID = models.ForeignKey(Shot)

	def __unicode__(self):
		return u'%s, %s' % (self.ShotCustomShotFieldID, self.Value)

class Version(models.Model):
	VersionID = models.IntegerField(primary_key=True, blank=False, null=False)
	Major = models.IntegerField()
	Minor = models.IntegerField()
	External = models.IntegerField()
	Notes = models.TextField(blank=True, null=True)
	Tags = models.TextField(blank=True, null=True)
	CreationDate = models.DateField()
	View = models.CharField(max_length=100, blank=True, null=True)
	Task = models.CharField(max_length=100, blank=True, null=True)
	PublishedBy = models.CharField(max_length=100, blank=True, null=True)
	Shot_ID = models.ForeignKey(Shot)

	'''def save(self, *args, **kwargs):
					if not self.id:
						self.CreationDate = datetime.date.today()
					return super(Version, self).save(*args, **kwargs)'''

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.VersionID, self.Major, self.Minor, self.External, self.CreationDate)

class VersionAsset(models.Model):
	VersionAssetID = models.IntegerField(primary_key=True, blank=False, null=False)
	Assets_ID = models.ForeignKey(Assets)
	Version_ID = models.ForeignKey(Version)

	def __unicode__(self):
		return u'%s' % (self.VersionAssetID)

class Script(models.Model):
	ScriptName = models.CharField(max_length=100, blank=True, null=True)
	MajorVersion = models.CharField(max_length=100)
	MinorVersion = models.CharField(max_length=100)
	Task = models.CharField(max_length=100)
	STask = models.CharField(max_length=100)
	Project_ID = models.ForeignKey(Project)
	Shot_ID = models.ForeignKey(Shot)
	User_ID = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.id, self.ScriptName, self.MajorVersion, self.MinorVersion, self.Task)

class PublishJob(models.Model):
	CreationDate = models.DateField()
	CreatedBy = models.CharField(max_length=100)
	PublishDate = models.DateField()
	PublishType = models.CharField(max_length=100)
	Script_ID = models.ForeignKey(Script)
	Status_ID = models.OneToOneField(Status)

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.CreationDate = datetime.date.today()
		return super(PublishJob, self).save(*args, **kwargs)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.CreatedBy, self.PublishType, self.CreationDate, self.PublishDate)

class Lineup(models.Model):
	CreationDate = models.DateField()
	CreatedBy = models.CharField(max_length=100)
	Name = models.CharField(max_length=100)
	Camera = models.CharField(max_length=100)
	TStop = models.CharField(max_length=100)
	FrameSize = models.CharField(max_length=100)
	CutLengthFrames = models.CharField(max_length=100)
	InFrame = models.CharField(max_length=100)
	InTC = models.CharField(max_length=100)
	OutFrame = models.CharField(max_length=100)
	OutTC = models.CharField(max_length=100)
	FramesWithHandles = models.CharField(max_length=100)
	InFramesWithHandles = models.CharField(max_length=100)
	InTCWithHandles = models.CharField(max_length=100)
	OutFrameWithHandles = models.CharField(max_length=100)
	OutTCWithHandles = models.CharField(max_length=100)
	RawMediaStart = models.CharField(max_length=100)
	RawMediaEnd = models.CharField(max_length=100)
	RawMediaDuration = models.CharField(max_length=100)
	RawMediaStartFrame = models.CharField(max_length=100)
	RawMediaEndFrame = models.CharField(max_length=100)
	RawMediaDurationFrames = models.CharField(max_length=100)
	EditorialName = models.CharField(max_length=100)
	EDLPull = models.CharField(max_length=100)
	ElementDescription = models.TextField()
	Format = models.CharField(max_length=100)
	ISO = models.CharField(max_length=100)
	Kelvin = models.CharField(max_length=100)
	Lens = models.CharField(max_length=100)
	Reel = models.CharField(max_length=100)
	ReelID = models.CharField(max_length=100)
	Scene = models.CharField(max_length=100)
	SceneDescription = models.TextField()
	Setup = models.CharField(max_length=100)
	ShootDate = models.DateField()
	ShootDay = models.CharField(max_length=100)
	ShotDescription = models.TextField()
	ShuttleAngle = models.CharField(max_length=100)
	ShutterSpeed = models.CharField(max_length=100)
	SlugLine = models.SlugField(max_length=100, unique=True)
	Speed = models.CharField(max_length=100)
	StabilizeCurvesSent = models.IntegerField()
	Take = models.CharField(max_length=100)
	Tint = models.CharField(max_length=100)
	Project_ID = models.ForeignKey(Project)
	Shot_ID = models.ForeignKey(Shot)

	def save(self, *args, **kwargs):
		if not self.id:
			self.SlugLine = slugify(self.title)
		super(Lineup, self).save(*args, **kwargs)

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.CreationDate = datetime.date.today()
		return super(Lineup, self).save(*args, **kwargs)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.CreatedBy, self.Name, self.Camera, self.CreationDate)

class SalaryGeneralData(models.Model):
	MaxSalaryInc = models.FloatField(primary_key=True, blank=False, null=False, editable=True)
	CPIMX = models.FloatField()
	CPIUSA = models.FloatField()
	CPIAdjustStrategy = models.IntegerField()

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.MaxSalaryInc, self.CPIMX, self.CPIUSA, self.CPIAdjustStrategy)

class SalaryStructure(models.Model):
	SalaryName = models.CharField(max_length=100)
	SalaryDefinition = models.CharField(max_length=100)
	SalaryMidRange = models.FloatField()
	LevelIncrease = models.FloatField()
	CurrentType = models.IntegerField()
	Salary1 = models.FloatField()
	Salary2 = models.FloatField()
	Salary3 = models.FloatField()
	Salary4 = models.FloatField()
	Salary5 = models.FloatField()
	Salary6 = models.FloatField()
	Salary7 = models.FloatField()
	Salary8 = models.FloatField()
	Salary9 = models.FloatField()
	SalaryGeneralData_ID = models.ForeignKey(SalaryGeneralData)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.SalaryName, self.SalaryDefinition, self.SalaryMidRange, self.LevelIncrease, self.CurrentType)

class Department(models.Model):
	DepartmentName = models.CharField(max_length=100)
	DepartmentHeadID = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.DepartmentName)

class Associate(models.Model):
	FirstName = models.CharField(max_length=100)
	LastName = models.CharField(max_length=100)
	Active = models.IntegerField()
	CurrentSalary = models.FloatField()
	LastIncrease = models.DateField()
	LastCOLncrease = models.DateField()
	IncreaseApply = models.IntegerField()
	BossID = models.IntegerField()
	FirstHired = models.DateField()
	Title = models.CharField(max_length=100)
	JobDescription = models.TextField()
	Address = models.CharField(max_length=100)
	Phone = models.CharField(max_length=100)
	AllowedDaysPerYear = models.FloatField()
	Department_ID = models.ForeignKey(Department)
	SalaryStructure_ID = models.ForeignKey(SalaryStructure)
	User_ID = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s, %s, %s' % (self.FirstName, self.LastName, self.Title, self.Active, self.CurrentSalary, self.LastIncrease, self.LastCOLncrease, self.FirstHired)

class COL(models.Model):
	Name = models.CharField(max_length=100)
	Year = models.CharField(max_length=100)
	COL = models.FloatField()

	def __unicode__(self):
		return u'%s, %s, %s' % (self.Name, self.Year, self.COL)

class MeritPercentages(models.Model):
	SalaryQuartile = models.IntegerField(primary_key=True, blank=False, null=False, editable=True)
	Rate0 = models.FloatField()
	Rate1 = models.FloatField()
	Rate2 = models.FloatField()
	Rate3 = models.FloatField()
	Rate4 = models.FloatField()

	def __unicode__(self):
		return u'%s' % (self.SalaryQuartile)

class AssociateSalaryHistory(models.Model):
	SalaryModDate = models.DateField()
	OldSalary = models.FloatField()
	NewSalary = models.FloatField()
	PerformanceRating = models.CharField(max_length=100)
	CostOfLiving = models.FloatField()
	MeritIncrease = models.FloatField()
	MeritAmount = models.FloatField()
	PromotionBonus = models.FloatField()
	PromotionBonusAmount = models.FloatField()
	SalaryEndDate = models.DateField()
	Notes = models.TextField()
	UpdatedBy = models.CharField(max_length=100)
	Associate_ID = models.ForeignKey(Associate)
	COL_ID = models.OneToOneField(COL)
	SalaryQuartile = models.OneToOneField(MeritPercentages)
	SalaryStructure_ID = models.ForeignKey(SalaryStructure)

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.SalaryModDate = datetime.date.today()
		self.SalaryModDate = datetime.datetime.today()
		return super(AssociateSalaryHistory, self).save(*args, **kwargs)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.SalaryModDate, self.OldSalary, self.NewSalary, self.UpdatedBy)

class VacationPeriod(models.Model):
	StartDate = models.DateField()
	EndDate = models.DateField()
	AllowedDays = models.FloatField()
	Number = models.IntegerField()
	Associate_ID = models.ForeignKey(Associate)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.StartDate, self.EndDate, self.AllowedDays, self.Number)

class VacationEvent(models.Model):
	PeriodID = models.IntegerField()
	StartDate = models.DateField()
	EndDate = models.DateField()
	Days = models.FloatField()
	DaysBeforeEvent = models.FloatField()
	VacationPeriod_ID = models.ForeignKey(VacationPeriod)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.PeriodID, self.StartDate, self.EndDate, self.Days, self.DaysBeforeEvent)

class AccessControl(models.Model):
	EnrollID = models.IntegerField()
	CardID = models.CharField(max_length=100)
	Priviledge = models.IntegerField()
	Associate_ID = models.ForeignKey(Associate)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.EnrollID, self.CardID, self.Priviledge)

class ContractEvent(models.Model):
	StartDate = models.DateField()
	DurationDays = models.IntegerField()
	AllowedDays = models.FloatField()
	CurrentSalary = models.FloatField()
	JobDescription = models.TextField()
	Title = models.CharField(max_length=100)
	ByProject = models.IntegerField()
	Valid = models.IntegerField()
	Associate_ID = models.ForeignKey(Associate)
	Department_ID = models.ForeignKey(Department)
	SalaryStructure_ID = models.ForeignKey(SalaryStructure)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.StartDate, self.DurationDays, self.AllowedDays, self.CurrentSalary, self.Title)

class Inventory(models.Model):
	Type = models.IntegerField()
	InDate = models.DateField()
	Name = models.CharField(max_length=100)
	Description = models.TextField()
	Distributor = models.CharField(max_length=100)
	Condition = models.CharField(max_length=100)
	Location = models.CharField(max_length=100)
	Cost = models.FloatField()
	Serial = models.CharField(max_length=100)
	BarCode = models.CharField(max_length=100)
	InternalBarCode = models.CharField(max_length=100)
	Department_ID = models.ForeignKey(Department)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s, %s, %s' % (self.Type, self.InDate, self.Name, self.Distributor, self.Condition, self.Location, self.Cost, self.Serial)

class AccessControlDevice(models.Model):
	DeviceName = models.CharField(max_length=100)
	IP = models.CharField(max_length=100)
	Port = models.IntegerField()
	IsSSR = models.IntegerField()
	IsUSB = models.IntegerField()
	ReadsCards = models.IntegerField()
	ReadsFingerprints = models.IntegerField()
	Inventory_ID = models.ForeignKey(Inventory)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.DeviceName, self.IP, self.Port)

class TaskStatus(models.Model):
	TaskStatusName = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s' % (self.TaskStatusName)

class TaskEntityType(models.Model):
	Entity = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s' % (self.Entity)

class Task(models.Model):
	TaskName = models.CharField(max_length=100)
	Parent_ID = models.IntegerField()
	Offset = models.CharField(max_length=100)
	OffsetType_ID = models.IntegerField()
	Duration = models.CharField(max_length=100)
	Notes = models.TextField()
	Position = models.IntegerField()
	Hidden = models.IntegerField()
	BakedStartDate = models.DateField()
	BakedEndDate = models.DateField()
	OriginalStartDate = models.DateField()
	OriginalEndDate = models.DateField()
	IdleDays = models.IntegerField()
	IsClone = models.IntegerField()
	IsActive = models.IntegerField()
	Project_ID = models.ForeignKey(Project)
	TaskEntityType_ID = models.ForeignKey(TaskEntityType)
	TaskStatus_ID = models.ForeignKey(TaskStatus)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s' % (self.TaskName, self.Offset, self.Duration, self.OriginalStartDate, self.OriginalEndDate)

class TaskArtist(models.Model):
	Task_ID = models.ForeignKey(Task)
	User_ID = models.ForeignKey(UserProfile)

class TaskDependencies(models.Model):
	Dependency_ID = models.AutoField(primary_key=True, blank=False, null=False, editable=False)
	Task_ID = models.ForeignKey(Task)