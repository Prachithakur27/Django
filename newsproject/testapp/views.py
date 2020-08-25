from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def movie_news_view(request):
    news1 = 'In telgu devdas movie is not good'
    news2 = 'salman updating minimum 100cr for his movies'
    news3 = 'hindi movies are best'
    news4 = 'he is my fev actor'

    my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4}
    return render(request,'testapp/mnews.html',my_dict)
