from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from .views import AboutPageView, ContactPageView


urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
   # path('about/', AboutPageView.as_view(), name='about'),
   # path('contact/', ContactPageView.as_view(), name='contact'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', login_required(views.add_to_cart), name='add-to-cart'),
    path('cart/', login_required(views.show_cart), name='showcart'),

    path('pluscart/', login_required(views.plus_cart)),
    path('minuscart/', login_required(views.minus_cart)),
    path('removecart/', login_required(views.remove_cart)),

    path('buy', login_required(views.buy_now), name='buy-now'),
    #path('checkout/', login_required(views.buy_now), name='checkout'),
    path('profile/', login_required(views.ProfileView.as_view()), name='profile'),
    path('address/', login_required(views.address), name='address'),
    path('orders/', login_required(views.orders), name='orders'),

    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),

    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path('checkout/', login_required(views.checkout), name='checkout'),
    #path('paymentdone/', login_required(views.payment_done), name='paymentdone'),
    path('paymentdone/', login_required(views.payment_done), name='paymentdone'),
    path('search/', views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
