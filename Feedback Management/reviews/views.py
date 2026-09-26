# # from django.shortcuts import render

# # # Create your views here.


# # def dashboard(request):
# #     return render(request, 'dashboard.html')



# from django.shortcuts import render


# def dashboard(request):
#     return render(request, 'dashboard.html')






from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/login/')
def dashboard(request):

    search = request.GET.get('search', '')
    sentiment = request.GET.get('sentiment', '')
    channel = request.GET.get('channel', '')
    status = request.GET.get('status', '')

    feedbacks = Feedback.objects.all()

    # Search filter
    if search:
        feedbacks = feedbacks.filter(
            content__icontains=search
        )

    # Sentiment filter
    if sentiment:
        feedbacks = feedbacks.filter(
            sentiment=sentiment
        )

    # Channel filter
    if channel:
        feedbacks = feedbacks.filter(
            channel=channel
        )

    # Status filter
    if status:
        feedbacks = feedbacks.filter(
            status=status
        )

        # Pagination

    # paginator = Paginator(feedbacks, 10)

    # page_number = request.GET.get('page')

    # feedbacks = paginator.get_page(page_number)

    total_feedbacks = feedbacks.count()

    positive_count = feedbacks.filter(
        sentiment='POS'
    ).count()

    neutral_count = feedbacks.filter(
        sentiment='NEU'
    ).count()

    negative_count = feedbacks.filter(
        sentiment='NEG'
    ).count()




    # Pagination
    # paginator = Paginator(feedbacks, 10)

    # page_number = request.GET.get('page')

    # feedbacks = paginator.get_page(page_number)


        # Sentiment percentages

    positive_percentage = (
        (positive_count / total_feedbacks) * 100
        if total_feedbacks > 0 else 0
    )

    neutral_percentage = (
        (neutral_count / total_feedbacks) * 100
        if total_feedbacks > 0 else 0
    )

    negative_percentage = (
        (negative_count / total_feedbacks) * 100
        if total_feedbacks > 0 else 0
    )

        # Channel-wise feedback count

    website_count = feedbacks.filter(
        channel='Website'
    ).count()

    email_count = feedbacks.filter(
        channel='Email'
    ).count()

    social_count = feedbacks.filter(
        channel='Social Media'
    ).count()


    # Status-wise feedback count

    new_count = feedbacks.filter(
        status='NEW'
    ).count()

    reviewed_count = feedbacks.filter(
        status='REVIEWED'
    ).count()

    actioned_count = feedbacks.filter(
        status='ACTIONED'
    ).count()


    # Pagination - MUST BE LAST

    paginator = Paginator(feedbacks, 10)

    page_number = request.GET.get('page')

    feedbacks = paginator.get_page(page_number)

    context = {
        'feedbacks': feedbacks,
        'total_feedbacks': total_feedbacks,
        'positive_count': positive_count,
        'neutral_count': neutral_count,
        'negative_count': negative_count,



        'positive_percentage': round(positive_percentage, 1),
        'neutral_percentage': round(neutral_percentage, 1),
        'negative_percentage': round(negative_percentage, 1),



        'website_count': website_count,
        'email_count': email_count,
        'social_count': social_count,


        'new_count': new_count,
        'reviewed_count': reviewed_count,
        'actioned_count': actioned_count,

    }


    return render(
        request,
        'dashboard.html',
        context
    )




@login_required(login_url='/login/')
def add_feedback(request):

    if request.method == 'POST':

        content = request.POST.get('content', '').strip()
        channel = request.POST.get('channel', '').strip()
        sentiment = request.POST.get('sentiment', '').strip()
        status = request.POST.get('status', '').strip()

        # Backend validation
        if not content:
            return render(
                request,
                'add_feedback.html',
                {'error': 'Feedback content cannot be empty.'}
            )

        if not channel:
            return render(
                request,
                'add_feedback.html',
                {'error': 'Please select a channel.'}
            )

        if sentiment not in ['POS', 'NEU', 'NEG']:
            return render(
                request,
                'add_feedback.html',
                {'error': 'Invalid sentiment selected.'}
            )

        if status not in ['NEW', 'REVIEWED', 'ACTIONED']:
            return render(
                request,
                'add_feedback.html',
                {'error': 'Invalid status selected.'}
            )

        Feedback.objects.create(
            content=content,
            channel=channel,
            sentiment=sentiment,
            status=status
        )


        messages.success(request, 'Feedback added successfully!')


        return redirect('/')

    return render(
        request,
        'add_feedback.html'
    )

@login_required(login_url='/login/')
def edit_feedback(request, id):

    feedback = get_object_or_404(
        Feedback,
        id=id
    )

    if request.method == 'POST':

        feedback.content = request.POST.get('content')
        feedback.channel = request.POST.get('channel')
        feedback.sentiment = request.POST.get('sentiment')
        feedback.status = request.POST.get('status')

        feedback.save()

        messages.success(request, 'Feedback updated successfully!')

        return redirect('/')

    return render(
        request,
        'edit_feedback.html',
        {'feedback': feedback}
    )





@login_required(login_url='/login/')
def delete_feedback(request, id):

    feedback = get_object_or_404(
        Feedback,
        id=id
    )

    if request.method == 'POST':

        feedback.delete()


        messages.success(request, 'Feedback deleted successfully!')


        return redirect('/')

    return render(
        request,
        'delete_feedback.html',
        {'feedback': feedback}
    )