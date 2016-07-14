from django.contrib import admin
from ollinvfx.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class MyUserAdmin(UserAdmin):
	list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login']
	list_filter =  ['id', 'username', 'email', 'first_name', 'last_name']
	inlines = [UserProfileInline, ]

try:
	admin.site.unregister(User)
finally:
	admin.site.register(User, MyUserAdmin)

class UserTypeAdmin(admin.ModelAdmin):
	list_display = ['id', 'TypeName']
	search_fields = ['id', 'TypeName']
	list_filter = ['id', 'TypeName']
admin.site.register(UserTypes, UserTypeAdmin)

class AccessControlFingerprintAdmin(admin.ModelAdmin):
	list_display = ['id', 'EnrollID', 'Finger', 'Fingerprint']
	search_fields = ['id', 'EnrollID', 'Finger', 'Fingerprint']
	list_filter = ['id', 'EnrollID', 'Finger', 'Fingerprint']
admin.site.register(AccessControlFingerprint, AccessControlFingerprintAdmin)

class StatusAdmin(admin.ModelAdmin):
	list_display = ['StatusID', 'StatusName']
	search_fields = ['StatusID', 'StatusName']
	list_filter = ['StatusID', 'StatusName']
admin.site.register(Status, StatusAdmin)

class AccessControlLogAdmin(admin.ModelAdmin):
	list_display = ['id', 'EventID', 'Date', 'EnrollID', 'Period', 'Method', 'OverrideAction', 'Status_ID']
	search_fields = ['id', 'EventID', 'Date', 'EnrollID', 'Period', 'Method', 'OverrideAction', 'Status_ID']
	list_filter = ['id', 'EventID', 'Date', 'EnrollID', 'Period', 'Method', 'OverrideAction']
admin.site.register(AccessControlLog, AccessControlLogAdmin)

class LoginAttemptAdmin(admin.ModelAdmin):
	list_display = ['id', 'Attempts', 'LastAttempt', 'User_ID']
	search_fields = ['id', 'Attempts', 'LastAttempt', 'User_ID']
	list_filter = ['id', 'Attempts', 'LastAttempt', 'User_ID']
admin.site.register(LoginAttempt, LoginAttemptAdmin)

class UserGroupAdmin(admin.ModelAdmin):
	list_display = ['GroupID', 'get_members']
	search_fields = ['GroupID', 'User_ID']
	list_filter = ['GroupID']
admin.site.register(UserGroup, UserGroupAdmin)

class EvaluationRoundAdmin(admin.ModelAdmin):
	list_display = ['EvaluationRoundID', 'Date']
	search_fields = ['EvaluationRoundID', 'Date']
	list_filter = ['EvaluationRoundID','Date']
admin.site.register(EvaluationRound, EvaluationRoundAdmin)

class EvaluationAdmin(admin.ModelAdmin):
	list_display = ['EvaluationID', 'Evaluated', 'Evaluator', 'EvaluationRound_ID', 'Technical', 'Professional', 'Teamwork', 'ForceEval', 'EvalApplied', 'EvaluationDate', 'CurrentBoss']
	search_fields = ['EvaluationID', 'Evaluated', 'Evaluator', 'EvaluationRound_ID', 'Technical', 'Professional', 'Teamwork', 'ForceEval', 'EvalApplied', 'EvaluationDate', 'CurrentBoss']
	list_filter = ['EvaluationID', 'Evaluated', 'Evaluator', 'Technical', 'Professional', 'Teamwork', 'ForceEval', 'EvalApplied', 'EvaluationDate', 'CurrentBoss']
admin.site.register(Evaluation, EvaluationAdmin)

class EntityTypeAdmin(admin.ModelAdmin):
	list_display = ['EntityTypeID', 'EntityName']
	search_fields = ['EntityTypeID', 'EntityName']
	list_filter = ['EntityTypeID', 'EntityName']
admin.site.register(EntityType, EntityTypeAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'Comments', 'Date', 'EntityID', 'EntityType_ID', 'User_ID']
	search_fields = ['id', 'Comments', 'Date', 'EntityID', 'EntityType_ID', 'User_ID']
	list_filter = ['id', 'Comments', 'Date', 'EntityID']
admin.site.register(Comment, CommentAdmin)

class AlarmAdmin(admin.ModelAdmin):
	list_display = ['AlarmID', 'Due', 'What', 'Action_ID', 'Mode', 'LastFired', 'EntityID', 'EntityType_ID', 'Status_ID']
	search_fields = ['AlarmID', 'Due', 'What', 'Action_ID', 'Mode', 'LastFired', 'EntityID', 'EntityType_ID', 'Status_ID']
	list_filter = ['AlarmID', 'Due', 'What', 'Action_ID', 'Mode', 'LastFired', 'EntityID']
admin.site.register(Alarm, AlarmAdmin)

class AlarmReminderAdmin(admin.ModelAdmin):
	list_display = ['AlarmReminderID', 'DaysBefore', 'Fired', 'Alarm_ID']
	search_fields = ['AlarmReminderID', 'DaysBefore', 'Fired', 'Alarm_ID']
	list_filter = ['AlarmReminderID', 'DaysBefore', 'Fired']
admin.site.register(AlarmReminder, AlarmReminderAdmin)

class AlarmActionParameterAdmin(admin.ModelAdmin):
	list_display = ['id', 'Parameter', 'Alarm_ID']
	search_fields = ['id', 'Parameter', 'Alarm_ID']
	list_filter = ['id', 'Parameter']
admin.site.register(AlarmActionParameter, AlarmActionParameterAdmin)

class CommandsAdmin(admin.ModelAdmin):
	list_display = ['id', 'CommandName']
	search_fields = ['id', 'CommandName']
	list_filter = ['id', 'CommandName']
admin.site.register(Commands, CommandsAdmin)

class PriviledgesMatrixAdmin(admin.ModelAdmin):
	list_display = ['Commands_ID', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
	search_fields = ['Commands_ID', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
	list_filter = ['Commands_ID', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
admin.site.register(PriviledgesMatrix, PriviledgesMatrixAdmin)

class CommandRelationsAdmin(admin.ModelAdmin):
	list_display = ['id', 'Command', 'RelatedTo']
	search_fields = ['id', 'Command', 'RelatedTo']
	list_filter = ['id', 'Command', 'RelatedTo']
admin.site.register(CommandRelations, CommandRelationsAdmin)

class ExtendedPermissionsAdmin(admin.ModelAdmin):
	list_display = ['id', 'Action', 'Commands_ID', 'User_ID']
	search_fields = ['id', 'Action', 'Commands_ID', 'User_ID']
	list_filter = ['id', 'Action']
admin.site.register(ExtendedPermissions, ExtendedPermissionsAdmin)

class NotificationAdmin(admin.ModelAdmin):
	list_display = ['NotificationID', 'AlreadyRead', 'TypeID', 'From', 'AddressedTo', 'Subject', 'DateTime', 'Status_ID']
	search_fields = ['NotificationID', 'AlreadyRead', 'TypeID', 'From', 'AddressedTo', 'Subject', 'DateTime', 'Status_ID']
	list_filter = ['NotificationID', 'AlreadyRead', 'TypeID', 'From', 'AddressedTo', 'Subject', 'DateTime']
admin.site.register(Notification, NotificationAdmin)

class NotificationMetadataAdmin(admin.ModelAdmin):
	list_display = ['ID', 'MetadataName', 'MetadataValue', 'Notification_ID']
	search_fields = ['ID', 'MetadataName', 'MetadataValue', 'Notification_ID']
	list_filter = ['ID', 'MetadataName', 'MetadataValue']
admin.site.register(NotificationMetadata, NotificationMetadataAdmin)

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['ProjectID', 'ProjectName', 'ProjectNickname', 'Director', 'Producer', 'Studio', 'ConsumableAllowance', 'Contingency', 'ImageAssetID', 'Active', 'CreationDate', 'RestrictShotsToAssignedUsers', 'StartDate']
	search_fields = ['ProjectID', 'ProjectName', 'ProjectNickname', 'Director', 'Producer', 'Studio', 'ConsumableAllowance', 'Contingency', 'ImageAssetID', 'Active', 'CreationDate', 'RestrictShotsToAssignedUsers', 'StartDate']
	list_filter = ['ProjectID', 'ProjectName', 'ProjectNickname', 'Director', 'Producer', 'Studio', 'ConsumableAllowance', 'Contingency', 'ImageAssetID', 'Active', 'CreationDate', 'RestrictShotsToAssignedUsers', 'StartDate']
admin.site.register(Project, ProjectAdmin)

class MilestoneAdmin(admin.ModelAdmin):
	list_display = ['MilestoneID', 'Name', 'Date', 'Project_ID']
	search_fields = ['MilestoneID', 'Name', 'Date', 'Project_ID']
	list_filter = ['MilestoneID', 'Name', 'Date']
admin.site.register(Milestone, MilestoneAdmin)

class IncomingFileAdmin(admin.ModelAdmin):
	list_display = ['IncomingFileID', 'Date', 'Sender', 'AddressedTo', 'SourcePath', 'FinalPath', 'Area', 'Media', 'Project_ID']
	search_fields = ['IncomingFileID', 'Date', 'Sender', 'AddressedTo', 'SourcePath', 'FinalPath', 'Area', 'Media', 'Project_ID']
	list_filter = ['IncomingFileID', 'Date', 'Sender', 'AddressedTo', 'SourcePath', 'FinalPath', 'Area', 'Media']
admin.site.register(IncomingFile, IncomingFileAdmin)

class ProjectUserAdmin(admin.ModelAdmin):
	list_display = ['id', 'Project_ID', 'User_ID']
	search_fields = ['id', 'Project_ID', 'User_ID']
	list_filter= ['id']
admin.site.register(ProjectUser, ProjectUserAdmin)

class PlaylistAdmin(admin.ModelAdmin):
	list_display = ['PlaylistID', 'PlaylistName', 'AutoUpdate', 'Project_ID']
	search_fields = ['PlaylistID', 'PlaylistName', 'AutoUpdate', 'Project_ID']
	list_filter = ['PlaylistID', 'PlaylistName', 'AutoUpdate']
admin.site.register(Playlist, PlaylistAdmin)

class RateSetAdmin(admin.ModelAdmin):
	list_display = ['RateSetID', 'RateSetNumber', 'RateSetName', 'RateSetNotes', 'RateSetCreationDate', 'RateSetLastModification', 'RateSetConsumableAllowance', 'RateSetContingency', 'RateSetExtra', 'RateSetExtraIT', 'Project_ID']
	search_fields = ['RateSetID', 'RateSetNumber', 'RateSetName', 'RateSetNotes', 'RateSetCreationDate', 'RateSetLastModification', 'RateSetConsumableAllowance', 'RateSetContingency', 'RateSetExtra', 'RateSetExtraIT', 'Project_ID']
	list_filter = ['RateSetID', 'RateSetNumber', 'RateSetName', 'RateSetNotes', 'RateSetCreationDate', 'RateSetLastModification', 'RateSetConsumableAllowance', 'RateSetContingency', 'RateSetExtra', 'RateSetExtraIT']
admin.site.register(RateSet, RateSetAdmin)

class HardDiskStatusAdmin(admin.ModelAdmin):
	list_display = ['HardDiskStatusID', 'HardDiskStatusName']
	search_fields = ['HardDiskStatusID', 'HardDiskStatusName']
	list_filter = ['HardDiskStatusID', 'HardDiskStatusName']
admin.site.register(HardDiskStatus, HardDiskStatusAdmin)

class HardDiskRegisterAdmin(admin.ModelAdmin):
	list_display = ['HardDiskRegisterID', 'SerialNumber', 'HardDiskNumber', 'HardDiskName', 'FromAddress', 'ContentOnArrival', 'ArrivalDate', 'ContentOnExit', 'ExitDate', 'HardDiskStatus_ID', 'Project_ID']
	search_fields = ['HardDiskRegisterID', 'SerialNumber', 'HardDiskNumber', 'HardDiskName', 'FromAddress', 'ContentOnArrival', 'ArrivalDate', 'ContentOnExit', 'ExitDate', 'HardDiskStatus_ID', 'Project_ID']
	list_filter = ['HardDiskRegisterID', 'SerialNumber', 'HardDiskNumber', 'HardDiskName', 'FromAddress', 'ContentOnArrival', 'ArrivalDate', 'ContentOnExit', 'ExitDate']
admin.site.register(HardDiskRegister, HardDiskRegisterAdmin)

class UploadControlAdmin(admin.ModelAdmin):
	list_display = ['UploadControlID', 'Filename', 'Path', 'Date', 'Project_ID', 'User_ID']
	search_fields = ['UploadControlID', 'Filename', 'Path', 'Date', 'Project_ID', 'User_ID']
	list_filter = ['UploadControlID', 'Filename', 'Path', 'Date']
admin.site.register(UploadControl, UploadControlAdmin)

class StorageUseAdmin(admin.ModelAdmin):
	list_display = ['id', 'ProjectNickname', 'VFXID', 'VersionNumber', 'Size', 'Project_ID', 'User_ID']
	search_fields = ['id', 'ProjectNickname', 'VFXID', 'VersionNumber', 'Size', 'Project_ID', 'User_ID']
	list_filter = ['id', 'ProjectNickname', 'VFXID', 'VersionNumber', 'Size']
admin.site.register(StorageUse, StorageUseAdmin)

class ServiceTypeAdmin(admin.ModelAdmin):
	list_display = ['id', 'ServiceTypeName']
	search_fields = ['id', 'ServiceTypeName']
	list_filter = ['id', 'ServiceTypeName']
admin.site.register(ServiceType, ServiceTypeAdmin)

class ServiceAdmin(admin.ModelAdmin):
	list_display = ['ServiceID', 'ServiceName', 'CostPerDay', 'ServiceType_ID']
	search_fields = ['ServiceID', 'ServiceName', 'CostPerDay', 'ServiceType_ID']
	list_filter = ['ServiceID', 'ServiceName', 'CostPerDay']
admin.site.register(Service, ServiceAdmin)

class ServiceHistogramColorAdmin(admin.ModelAdmin):
	list_display = ['ServiceHistogramColorID', 'R', 'G', 'B', 'Service_ID']
	search_fields = ['ServiceHistogramColorID', 'R', 'G', 'B', 'Service_ID']
	list_filter = ['ServiceHistogramColorID', 'R', 'G', 'B']
admin.site.register(ServiceHistogramColor, ServiceHistogramColorAdmin)

class ProjectServiceAdmin(admin.ModelAdmin):
	list_display = ['ProjectServiceID', 'Rate', 'RateSetNumber', 'Project_ID', 'Service_ID']
	search_fields = ['ProjectServiceID', 'Rate', 'RateSetNumber', 'Project_ID', 'Service_ID']
	list_filter = ['ProjectServiceID', 'Rate', 'RateSetNumber']
admin.site.register(ProjectService, ProjectServiceAdmin)

class ProjectTaskServiceAdmin(admin.ModelAdmin):
	list_display = ['ProjectTaskServiceID', 'Slots', 'Project_ID', 'Service_ID']
	search_fields = ['ProjectTaskServiceID', 'Slots', 'Project_ID', 'Service_ID']
	list_filter = ['ProjectTaskServiceID', 'Slots']
admin.site.register(ProjectTaskService, ProjectTaskServiceAdmin)

class AssetTypeAdmin(admin.ModelAdmin):
	list_display = ['AssetTypeID', 'AssetTypeName']
	search_fields = ['AssetTypeID', 'AssetTypeName']
	list_filter = ['AssetTypeID', 'AssetTypeName']
admin.site.register(AssetType, AssetTypeAdmin)

class SequencialIDGeneratorAdmin(admin.ModelAdmin):
	list_display = ['SIG_id']
	search_fields = ['SIG_id']
	list_filter = ['SIG_id']
admin.site.register(SequencialIDGenerator, SequencialIDGeneratorAdmin)

class SequenceAdmin(admin.ModelAdmin):
	list_display = ['SequencialIDGenerator_ID', 'SequenceName', 'SequenceNickname', 'Project_ID']
	search_fields = ['SequencialIDGenerator_ID', 'SequenceName', 'SequenceNickname', 'Project_ID']
	list_filter = ['SequencialIDGenerator_ID', 'SequenceName', 'SequenceNickname']
admin.site.register(Sequence, SequenceAdmin)

class ShotAdmin(admin.ModelAdmin):
	list_display = ['ShotID', 'VFXID', 'ExternalID', 'ShotName', 'Location', 'CameraMotion', 'SceneNumber', 'PageNumber', 'Frames', 'ImageAssetID', 'WorkedeBy', 'Type', 'Lens', 'VFXTasks', 'IsReference', 'SortIndex', 'Take', 'Active', 'PrimaryBidNumber', 'Project_ID', 'Sequence_ID', 'Status_ID']
	search_fields = ['ShotID', 'VFXID', 'ExternalID', 'ShotName', 'Location', 'CameraMotion', 'SceneNumber', 'PageNumber', 'Frames', 'ImageAssetID', 'WorkedeBy', 'Type', 'Lens', 'VFXTasks', 'IsReference', 'SortIndex', 'Take', 'Active', 'PrimaryBidNumber', 'Project_ID', 'Sequence_ID', 'Status_ID']
	list_filter = ['ShotID', 'VFXID', 'ExternalID', 'ShotName', 'Location', 'CameraMotion', 'SceneNumber', 'PageNumber', 'Frames', 'ImageAssetID', 'WorkedeBy', 'Type', 'Lens', 'VFXTasks', 'IsReference', 'SortIndex', 'Take', 'Active']
admin.site.register(Shot, ShotAdmin)

class BidAdmin(admin.ModelAdmin):
	list_display = ['BidID', 'BidNumber', 'BidName', 'BidDate', 'BidLastModification', 'AddConsumablesAllowance', 'RateSetNumber', 'HideInCalendar', 'Project_ID', 'Shot_ID']
	search_fields = ['BidID', 'BidNumber', 'BidName', 'BidDate', 'BidLastModification', 'AddConsumablesAllowance', 'RateSetNumber', 'HideInCalendar', 'Project_ID', 'Shot_ID']
	list_filter = ['BidID', 'BidNumber', 'BidName', 'BidDate', 'BidLastModification', 'AddConsumablesAllowance', 'RateSetNumber', 'HideInCalendar']
admin.site.register(Bid, BidAdmin)

class AssetsAdmin(admin.ModelAdmin):
	list_display = ['AssetID', 'AssetName', 'Size', 'UploadDate', 'Public', 'Parent', 'LastModified', 'OnCloud', 'CloudStatus', 'AssetType_ID', 'Project_ID', 'Shot_ID', 'User_ID_Uploader']
	search_fields = ['AssetID', 'AssetName', 'Size', 'UploadDate', 'Public', 'Parent', 'LastModified', 'OnCloud', 'CloudStatus', 'AssetType_ID', 'Project_ID', 'Shot_ID', 'User_ID_Uploader']
	list_filter = ['AssetID', 'AssetName', 'Size', 'UploadDate', 'Public', 'Parent', 'LastModified', 'OnCloud', 'CloudStatus']
admin.site.register(Assets, AssetsAdmin)

class TransferAdmin(admin.ModelAdmin):
	list_display = ['TransferID', 'Date', 'IP', 'Type', 'Assets_ID', 'User_ID']
	search_fields = ['TransferID', 'Date', 'IP', 'Type', 'Assets_ID', 'User_ID']
	list_filter = ['TransferID', 'Date', 'IP', 'Type']
admin.site.register(Transfer, TransferAdmin)

class AssetPriviledgesAdmin(admin.ModelAdmin):
	list_display = ['id', 'Assets_ID', 'UserTypes_ID']
	search_fields = ['id', 'Assets_ID', 'UserTypes_ID']
	list_filter = ['id']
admin.site.register(AssetPriviledges, AssetPriviledgesAdmin)

class DeletedAssetsAdmin(admin.ModelAdmin):
	list_display = ['DeletedAssetID', 'AssetName', 'AssetType', 'Size', 'UploadDate', 'Public', 'Assets_ID', 'Project_ID', 'User_ID_Uploader']
	search_fields = ['DeletedAssetID', 'AssetName', 'AssetType', 'Size', 'UploadDate', 'Public', 'Assets_ID', 'Project_ID', 'User_ID_Uploader']
	list_filter = ['DeletedAssetID', 'AssetName', 'AssetType', 'Size', 'UploadDate', 'Public']
admin.site.register(DeletedAssets, DeletedAssetsAdmin)

class DownloadControlAdmin(admin.ModelAdmin):
	list_display = ['DownloadControlID', 'Path', 'Date', 'Assets_ID', 'User_ID']
	search_fields = ['DownloadControlID', 'Path', 'Date', 'Assets_ID', 'User_ID']
	list_filter = ['DownloadControlID', 'Path', 'Date']
admin.site.register(DownloadControl, DownloadControlAdmin)

class ShotsServiceAdmin(admin.ModelAdmin):
	list_display = ['ShotServiceID', 'Days', 'BidNumber', 'Project_ID', 'Service_ID', 'Shot_ID']
	search_fields = ['ShotServiceID', 'Days', 'BidNumber', 'Project_ID', 'Service_ID', 'Shot_ID']
	list_filter = ['ShotServiceID', 'Days', 'BidNumber']
admin.site.register(ShotsService, ShotsServiceAdmin)

class ShotsAssetsAdmin(admin.ModelAdmin):
	list_display = ['ShotsAssetsID', 'Assets_ID', 'Project_ID', 'Shot_ID']
	search_fields = ['ShotsAssetsID', 'Assets_ID', 'Project_ID', 'Shot_ID']
	list_filter = ['ShotsAssetsID']
admin.site.register(ShotsAssets, ShotsAssetsAdmin)

class ShotStatusLogAdmin(admin.ModelAdmin):
	list_display = ['id', 'FromStatus', 'ToStatus', 'Date', 'Project_ID', 'Shot_ID', 'User_ID']
	search_fields = ['id', 'FromStatus', 'ToStatus', 'Date', 'Project_ID', 'Shot_ID', 'User_ID']
	list_filter = ['id', 'FromStatus', 'ToStatus', 'Date']
admin.site.register(ShotStatusLog, ShotStatusLogAdmin)

class ShotDeliveryAdmin(admin.ModelAdmin):
	list_display = ['id', 'VFXID', 'ShotName', 'ReviewDate', 'InternalVersion', 'ClientVersion', 'Work', 'Stereo', 'Project_ID', 'Shot_ID', 'Status_ID']
	search_fields = ['id', 'VFXID', 'ShotName', 'ReviewDate', 'InternalVersion', 'ClientVersion', 'Work', 'Stereo', 'Project_ID', 'Shot_ID', 'Status_ID']
	list_filter = ['id', 'VFXID', 'ShotName', 'ReviewDate', 'InternalVersion', 'ClientVersion', 'Work', 'Stereo']
admin.site.register(ShotDelivery, ShotDeliveryAdmin)

class ShotGroupAdmin(admin.ModelAdmin):
	list_display = ['ShotGroupID', 'ShotGroupName', 'ShotGroupNotes', 'Project_ID']
	search_fields = ['ShotGroupID', 'ShotGroupName', 'ShotGroupNotes', 'Project_ID']
	list_filter = ['ShotGroupID', 'ShotGroupName', 'ShotGroupNotes']
admin.site.register(ShotGroup, ShotGroupAdmin)

class ShotGroupShotIDAdmin(admin.ModelAdmin):
	list_display = ['id', 'Shot_ID', 'ShotGroup_ID']
	search_fields = ['id', 'Shot_ID', 'ShotGroup_ID']
	list_filter = ['id']
admin.site.register(ShotGroupShotID, ShotGroupShotIDAdmin)

class ShotGroupTentpoleAdmin(admin.ModelAdmin):
	list_display = ['id', 'Shot_ID', 'ShotGroup_ID']
	search_fields = ['id', 'Shot_ID', 'ShotGroup_ID']
	list_filter = ['id']
admin.site.register(ShotGroupTentpole, ShotGroupTentpoleAdmin)

class ShotUserAdmin(admin.ModelAdmin):
	list_display = ['id', 'Shot_ID', 'User_ID']
	search_fields = ['id', 'Shot_ID', 'User_ID']
	list_filter = ['id']
admin.site.register(ShotUser, ShotUserAdmin)

class SelectionSetAdmin(admin.ModelAdmin):
	list_display = ['SelectionSetID', 'SelectionSetName', 'Project_ID']
	search_fields = ['SelectionSetID', 'SelectionSetName', 'Project_ID']
	list_filter = ['SelectionSetID', 'SelectionSetName']
admin.site.register(SelectionSet, SelectionSetAdmin)

class ShotSelectionSetAdmin(admin.ModelAdmin):
	list_display = ['ShotSelectionSetID', 'SelectionSet_ID', 'Shot_ID']
	search_fields = ['ShotSelectionSetID', 'SelectionSet_ID', 'Shot_ID']
	list_filter = ['ShotSelectionSetID']
admin.site.register(ShotSelectionSet, ShotSelectionSetAdmin)

class CustomShotFieldAdmin(admin.ModelAdmin):
	list_display = ['CustomShotFieldID', 'FieldName', 'DefaultValue', 'Project_ID']
	search_fields = ['CustomShotFieldID', 'FieldName', 'DefaultValue', 'Project_ID']
	list_filter = ['CustomShotFieldID', 'FieldName', 'DefaultValue']
admin.site.register(CustomShotField, CustomShotFieldAdmin)

class ShotCustomShotFieldAdmin(admin.ModelAdmin):
	list_display = ['ShotCustomShotFieldID', 'Value', 'CustomShotField_ID', 'Shot_ID']
	search_fields = ['ShotCustomShotFieldID', 'Value', 'CustomShotField_ID', 'Shot_ID']
	list_filter = ['ShotCustomShotFieldID', 'Value']
admin.site.register(ShotCustomShotField, ShotCustomShotFieldAdmin)

class VersionAdmin(admin.ModelAdmin):
	list_display = ['VersionID', 'Major', 'Minor', 'External', 'CreationDate', 'View', 'Task', 'PublishedBy', 'Shot_ID']
	search_fields = ['VersionID', 'Major', 'Minor', 'External', 'CreationDate', 'View', 'Task', 'PublishedBy', 'Shot_ID']
	list_filter = ['VersionID', 'Major', 'Minor', 'External', 'CreationDate', 'View', 'Task', 'PublishedBy']
admin.site.register(Version, VersionAdmin)

class VersionAssetAdmin(admin.ModelAdmin):
	list_display = ['VersionAssetID', 'Assets_ID', 'Version_ID']
	search_fields = ['VersionAssetID', 'Assets_ID', 'Version_ID']
	list_filter = ['VersionAssetID']
admin.site.register(VersionAsset, VersionAssetAdmin)

class ScriptAdmin(admin.ModelAdmin):
	list_display = ['id', 'ScriptName', 'MajorVersion', 'MinorVersion', 'Task', 'STask', 'Project_ID', 'Shot_ID', 'User_ID']
	search_fields = ['id', 'ScriptName', 'MajorVersion', 'MinorVersion', 'Task', 'STask', 'Project_ID', 'Shot_ID', 'User_ID']
	list_filter = ['id', 'ScriptName', 'MajorVersion', 'MinorVersion', 'Task', 'STask']
admin.site.register(Script, ScriptAdmin)

class PublishJobAdmin(admin.ModelAdmin):
	list_display = ['id', 'CreationDate', 'CreatedBy', 'PublishDate', 'PublishType', 'Script_ID', 'Status_ID']
	search_fields = ['id', 'CreationDate', 'CreatedBy', 'PublishDate', 'PublishType', 'Script_ID', 'Status_ID']
	list_filter = ['id', 'CreationDate', 'CreatedBy', 'PublishDate', 'PublishType']
admin.site.register(PublishJob, PublishJobAdmin)

class LineupAdmin(admin.ModelAdmin):
	list_display = ['id', 'CreationDate', 'CreatedBy', 'Name', 'Camera', 'TStop', 'FrameSize', 'CutLengthFrames', 'InFrame', 'InTC', 'OutFrame', 'OutTC', 'FramesWithHandles', 'InFramesWithHandles', 'InTCWithHandles', 'OutFrameWithHandles', 'OutTCWithHandles', 'RawMediaStart', 'RawMediaEnd', 'RawMediaDuration', 'RawMediaStartFrame', 'RawMediaEndFrame', 'RawMediaDurationFrames', 'EditorialName', 'EDLPull', 'Format', 'ISO', 'Kelvin', 'Lens', 'Reel', 'ReelID', 'Scene', 'Setup', 'ShootDate', 'ShootDay', 'ShuttleAngle', 'ShutterSpeed', 'StabilizeCurvesSent', 'Take', 'Tint', 'Project_ID', 'Shot_ID']
	search_fields = ['id', 'CreationDate', 'CreatedBy', 'Name', 'Camera', 'TStop', 'FrameSize', 'CutLengthFrames', 'InFrame', 'InTC', 'OutFrame', 'OutTC', 'FramesWithHandles', 'InFramesWithHandles', 'InTCWithHandles', 'OutFrameWithHandles', 'OutTCWithHandles', 'RawMediaStart', 'RawMediaEnd', 'RawMediaDuration', 'RawMediaStartFrame', 'RawMediaEndFrame', 'RawMediaDurationFrames', 'EditorialName', 'EDLPull', 'Format', 'ISO', 'Kelvin', 'Lens', 'Reel', 'ReelID', 'Scene', 'Setup', 'ShootDate', 'ShootDay', 'ShuttleAngle', 'ShutterSpeed', 'StabilizeCurvesSent', 'Take', 'Tint',  'Project_ID', 'Shot_ID']
	list_filter = ['id', 'CreationDate', 'CreatedBy', 'Name', 'Camera', 'TStop', 'FrameSize', 'CutLengthFrames', 'InFrame', 'InTC', 'OutFrame', 'OutTC', 'FramesWithHandles', 'InFramesWithHandles', 'InTCWithHandles', 'OutFrameWithHandles', 'OutTCWithHandles', 'RawMediaStart', 'RawMediaEnd', 'RawMediaDuration', 'RawMediaStartFrame', 'RawMediaEndFrame', 'RawMediaDurationFrames', 'EditorialName', 'EDLPull', 'Format', 'ISO', 'Kelvin', 'Lens', 'Reel', 'ReelID', 'Scene', 'Setup', 'ShootDate', 'ShootDay', 'ShuttleAngle', 'ShutterSpeed', 'StabilizeCurvesSent', 'Take', 'Tint']
admin.site.register(Lineup, LineupAdmin)

class SalaryGeneralDataAdmin(admin.ModelAdmin):
	list_display = ['MaxSalaryInc', 'CPIMX', 'CPIUSA', 'CPIAdjustStrategy']
	search_fields = ['MaxSalaryInc', 'CPIMX', 'CPIUSA', 'CPIAdjustStrategy']
	list_filter = ['MaxSalaryInc', 'CPIMX', 'CPIUSA', 'CPIAdjustStrategy']
admin.site.register(SalaryGeneralData, SalaryGeneralDataAdmin)

class SalaryStructureAdmin(admin.ModelAdmin):
	list_display = ['id', 'SalaryName', 'SalaryDefinition', 'SalaryMidRange', 'LevelIncrease', 'CurrentType', 'Salary1', 'Salary2', 'Salary3', 'Salary4', 'Salary5', 'Salary6', 'Salary7', 'Salary8', 'Salary9', 'SalaryGeneralData_ID']
	search_fields = ['id', 'SalaryName', 'SalaryDefinition', 'SalaryMidRange', 'LevelIncrease', 'CurrentType', 'Salary1', 'Salary2', 'Salary3', 'Salary4', 'Salary5', 'Salary6', 'Salary7', 'Salary8', 'Salary9', 'SalaryGeneralData_ID']
	list_filter = ['id', 'SalaryName', 'SalaryDefinition', 'SalaryMidRange', 'LevelIncrease', 'CurrentType', 'Salary1', 'Salary2', 'Salary3', 'Salary4', 'Salary5', 'Salary6', 'Salary7', 'Salary8', 'Salary9']
admin.site.register(SalaryStructure, SalaryStructureAdmin)

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['id', 'DepartmentName', 'DepartmentHeadID']
	search_fields = ['id', 'DepartmentName', 'DepartmentHeadID']
	list_filter = ['id', 'DepartmentName', 'DepartmentHeadID']
admin.site.register(Department, DepartmentAdmin)

class AssociateAdmin(admin.ModelAdmin):
	list_display = ['id', 'FirstName', 'LastName', 'Active', 'CurrentSalary', 'LastIncrease', 'LastCOLncrease', 'IncreaseApply', 'BossID', 'FirstHired', 'Title', 'Address', 'Phone', 'AllowedDaysPerYear', 'Department_ID', 'SalaryStructure_ID', 'User_ID']
	search_fields = ['id', 'FirstName', 'LastName', 'Active', 'CurrentSalary', 'LastIncrease', 'LastCOLncrease', 'IncreaseApply', 'BossID', 'FirstHired', 'Title', 'Address', 'Phone', 'AllowedDaysPerYear', 'Department_ID', 'SalaryStructure_ID', 'User_ID']
	list_filter = ['id', 'FirstName', 'LastName', 'Active', 'CurrentSalary', 'LastIncrease', 'LastCOLncrease', 'IncreaseApply', 'BossID', 'FirstHired', 'Title', 'Address', 'Phone', 'AllowedDaysPerYear']
admin.site.register(Associate, AssociateAdmin)

class COLAdmin(admin.ModelAdmin):
	list_display = ['id', 'Name', 'Year', 'COL']
	search_fields = ['id', 'Name', 'Year', 'COL']
	list_filter = ['id', 'Name', 'Year', 'COL']
admin.site.register(COL, COLAdmin)

class MeritPercentagesAdmin(admin.ModelAdmin):
	list_display = ['SalaryQuartile', 'Rate0', 'Rate1', 'Rate2', 'Rate3', 'Rate4']
	search_fields = ['SalaryQuartile', 'Rate0', 'Rate1', 'Rate2', 'Rate3', 'Rate4']
	list_filter = ['SalaryQuartile', 'Rate0', 'Rate1', 'Rate2', 'Rate3', 'Rate4']
admin.site.register(MeritPercentages, MeritPercentagesAdmin)

class AssociateSalaryHistoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'SalaryModDate', 'OldSalary', 'NewSalary', 'PerformanceRating', 'CostOfLiving', 'MeritIncrease', 'MeritAmount', 'PromotionBonus', 'PromotionBonusAmount', 'SalaryEndDate', 'UpdatedBy', 'Associate_ID', 'COL_ID', 'SalaryQuartile', 'SalaryStructure_ID']
	search_fields = ['id', 'SalaryModDate', 'OldSalary', 'NewSalary', 'PerformanceRating', 'CostOfLiving', 'MeritIncrease', 'MeritAmount', 'PromotionBonus', 'PromotionBonusAmount', 'SalaryEndDate', 'UpdatedBy', 'Associate_ID', 'COL_ID', 'SalaryQuartile', 'SalaryStructure_ID']
	list_filter = ['id', 'SalaryModDate', 'OldSalary', 'NewSalary', 'PerformanceRating', 'CostOfLiving', 'MeritIncrease', 'MeritAmount', 'PromotionBonus', 'PromotionBonusAmount', 'SalaryEndDate', 'UpdatedBy']
admin.site.register(AssociateSalaryHistory, AssociateSalaryHistoryAdmin)

class VacationPeriodAdmin(admin.ModelAdmin):
	list_display = ['id', 'StartDate', 'EndDate', 'AllowedDays', 'Number', 'Associate_ID']
	search_fields = ['id', 'StartDate', 'EndDate', 'AllowedDays', 'Number', 'Associate_ID']
	list_filter = ['id', 'StartDate', 'EndDate', 'AllowedDays', 'Number']
admin.site.register(VacationPeriod, VacationPeriodAdmin)

class VacationEventAdmin(admin.ModelAdmin):
	list_display = ['id', 'PeriodID', 'StartDate', 'EndDate', 'Days', 'DaysBeforeEvent', 'VacationPeriod_ID']
	search_fields = ['id', 'PeriodID', 'StartDate', 'EndDate', 'Days', 'DaysBeforeEvent', 'VacationPeriod_ID']
	list_filter = ['id', 'PeriodID', 'StartDate', 'EndDate', 'Days', 'DaysBeforeEvent']
admin.site.register(VacationEvent, VacationEventAdmin)

class AccessControlAdmin(admin.ModelAdmin):
	list_display = ['id', 'EnrollID', 'CardID', 'Priviledge', 'Associate_ID']
	search_fields = ['id', 'EnrollID', 'CardID', 'Priviledge', 'Associate_ID']
	list_filter = ['id', 'EnrollID', 'CardID', 'Priviledge']
admin.site.register(AccessControl, AccessControlAdmin)

class ContractEventAdmin(admin.ModelAdmin):
	list_display = ['id', 'StartDate', 'DurationDays', 'AllowedDays', 'CurrentSalary', 'Title', 'ByProject', 'Valid', 'Associate_ID', 'Department_ID', 'SalaryStructure_ID']
	search_fields = ['id', 'StartDate', 'DurationDays', 'AllowedDays', 'CurrentSalary', 'Title', 'ByProject', 'Valid', 'Associate_ID', 'Department_ID', 'SalaryStructure_ID']
	list_filter = ['id', 'StartDate', 'DurationDays', 'AllowedDays', 'CurrentSalary', 'Title', 'ByProject', 'Valid']
admin.site.register(ContractEvent, ContractEventAdmin)

class InventoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'Type', 'InDate', 'Name', 'Distributor', 'Condition', 'Location', 'Cost', 'Serial', 'BarCode', 'InternalBarCode', 'Department_ID']
	search_fields = ['id', 'Type', 'InDate', 'Name', 'Distributor', 'Condition', 'Location', 'Cost', 'Serial', 'BarCode', 'InternalBarCode', 'Department_ID']
	list_filter = ['id', 'Type', 'InDate', 'Name', 'Distributor', 'Condition', 'Location', 'Cost', 'Serial', 'BarCode', 'InternalBarCode']
admin.site.register(Inventory, InventoryAdmin)

class AccessControlDeviceAdmin(admin.ModelAdmin):
	list_display = ['id', 'DeviceName', 'IP', 'Port', 'IsSSR', 'IsUSB', 'ReadsCards', 'ReadsFingerprints', 'Inventory_ID']
	search_fields = ['id', 'DeviceName', 'IP', 'Port', 'IsSSR', 'IsUSB', 'ReadsCards', 'ReadsFingerprints', 'Inventory_ID']
	list_filter = ['id', 'DeviceName', 'IP', 'Port', 'IsSSR', 'IsUSB', 'ReadsCards', 'ReadsFingerprints']
admin.site.register(AccessControlDevice, AccessControlDeviceAdmin)

class TaskStatusAdmin(admin.ModelAdmin):
	list_display = ['id', 'TaskStatusName']
	search_fields = ['id', 'TaskStatusName']
	list_filter = ['id', 'TaskStatusName']
admin.site.register(TaskStatus, TaskStatusAdmin)

class TaskEntityTypeAdmin(admin.ModelAdmin):
	list_display = ['id', 'Entity']
	search_fields = ['id', 'Entity']
	list_filter = ['id', 'Entity']
admin.site.register(TaskEntityType, TaskEntityTypeAdmin)

class TaskAdmin(admin.ModelAdmin):
	list_display = ['id', 'TaskName', 'Parent_ID', 'Offset', 'OffsetType_ID', 'Duration', 'Position', 'Hidden', 'BakedStartDate', 'BakedEndDate', 'OriginalStartDate', 'OriginalEndDate', 'IdleDays', 'IsClone', 'IsActive', 'Project_ID', 'TaskEntityType_ID', 'TaskStatus_ID']
	search_fields = ['id', 'TaskName', 'Parent_ID', 'Offset', 'OffsetType_ID', 'Duration', 'Position', 'Hidden', 'BakedStartDate', 'BakedEndDate', 'OriginalStartDate', 'OriginalEndDate', 'IdleDays', 'IsClone', 'IsActive', 'Project_ID', 'TaskEntityType_ID', 'TaskStatus_ID']
	list_filter = ['id', 'TaskName', 'Parent_ID', 'Offset', 'OffsetType_ID', 'Duration', 'Position', 'Hidden', 'BakedStartDate', 'BakedEndDate', 'OriginalStartDate', 'OriginalEndDate', 'IdleDays', 'IsClone', 'IsActive']
admin.site.register(Task, TaskAdmin)

class TaskArtistAdmin(admin.ModelAdmin):
	list_display = ['id', 'Task_ID', 'User_ID']
	search_fields = ['id', 'Task_ID', 'User_ID']
	list_filter = ['id']
admin.site.register(TaskArtist, TaskArtistAdmin)

class TaskDependenciesAdmin(admin.ModelAdmin):
	list_display = ['Dependency_ID', 'Task_ID']
	search_fields = ['Dependency_ID', 'Task_ID']
	list_filter = ['Dependency_ID']
admin.site.register(TaskDependencies, TaskDependenciesAdmin)