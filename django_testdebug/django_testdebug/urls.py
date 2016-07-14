from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_testdebug.views.home', name='home'),
    # url(r'^django_testdebug/', include('django_testdebug.foo.urls')),

    # There URL's verify the authenticity of a user who wishes to login
    url(r'^accounts/login_user/$', 'ollinvfx_testdebug.views.login_user', name='login_user'),
    url(r'^accounts/auth/$', 'ollinvfx_testdebug.views.auth_view', name='auth_view'),
    url(r'^accounts/logout_user/$', 'ollinvfx_testdebug.views.logout_user', name='logout_user'),
    url(r'^accounts/loggedin/$', 'ollinvfx_testdebug.views.loggedin', name='loggedin'),
    url(r'^accounts/invalid/$', 'ollinvfx_testdebug.views.invalid_login', name='invalid_login'),

    #Shot options
    url(r'^shot_options/$', 'ollinvfx_testdebug.views.shot_options', name='shot_options'),

    url(r'^shot_options/update_shot/$', 'ollinvfx_testdebug.views.update_shot', name='update_shot'),
    url(r'^shot_options/updateshotgeneral/$', 'ollinvfx_testdebug.views.updateshotgeneral', name='updateshotgeneral'),

    url(r'^shot_options/remove_shot/$', 'ollinvfx_testdebug.views.remove_shot', name='remove_shot'),
    url(r'^shot_options/delete_shot/$', 'ollinvfx_testdebug.views.delete_shot', name='delete_shot'),

    url(r'^shot_options/new_shot/$', 'ollinvfx_testdebug.views.new_shot', name='new_shot'),
    url(r'^shot_options/add_shot/$', 'ollinvfx_testdebug.views.add_shot', name='add_shot'),

    url(r'^shot_options/find_matches/$', 'ollinvfx_testdebug.views.find_matches', name='find_matches'),
    url(r'^shot_options/search_matches/$', 'ollinvfx_testdebug.views.search_matches', name='search_matches'),

    url(r'^shot_options/main_image_assign_shot/$', 'ollinvfx_testdebug.views.main_image_assign_shot', name='main_image_assign_shot'),
    url(r'^shot_options/assign_Image_To_shot/$', 'ollinvfx_testdebug.views.assign_Image_To_shot', name='assign_Image_To_shot'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )