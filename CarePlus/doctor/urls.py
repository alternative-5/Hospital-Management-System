from django.urls import path
from doctor import views


urlpatterns = [
    path('doc/',views.doc, name='doc'),
    path('appoint_table/',views.appoint_table, name='appoint_table'),
    path('update_doc/<int:update_id>/',views.update_doc, name='update_doc'),
    path('doc_base/',views.doc_base, name='doc_base'),
    path('appoint_approve/<int:appoint_id>/',views.appoint_approve,name='appoint_approve'),
    path('doct_patient/',views.doct_patient, name='doct_patient')

    # path('delete_doc/<int:delete_id>/',views.delete_doc, name='delete_doc'),
]