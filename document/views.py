from django.shortcuts import render
from document.forms import DocumentForm
from django.shortcuts import render, redirect



def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = DocumentForm()
    return render(request, 'document/upload_document.html', {
        'form': form
    })

