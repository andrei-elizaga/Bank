from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.index_title = 'Admin'
admin.site.site_header = 'Bank'
admin.site.site_title = 'Bank'

urlpatterns = [

    # Core
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # API (v1)
    path('', include('v1.accounts.urls')),
    path('', include('v1.bank_transactions.urls')),
    path('', include('v1.banks.urls')),
    path('', include('v1.blocks.urls')),
    path('', include('v1.confirmation_blocks.urls')),
    path('', include('v1.connection_requests.urls')),
    path('', include('v1.invalid_blocks.urls')),
    path('', include('v1.self_configurations.urls')),
    path('', include('v1.validator_confirmation_services.urls')),
    path('', include('v1.validators.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
