from django.urls import path

from produtos.views import (index,ola,
    CreateCategoryView,
    ListCategoryView,
    DetailCategoryView,
    UpdateCategoryView,
    DeleteCategoryView,
)
urlpatterns = [
    path('',index,name="index"),
    path('ola',ola,name="ola"),
    path('categoria/add',
            CreateCategoryView.as_view(),
            name='create_category'
        ),
    path('categoria',
            ListCategoryView.as_view(),
            name='list_category'
        ),
    path('categoria/<int:pk>',
         DetailCategoryView.as_view(),
         name='category_detail'
        ),
    path('categoria/<int:pk>/update',
         UpdateCategoryView.as_view(),
         name='category_update'
        ),
    path('categoria/<int:pk>/delete',
         DeleteCategoryView.as_view(),
         name='category_delete'
        ),

]