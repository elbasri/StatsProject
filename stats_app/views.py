# stats_app/views.py
import os
import pandas as pd
import matplotlib.pyplot as plt

from django.shortcuts import render, redirect
from .models import UploadedFile, Result
from .forms import UploadFileForm
from django.core.files.storage import default_storage
from io import StringIO
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

def process_data(file_path):
    df = pd.read_csv(file_path)
    # Effectuez des opérations statistiques.

    # Votre représentation graphique en utilisant Matplotlib.
    #Date,Produit,Quantité,Prix,Client
    plt.plot(df['Produit'], df['Prix'])
    plt.savefig('stats_app/static/graph.png')


    # Capturez la sortie de df.info() sous forme de chaîne de caractères.
    info_buffer = StringIO()
    df.info(buf=info_buffer)
    info_string = info_buffer.getvalue()

    return info_string

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            instance = UploadedFile(file=uploaded_file)
            instance.save()
            
            uploaded_file_instance = UploadedFile.objects.create(file=uploaded_file)
            uploaded_file_id = uploaded_file_instance.id

            # Enregistrez le fichier téléchargé dans le stockage par défaut.
            file_path = default_storage.save(uploaded_file.name, uploaded_file)

            # Obtenez le chemin du fichier en utilisant default_storage.path()
            file_path = default_storage.path(file_path)

            # Traitez le fichier et obtenez les informations du DataFrame.
            result_text = process_data(file_path)

            # Enregistrez le résultat dans la base de données.
            instance = Result.objects.create(
                uploaded_file_id=uploaded_file_id,
                result_text=result_text
            )
            instance.save()

            return redirect('result', pk=instance.pk)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def result_view(request, result_id):
    try:
        result = Result.objects.get(id=result_id)
        df_info = result.result_text
        df_info_html = pd.DataFrame()._info_repr_html()

        uploaded_file = get_object_or_404(UploadedFile, id=result.uploaded_file_id)
    except Result.DoesNotExist:
        raise Http404("Result does not exist")
    except UploadedFile.DoesNotExist:
        raise Http404("Uploaded file does not exist")

    return render(request, 'result.html', {'result': result, 'uploaded_file': uploaded_file, 'df_info': df_info})


def home(request):
    # Obtenez des statistiques (personnalisez selon vos besoins)
    total_files = UploadedFile.objects.count()
    total_results = Result.objects.count()

    context = {
        'total_files': total_files,
        'total_results': total_results,
    }

    return render(request, 'home.html', context)