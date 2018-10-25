from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm,ProfileForm,SeekForm,HelpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Profile,Seek,Help
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            profile=Profile(user=user)
            profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Confirm your account registration.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('<h1>Please confirm your email address to complete the registration</h1>')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        
        return HttpResponse('<h2>Thank you for your email confirmation. To login to your account, <a href="/accounts/login">Go this way .</a></h2>')
    else:
        return HttpResponse('<h1>Activation link is invalid!</h1>')


def profile(request):
    profile = Profile.objects.filter(user=request.user)
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form =ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if image_form.is_valid:
            image_form.save()
        else:
            image_form = ProfileForm()
            return render(request, 'profile.html', {"image_form": image_form})
    return render(request, 'profile.html', {"image_form": image_form})


def profiles(request,id):
    profile = Profile.objects.get(user_id=id)
    # seek=Seek.objects.filter(user_id=id)
   
                       
    return render(request,'profiles.html',{"profile":profile})

def seek(request):
    users = Profile.objects.all()
    seek = Seek.objects.all()
    # neighbourhood = request.user.profile.neighbourhood
    if request.method == 'POST':
        post_form = SeekForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            # post.neighbourhood = neighbourhood
            post.save()
            
        return redirect('/')

    else:
        post_form = SeekForm()
    return render(request, 'seek.html', {"post_form": post_form,"seek":seek,"users":users })

def helpout(request):
    posts = Seek.objects.all()
    # seek = request.user.profile.seek
    if request.method == 'POST':
        help_form = HelpForm(request.POST, request.FILES)
        if help_form.is_valid():
            post = help_form.save(commit=False)
            post.user = request.user
            post.seek = seek
            post.save()
            
        return redirect('/')

    else:
        help_form = HelpForm()
    return render(request, 'help.html', {"help_form": help_form,"posts":posts })
