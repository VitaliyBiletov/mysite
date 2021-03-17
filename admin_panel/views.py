from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import UserForm, PupilRegistrationForm, LogoGroupsForm, ProfileForm
from .models import Pupil, LogoGroups
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.
def index(request):
    print(request.user)
    return render(
        request,
        'admin_panel/index.html',
        {
            'title': 'Администратор'
        }
    )


@login_required
@transaction.atomic
def users(request):
    if request.user.is_staff:
        if request.method == "POST":
            user_form = UserForm(request.POST)
            print(user_form)
            profile_form = ProfileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                new_profile = profile_form.save(commit=False)
                new_profile.user = user
                new_profile.save()
                profile_form.save_m2m()
                return redirect('/admin_panel/users_registration/')
        else:
            user_form = UserForm()
            profile_form = ProfileForm()
            list_users = User.objects.all()
            print(list_users)
            return render(
                request,
                'admin_panel/users_registration.html',
                {
                    'list_users': list_users,
                    'user_form': user_form,
                    'profile_form': profile_form
                 }
        )
    else:
        return redirect('/')


def pupils(request):
    list_pupils = Pupil.objects.all().order_by('last_name')
    paginator = Paginator(list_pupils, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        list_pupils = paginator.page(page)
    except PageNotAnInteger:
        list_pupils = paginator.page(1)
    except EmptyPage:
        list_pupils = paginator.page(paginator.num_pages)

    if request.user.is_staff:
        if request.method == "POST":
            pupil_form = PupilRegistrationForm(request.POST)
            if pupil_form.is_valid():
                new_pupil = pupil_form.save(commit=False)
                new_pupil.save()
                new_pupil_form = PupilRegistrationForm()
                return render(
                    request,
                    'admin_panel/pupils_registration.html',
                    {
                        'new_pupil': new_pupil,
                        'pupil_registration_form': new_pupil_form,
                        'list_pupils': list_pupils,
                        'page_obj': page_obj
                    }
                )
        else:
            pupil_form = PupilRegistrationForm()
        return render(
            request,
            'admin_panel/pupils_registration.html',
            {
                'pupil_registration_form': pupil_form,
                'pupils': list_pupils,
                'list_pupils': list_pupils,
                'page_obj': page_obj
            }
        )
    else:
        return redirect('/')


def delete(request, id):
    # pupil = Pupil.objects.get(id=id)
    # pupil.delete()
    print(request.GET['type'])
    url = request.path
    url_parts = url.split('/')
    redirect_url = '/'.join(url_parts[0:3])
    return redirect(redirect_url)


def unpin(request, id):
    logo_group = LogoGroups.objects.get(id=id)
    logo_group.delete()
    teacher_id = request.GET.get('id_teacher')
    logo_groups_filtered = LogoGroups.objects.filter(teacher=teacher_id)
    return render(
        request,
        'admin_panel/result_table.html',
        {
            'logo_groups_filtered': logo_groups_filtered,
            'logo_groups_form': LogoGroupsForm(request.GET),
        }
    )


def groups(request):
    logo_group_form = LogoGroupsForm()
    return render(request, 'admin_panel/groups.html', {'logo_groups_form': logo_group_form})


def groups_view(request):
    if request.method == "POST":
        logo_group_form = LogoGroupsForm(request.POST)
        teacher_id = logo_group_form['teacher'].value()
        logo_groups_filtered = LogoGroups.objects.filter(teacher=teacher_id)
        return render(
            request,
            'admin_panel/result_table.html',
            {
                'logo_groups_form': LogoGroupsForm(request.POST),
                'logo_groups_filtered': logo_groups_filtered
            }
        )


def groups_attachment(request):
    if request.method == "POST":
        logo_group_form = LogoGroupsForm(request.POST)
        teacher_id = logo_group_form['teacher'].value()
        logo_groups_filtered = LogoGroups.objects.filter(teacher=teacher_id)
        if logo_group_form.is_valid():
            new_logo_group = logo_group_form.save(commit=False)
            new_logo_group.save()
            return render(
                request,
                'admin_panel/result_table.html',
                {
                    'logo_groups_filtered': logo_groups_filtered,
                }
            )