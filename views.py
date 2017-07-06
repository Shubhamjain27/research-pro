from django.contrib.auth import login, authenticate, get_user
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import Context, RequestContext
from .forms import SignUpForm, ProfileForm,ProfileForm2, InternForm, Cover
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Profile2, Friend, Applicant2
from django.contrib.auth import get_user_model
from django.views import generic

from student.exceptions import AlreadyExistsError

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('signup:home')

    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})
@login_required
def home(request):
    if request.method == 'POST':
        user = get_user(request)

        profile_form = ProfileForm(request.POST, request.FILES or None,instance=user.profile, )
        if profile_form.is_valid():
            profile_form.full_clean()
            profile_form.save()
            return redirect('signup:dashboard')

    else:
        profile_form = ProfileForm()
    context = {"form":  profile_form}
    return render(request, 'signup/profile.html', context)

@login_required
def dashboard(request):
    user = get_user(request)

    info = Profile.objects.filter(user=user)

    bookdata = {
        "detail": info
    }

    return render_to_response("signup/dashboard.html", bookdata, Context(request))


def signup_student(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('signup:home2')

    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})
@login_required
def home2(request):
    if request.method == 'POST':
        user = get_user(request)

        profile_form = ProfileForm2(request.POST,instance=user.profile2, )
        if profile_form.is_valid():
            profile_form.full_clean()
            profile_form.save()
            return redirect('signup:dashboard2')

    else:
        profile_form = ProfileForm2()
    context = {"form":  profile_form}
    return render(request, 'signup/profile2.html', context)

@login_required
def dashboard2(request):
    user = get_user(request)

    info = Profile2.objects.filter(user=user)

    bookdata = {
        "detail": info
    }

    return render_to_response("signup/dashboard2.html", bookdata, Context(request))


@login_required
def internview(request):
    if request.method == 'POST':
        user = get_user(request)
        form3 = InternForm(request.POST,instance=user.profile)
        if form3.is_valid():
            form3.full_clean()
            form3.save()
            return redirect('signup:dashboard')
    else:
        form3 = InternForm()
    context = {"form": form3}
    return render(request, 'signup/intern.html', context)


class Projects(generic.ListView):
    template_name = 'signup/projects.html'

    def get_queryset(self):
        return Profile.objects.exclude(skills_needed__isnull=True)


class ProjectsDetail(generic.DetailView):
    model = Profile
    template_name = 'signup/detail.html'

@login_required
def change_friends(request, pk):
    new_friend = User.objects.get(pk=pk)
    current_user = request.user
    if request.method == 'POST':
        cover_letter = Cover(request.POST)
        if cover_letter.is_valid():
            cover_letter.save()
            Friend.make_friend(current_user, new_friend, cover_letter)


            return redirect('signup:dashboard2')
    else:
        cover_letter = Cover()
    context = {"form": cover_letter}
    return render(request, 'signup/trial.html', context)


@login_required
def apply(request, pk):
    prof = User.objects.get(pk=pk)
    current_user = request.user
    if request.method == 'POST':
        cover_letter = Cover(request.POST)
        if cover_letter.is_valid():
            app = cover_letter.save(commit=False)
            app.user = current_user
            app.prof = prof
            app.save()
            return redirect('signup:dashboard2')
    else:
        cover_letter = Cover()
    context = {"form": cover_letter}
    return render(request, 'signup/trial.html', context)


@login_required
def profapplications(request):
    user = get_user(request)
    info = Applicant2.objects.filter(prof=user)
    bookdata = {
        "detail": info
    }

    return render_to_response("signup/dashboard2.html", bookdata, Context(request))


def profhome(request):
    return render(request, 'signup/profhome.html')


