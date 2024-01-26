from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard),
    path('add_pro/', views.insert_pro),
    path('insert_pro/',views.insert_pro),
    path('table_pro/',views.table_pro),
    path('update/<int:id>',views.update),
    path('edit_pro/<int:id>', views.edit_pro),
    path('destroy/<int:id>', views.destroy),
    path('admin_login/',views.admin_login)
]
