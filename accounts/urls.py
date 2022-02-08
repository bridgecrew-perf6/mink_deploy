from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('find_username/', views.find_username, name='find_username'),
    path('login/kakao/', views.kakao_login, name="kakao_login"),
    path('login/kakao/callback/', views.kakao_login_callback, name="kakao_login_callback"),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('accounts:password_reset_done'),
        template_name='accounts/password_reset/reset_password.html',
        email_template_name='accounts/password_reset/password_reset_form.html',
    ), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset/password_reset_confirm.html', success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset/password_reset_done.html'), name='password_reset_complete'),
]
