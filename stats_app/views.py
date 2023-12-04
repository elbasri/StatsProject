# stats_app/views.py
import os
import pandas as pd
import matplotlib.pyplot as plt

from django.shortcuts import render, redirect
from .models import UploadedFile, Result, Statsprj
from .forms import UploadFileForm
from django.core.files.storage import default_storage
from io import StringIO
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
import mpld3, random
from .algorithmes import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ResultListCreateView(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    
class ApplyAlgorithm(APIView):
    def post(self, request, *args, **kwargs):
        selected_columns = request.data.get('selectedColumns', [])
        selected_algorithm = request.data.get('selectedAlgorithm', '')
        result_data = request.data.get('resultData', [])
        
        return Response(result_data, status=status.HTTP_200_OK)

class UploadedFileListCreate(generics.ListCreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # Parse the CSV file and store data in the database
        if instance.file.name.endswith('.csv'):
            df = pd.read_csv(instance.file.path)
        elif instance.file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(instance.file.path)
        else:
            # Handle other file types or raise an exception if needed
            raise ValueError('Unsupported file format')

        # ... (perform other data processing as needed)

        # Update the serializer with additional fields if necessary
        serializer.instance = instance
        parsed_data = {
            'columns': df.columns.tolist(),
            'rows': df.values.tolist(),
        }
        serializer.validated_data['parsed_data'] = parsed_data

        instance.save()
        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class ResultListCreate(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

@api_view(['GET'])
def get_statistics(request):
    total_files = UploadedFile.objects.count()
    total_results = Result.objects.count()
    graph_results = Result.objects.exclude(graph='').count()

    # Add more statistics as needed

    data = {
        'total_files': total_files,
        'total_results': total_results,
        'graph_results': graph_results,
    }

    return Response(data)

def process_data(file_path, type):
    df = pd.read_csv(file_path)
    # Effectuez des opérations statistiques.
    # Votre représentation graphique en utilisant Matplotlib.
    #Date,Produit,Quantité,Prix,Client 
    
    graphName = random.randint(1,9999)
    #plt.savefig('stats_app/static/graph.png')
    html_file_path = "graphs/"+str(graphName)+"output.html"



    # Capturez la sortie de df.info() sous forme de chaîne de caractères.
    if(type == "topProd"):
        df["Chiffre_Affaire"] = df["Quantité"] * df["Prix"]
        Chiffre = df.groupby('Produit')["Chiffre_Affaire"].sum()
        ChiffreTotale = df["Chiffre_Affaire"].sum()

        print("Chiffre d'affaire: {}".format(Chiffre))
        print("Chiffre d'affaire Total: {}".format(ChiffreTotale))
        ProcResultat = Chiffre.nlargest(10)

        # Create a Matplotlib figure
        fig, ax = plt.subplots()
        plt.plot(df['Produit'], df['Prix'])
        # Save the figure as an HTML file using mpld3
        mpld3.save_html(fig, html_file_path)
    elif(type == "mounthlyRev"):
        
        df["Chiffre_Affaire"] = df["Quantité"] * df["Prix"]
        Chiffre = df.groupby('Produit')["Chiffre_Affaire"].sum()
        ChiffreTotale = df["Chiffre_Affaire"].sum()

        #4
        df['Date'] = pd.to_datetime(df['Date'])
        df['Mois'] = df['Date'].dt.strftime('%Y-%m')
        monthly_revenue = df.groupby('Mois')['Chiffre_Affaire'].sum()
        ProcResultat = pd.DataFrame({'Mois': monthly_revenue.index, 'Chiffre d\'affaires total': monthly_revenue.values})

        # Create a Matplotlib figure
        fig, ax = plt.subplots()
        plt.plot(df['Mois'], df['Chiffre_Affaire'])
        # Save the figure as an HTML file using mpld3
        mpld3.save_html(fig, html_file_path)
    elif(type == "GradientDescent"):
        df.columns = ['x0','x1','y']
        alpha, t0, t1, nbrIteration, m = 0.0002, 1, 2, 200, 50
        mse_list = gradientD(df, alpha, t0, t1, nbrIteration, m)
        fig, ax = plt.subplots()
        plt.plot(np.arange(nbrIteration),mse_list)
        mpld3.save_html(fig, html_file_path)

    elif(type == "NormalizeMinMax"):
        df.drop('Address', axis=1, inplace=True)
        ProcResultat = pd.DataFrame()
        ProcResultat = df.apply(minmax)
        fig, axes = plt.subplots(nrows=1, ncols=len(ProcResultat.columns)-1, figsize=(15, 5))
        for i, column in enumerate(ProcResultat.columns):
            if column != 'Price':
                axes[i].scatter(ProcResultat['Price'], ProcResultat[column], label=column)
                axes[i].set_title(column)
                axes[i].set_xlabel('Price')
                axes[i].set_ylabel(column)
                axes[i].legend()

        plt.tight_layout()
        mpld3.save_html(fig, html_file_path)
        
    elif(type == "GradientDescentN"):
        df.drop('Address', axis=1, inplace=True)
        dataframeRes = pd.DataFrame()
        dataframeRes = df.apply(minmax)
        dataframeRes["x0"] = 1
        alpha, t0, t1, nbrIteration, m = 0.0002, 1, 2, 10000, 50
        ProcResultat = gradientD(dataframeRes, alpha, t0, t1, nbrIteration, m, "x0", "Avg. Area Income", "Price")

        fig, ax = plt.subplots()
        plt.plot(np.arange(nbrIteration),ProcResultat)
        plt.tight_layout()
        mpld3.save_html(fig, html_file_path)
        
    elif(type == "MseN"):
        df.drop('Address', axis=1, inplace=True)
        dataframeRes = pd.DataFrame()
        dataframeRes = df.apply(minmax)
        dataframeRes["x0"] = 1
        alpha, t0, t1, nbrIteration, m = 0.0002, 1, 2, 200, 50
        ProcResultat = MSE(dataframeRes, t0, t1, m, "Avg. Area Income", "Price")

        fig, ax = plt.subplots()
        plt.plot(np.arange(nbrIteration),ProcResultat)
        plt.tight_layout()
        mpld3.save_html(fig, html_file_path)

    elif(type == "visualiser"):
        fig = visualiserCol(df, "Prix", "histograme")
        ProcResultat = ".."
        mpld3.save_html(fig, html_file_path)
        
    else:
        info_buffer = StringIO()
        df.info(buf=info_buffer, verbose=True, show_counts=True)
        ProcResultat = info_buffer.getvalue()

        # Create a Matplotlib figure
        fig, ax = plt.subplots()
        plt.plot(df[type], df['Prix'])
        # Save the figure as an HTML file using mpld3
        mpld3.save_html(fig, html_file_path)

    return [ProcResultat, html_file_path]

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            selected_options = request.POST.getlist('algorithme')
            first_selected_value = selected_options[0] if selected_options else None

            instance = UploadedFile(file=uploaded_file)
            instance.save()
            
            uploaded_file_instance = UploadedFile.objects.create(file=uploaded_file)
            uploaded_file_id = uploaded_file_instance.id

            # Enregistrez le fichier téléchargé dans le stockage par défaut.
            file_path = default_storage.save(uploaded_file.name, uploaded_file)

            # Obtenez le chemin du fichier en utilisant default_storage.path()
            file_path = default_storage.path(file_path)

            # Traitez le fichier et obtenez les informations du DataFrame.
            result_text = process_data(file_path, first_selected_value)
            #result_text = process_data(file_path, "topProd")
            #result_text = process_data(file_path, "mounthlyRev")

            # Enregistrez le résultat dans la base de données.
            instance = Result.objects.create(
                uploaded_file_id=uploaded_file_id,
                result_text=result_text[0],
                graph=result_text[1]
            )
            instance.save()

            return redirect('result_view', result_id=instance.id)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def result_view(request, result_id):
    try:
        result = Result.objects.get(id=result_id)
        uploaded_file = get_object_or_404(UploadedFile, id=result.uploaded_file_id)

        html_file_path = result.graph
        # Check if the file exists
        if os.path.exists(html_file_path):
            # Read the content of the HTML file
            with open(html_file_path, 'r') as html_file:
                html_content = html_file.read()
        else:
            html_content = "No Graph"
        
    except Result.DoesNotExist:
        raise Http404("Result does not exist")
    except UploadedFile.DoesNotExist:
        raise Http404("Uploaded file does not exist")

    return render(request, 'result.html', {'result': result, 'uploaded_file': uploaded_file, 'html_content': html_content})


def home(request):
    # Obtenez des statistiques (personnalisez selon vos besoins)
    total_files = UploadedFile.objects.count()
    total_results = Result.objects.count()

    context = {
        'total_files': total_files,
        'total_results': total_results,
    }

    return render(request, 'home.html', context)