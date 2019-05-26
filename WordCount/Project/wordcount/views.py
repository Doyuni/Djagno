from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    fulltext = request.GET['fulltext'] # 입력 text 전체
    words = fulltext.split()
    words_count = { word : words.count(word) for word in words } # comprehension
    # 마지막 인자는 dict, items로 키, 값 가져와야 iteration 가능
    return render(request, 'result.html', {'full': fulltext, 'length': len(words), 'countList' : words_count.items()}) 