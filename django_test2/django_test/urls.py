from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    url(r'^upload_usertype/$', 'ollinvfx.views.upload_usertype', name='upload_usertype'),
    url(r'^upload_user/$', 'ollinvfx.views.upload_user', name='upload_user'),
    url(r'^upload_accesscontrolfingerprint/$', 'ollinvfx.views.upload_accesscontrolfingerprint', name='upload_accesscontrolfingerprint'),
    url(r'^upload_status/$', 'ollinvfx.views.upload_status', name='upload_status'),
    url(r'^upload_accesscontrollog/$', 'ollinvfx.views.upload_accesscontrollog', name='upload_accesscontrollog'),
    url(r'^upload_loginattempt/$', 'ollinvfx.views.upload_loginattempt', name='upload_loginattempt'),
    url(r'^upload_usergroup/$', 'ollinvfx.views.upload_usergroup', name='upload_usergroup'),
    url(r'^upload_evaluationround/$', 'ollinvfx.views.upload_evaluationround', name='upload_evaluationround'),
    url(r'^upload_evaluation/$', 'ollinvfx.views.upload_evaluation', name='upload_evaluation'),
    url(r'^upload_entitytype/$', 'ollinvfx.views.upload_entitytype', name='upload_entitytype'),
    url(r'^upload_comment/$', 'ollinvfx.views.upload_comment', name='upload_comment'),
    url(r'^upload_alarm/$', 'ollinvfx.views.upload_alarm', name='upload_alarm'),
    url(r'^upload_alarmreminder/$', 'ollinvfx.views.upload_alarmreminder', name='upload_alarmreminder'),
    url(r'^upload_alarmactionparameter/$', 'ollinvfx.views.upload_alarmactionparameter', name='upload_alarmactionparameter'),
    url(r'^upload_commands/$', 'ollinvfx.views.upload_commands', name='upload_commands'),
    url(r'^upload_priviledgesmatrix/$', 'ollinvfx.views.upload_priviledgesmatrix', name='upload_priviledgesmatrix'),
    url(r'^upload_commandrelations/$', 'ollinvfx.views.upload_commandrelations', name='upload_commandrelations'),
    url(r'^upload_extendedpermissions/$', 'ollinvfx.views.upload_extendedpermissions', name='upload_extendedpermissions'),
    url(r'^upload_notification/$', 'ollinvfx.views.upload_notification', name='upload_notification'),
    url(r'^upload_notificationmetadata/$', 'ollinvfx.views.upload_notificationmetadata', name='upload_notificationmetadata'),
    url(r'^upload_project/$', 'ollinvfx.views.upload_project', name='upload_project'),
    url(r'^upload_milestone/$', 'ollinvfx.views.upload_milestone', name='upload_milestone'),
    url(r'^upload_incomingfile/$', 'ollinvfx.views.upload_incomingfile', name='upload_incomingfile'),
    url(r'^upload_projectuser/$', 'ollinvfx.views.upload_projectuser', name='upload_projectuser'),
    url(r'^upload_playlist/$', 'ollinvfx.views.upload_playlist', name='upload_playlist'),
    url(r'^upload_rateset/$', 'ollinvfx.views.upload_rateset', name='upload_rateset'),
    url(r'^upload_harddiskstatus/$', 'ollinvfx.views.upload_harddiskstatus', name='upload_harddiskstatus'),
    url(r'^upload_harddiskregister/$', 'ollinvfx.views.upload_harddiskregister', name='upload_harddiskregister'),
    url(r'^upload_uploadcontrol/$', 'ollinvfx.views.upload_uploadcontrol', name='upload_uploadcontrol'),
    url(r'^upload_storageuse/$', 'ollinvfx.views.upload_storageuse', name='upload_storageuse'),
    url(r'^upload_servicetype/$', 'ollinvfx.views.upload_servicetype', name='upload_servicetype'),
    url(r'^upload_service/$', 'ollinvfx.views.upload_service', name='upload_service'),
    url(r'^upload_servicehistogramcolor/$', 'ollinvfx.views.upload_servicehistogramcolor', name='upload_servicehistogramcolor'),
    url(r'^upload_projectservice/$', 'ollinvfx.views.upload_projectservice', name='upload_projectservice'),
    url(r'^upload_projecttaskservice/$', 'ollinvfx.views.upload_projecttaskservice', name='upload_projecttaskservice'),
    url(r'^upload_assettype/$', 'ollinvfx.views.upload_assettype', name='upload_assettype'),
    url(r'^upload_sequencialidgenerator/$', 'ollinvfx.views.upload_sequencialidgenerator', name='upload_sequencialidgenerator'),
    url(r'^upload_sequence/$', 'ollinvfx.views.upload_sequence', name='upload_sequence'),
    url(r'^upload_shot/$', 'ollinvfx.views.upload_shot', name='upload_shot'),
    url(r'^upload_bid/$', 'ollinvfx.views.upload_bid', name='upload_bid'),
    url(r'^upload_assets/$', 'ollinvfx.views.upload_assets', name='upload_assets'),
    url(r'^upload_transfer/$', 'ollinvfx.views.upload_transfer', name='upload_transfer'),
    url(r'^upload_assetpriviledges/$', 'ollinvfx.views.upload_assetpriviledges', name='upload_assetpriviledges'),
    url(r'^upload_deletedassets/$', 'ollinvfx.views.upload_deletedassets', name='upload_deletedassets'),
    url(r'^upload_downloadcontrols/$', 'ollinvfx.views.upload_downloadcontrols', name='upload_downloadcontrols'),
    url(r'^upload_shotsservice/$', 'ollinvfx.views.upload_shotsservice', name='upload_shotsservice'),
    url(r'^upload_shotsassets/$', 'ollinvfx.views.upload_shotsassets', name='upload_shotsassets'),
    url(r'^upload_shotstatuslog/$', 'ollinvfx.views.upload_shotstatuslog', name='upload_shotstatuslog'),
    url(r'^upload_shotdelivery/$', 'ollinvfx.views.upload_shotdelivery', name='upload_shotdelivery'),
    url(r'^upload_shotgroup/$', 'ollinvfx.views.upload_shotgroup', name='upload_shotgroup'),
    url(r'^upload_shotgroupshotid/$', 'ollinvfx.views.upload_shotgroupshotid', name='upload_shotgroupshotid'),
    url(r'^upload_shotgrouptentpole/$', 'ollinvfx.views.upload_shotgrouptentpole', name='upload_shotgrouptentpole'),
    url(r'^upload_shotuser/$', 'ollinvfx.views.upload_shotuser', name='upload_shotuser'),
    url(r'^upload_selectionset/$', 'ollinvfx.views.upload_selectionset', name='upload_selectionset'),
    url(r'^upload_shotselectionset/$', 'ollinvfx.views.upload_shotselectionset', name='upload_shotselectionset'),
    url(r'^upload_customshotfield/$', 'ollinvfx.views.upload_customshotfield', name='upload_customshotfield'),
    url(r'^upload_shotcustomshotfield/$', 'ollinvfx.views.upload_shotcustomshotfield', name='upload_shotcustomshotfield'),
    url(r'^upload_version/$', 'ollinvfx.views.upload_version', name='upload_version'),
    url(r'^upload_all/$', 'ollinvfx.views.upload_all', name='upload_all'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)