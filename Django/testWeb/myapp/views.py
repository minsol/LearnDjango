from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import datetime

from .models import Question,Choice

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('myapp/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'myapp/index.html', context)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now 
    return HttpResponse(html)

# def current_datetime(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
    
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'myapp/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/detail.html', {'question': question})



# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('myapp:results', args=(question.id,)))


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/results.html', {'question': question})


##### 我们将删除旧的 index, detail, 和 results 视图，并用 Django 的通用视图代替。
class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

        
class DetailView(generic.DetailView):
    model = Question
    template_name = 'myapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'myapp/results.html'