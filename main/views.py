from django.shortcuts import render
from django.http import HttpResponse
from .form import Form
from .text_summarization import TextSummarization
import re
# Create your views here.

def homepage(request):
	text = 'No search query'

	if request.method == 'POST':
		form = Form(request.POST)

		if form.is_valid():
			text = form.cleaned_data.get('text')
			summarize = TextSummarization(text)
			result = summarize.Summarize()
			# result = re.sub('[^\w\s]','',result)
			# result = re.sub('[\d]','',result)
			return render(request, 'main/home.html', {'result':result})

	return render(request, 'main/home.html')