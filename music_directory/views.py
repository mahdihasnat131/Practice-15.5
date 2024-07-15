from django.shortcuts import render
# from posts.models import Post
from musics.models import Music
from albums.models import Album

def home(request):
    # data = Post.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    #     print()
    # return render(request, 'home.html', {'data' : data})
    data1= Music.objects.all()
    
    data2=Album.objects.all()

    
    
    return render(request, 'home.html',{'data1':data1, 'data2':data2})