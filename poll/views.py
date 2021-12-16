from django.http import HttpResponse
from django.shortcuts import render
from poll.models import Question

def index(request):
    # db에 있는 모든 데이터 조회하기(select)
    question_list = Question.objects.all()
    return render(request, 'poll/index.html', {'question_list':question_list})
    #return HttpResponse("Welcome~ 환영합니다!!")

def detail(request, question_id):
    # 해당 id(순번)로 자료 조회(select)
    question = Question.objects.get(id=question_id)
    return render(request, 'poll/detail.html', {'question':question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    #선택자료넘겨받음
    try:
        choice_id = request.POST['choice']
        sel_choice = question.choice_set.get(id=choice_id)
    except:
        return render(request, 'poll/detail.html',
                      {'question':question, 'error':'선택을 확인하세요.'})
    else:
        sel_choice.votes = sel_choice.votes + 1
        sel_choice.save()   #dbㅇㅔ 저장
        return render(request, 'poll/vote_result.html', {'question':question})
