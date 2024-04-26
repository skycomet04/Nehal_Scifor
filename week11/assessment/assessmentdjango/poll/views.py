from django.shortcuts import render ,HttpResponse,redirect
from .models import Poll
from .forms import PollForm

# Create your views here.
def home(request):
    poll_list=Poll.objects.all()
    context={'p_list':poll_list}
    return render(request,'home.html',context)

def createpoll(request):
    if request.method =="POST":
        form=PollForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('home')
    else:
        form=PollForm()
    return render(request,'createpoll.html',{'form':form})

def result(request,pid):
    poll_result=Poll.objects.get(id=pid)
    total=0
    total=poll_result.one_vote + poll_result.two_vote
    context={'poll':poll_result,'total_vote':total}
    return render(request, 'result.html',context)

def vote(request,pid):
    poll_vote=Poll.objects.get(id=pid)
    if request.method =="POST":
        poll=request.POST.get('pollopt')
        print(poll)
        if poll=="option_one":
            poll_vote.one_vote+=1
        elif poll=="option_two":
            poll_vote.two_vote+=1
        poll_vote.save()
        return redirect('result',poll_vote.id)
    context={'polls':poll_vote}
    return render(request,'vote.html',context)
