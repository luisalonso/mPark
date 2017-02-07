from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response, render

from mParkCore.models import Patient, Professional, Session, Post, Comment
from mParkProfessional.forms import MyRegistrationForm, AddSession, PostForm, CommentForm

@login_required
def dashboard(request):
    patients = Patient.objects.all()
    return render(request, 'dashboard.html', {'patients': patients})


@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('mParkCore.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('mParkCore.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('mParkCore.views.post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('mParkCore.views.post_list')


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('mParkCore.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('mParkCore.views.post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('mParkCore.views.post_detail', pk=post_pk)


def session_edit(request):
    # handling errors and exceptions
    if request.method == 'POST':
        form = AddSession(request.POST)
        if form.is_valid():
            return render_to_response('dashboard.html')

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('dashboard.html', token)


def register(request):
    token = {}
    token.update(csrf(request))
    # When the user arrives in the page (not a POST) it loads MyRegistrationForm()
    # and shows register.html with the token

    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('registration/registration_complete.html')
        else:
            token['form'] = form
            return render_to_response('registration/register.html', token)
    else:
        form = MyRegistrationForm()

    token['form'] = form

    return render_to_response('registration/register.html', token)


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request,
                                  template_name='registration/password_reset_update_pass.html',
                                  uidb64=uidb64,
                                  token=token,
                                  post_reset_redirect=reverse('reset_complete'))


def reset(request):
    return password_reset(request,
                          template_name='registration/password_reset_request.html',
                          email_template_name='registration/password_reset_custom_email.html',
                          subject_template_name='registration/password_reset_subject.txt',
                          post_reset_redirect=reverse('reset_success'))


def reset_success(request):
    return render(request, 'registration/password_reset_success.html')


def reset_complete(request):
    return render(request, 'registration/password_reset_finish.html')


@login_required
def profile_detail(request, pk, pp):
    profile = get_object_or_404(Patient, pk=pk)
    user = get_object_or_404(Professional, id=pp)

    try:
        session = Session.objects.filter(patient=profile).latest('created_date')
    except:
        session = Session(patient=profile, professional=user, phase_I_duration=5, phase_II_duration=5,
                          phase_III_duration=5, phase_IV_duration=5, phase_V_duration=5, min_BPM=80, max_BPM=140)
        session.save()

    # check if this professional has access to the data of the patient
    return render(request, 'professional/profile.html', {'patient': profile, 'professional': user, 'session': session})

@login_required
def session_update(request):
    if request.method == 'POST':

        # POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            # Always use get on request.POST. Correct way of querying a QueryDict.
            pk = request.POST.get('pk')
            pp = request.POST.get('pp')
            t1 = request.POST.get('t1')
            t2 = request.POST.get('t2')
            t3 = request.POST.get('t3')
            t4 = request.POST.get('t4')
            t5 = request.POST.get('t5')
            max = request.POST.get('max')
            min = request.POST.get('min')

            print("Track 1 t1: " + t1)
            patient = get_object_or_404(Patient, pk=pk)
            professional = get_object_or_404(Professional, pk=pp)

            print("Track 2 t1: " + t1)
            session = Session(patient=patient, professional=professional, phase_I_duration=t1, phase_II_duration=t2,
                              phase_III_duration=t3, phase_IV_duration=t4, phase_V_duration=t5, min_BPM=min, max_BPM=max)
            session.save()

            print("Track 3 t1: " + t1)

            data = {"pk": pk, "pp": pp}
            # Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)
    # Get goes here
    return render(request, 'professional/profile.html')

@login_required
def explore_data(request):
    return render(request, 'professional/explore_data.html')

@login_required
def raw_data(request):
    return render(request, 'professional/raw_data.html')

def guide(request):
    return render(request, 'guide.html')