from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidateForm
from .models import Candidate
from django.conf import settings
from .utils import *

def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/candidate_list.html', {'candidates': candidates})

def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    return render(request, 'candidates/candidate_detail.html', {'candidate': candidate})

def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save(commit=False)

            # Encrypt sensitive fields using the public key
            candidate.adharnumber = encrypt_string_rsa(candidate.adharnumber)
            candidate.pannumber = encrypt_string_rsa(candidate.pannumber)
            candidate.passportnumber = encrypt_string_rsa(candidate.passportnumber)
            candidate.adharnumber = decrypt_string_rsa(candidate.adharnumber)
            candidate.pannumber = decrypt_string_rsa(candidate.pannumber)
            candidate.passportnumber = decrypt_string_rsa(candidate.passportnumber)            
            candidate.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'candidates/add_candidate.html', {'form': form})

def edit_candidate(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            candidate = form.save(commit=False)

            candidate.save()
            return redirect('candidate_detail', pk=pk)
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'candidates/edit_candidate.html', {'form': form, 'candidate': candidate})

def delete_candidate(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        candidate.delete()
        return redirect('candidate_list')
    return render(request, 'candidates/delete_candidate.html', {'candidate': candidate})

