import csv
from django.shortcuts import render, redirect
from .models import EnergyData
from .forms import CSVUploadForm
from django.core.paginator import Paginator
from django.db.models import Sum
import json
import os

def import_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(decoded_file)
            for row in csv_reader:
                EnergyData.objects.create(
                    date=row['date'],
                    region=row['region'],
                    consumption_twh=row['consumption_twh']
                )
            return redirect('data_list')
    else:
        csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'energy_data.csv')
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                EnergyData.objects.create(
                    date=row['date'],
                    region=row['region'],
                    consumption_twh=row['consumption_twh']
                )
        return redirect('data_list')

    form = CSVUploadForm()
    return render(request, 'energy/import_csv.html', {'form': form})

def data_list(request):
    data = EnergyData.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'energy/data_list.html', {'page_obj': page_obj})

def visualize_data(request):
    region_data = EnergyData.objects.values('region').annotate(total_consumption=Sum('consumption_twh'))
    region_labels = [item['region'] for item in region_data]
    region_values = [item['total_consumption'] for item in region_data]

    france_data = EnergyData.objects.filter(region='France').values('date__year').annotate(total_consumption=Sum('consumption_twh'))
    france_labels = [item['date__year'] for item in france_data]
    france_values = [item['total_consumption'] for item in france_data]

    context = {
        'region_labels': json.dumps(region_labels),
        'region_values': json.dumps(region_values),
        'france_labels': json.dumps(france_labels),
        'france_values': json.dumps(france_values),
    }
    return render(request, 'energy/visualize_data.html', context)
