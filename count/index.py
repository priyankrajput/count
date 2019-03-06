from django.http import HttpResponse
from django.shortcuts import render


def count(request):
    return render(request,'count.html')

def value(request):
    data = request.GET['text_area']
    word_list = data.split()
    length = len(word_list)

    word_dic = {}
    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1




    return render(request,'value.html',{'fulltext':data ,'length':length ,'word_dic':word_dic.items()})