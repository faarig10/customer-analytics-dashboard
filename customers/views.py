from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# View to get customer data
@api_view(['GET'])
def customer_data_view(request):
    data = Customer.objects.all().values()
    df = pd.DataFrame(data)
    return Response(df.to_dict(orient="records"))

# View to get customer segmentation
@api_view(['GET'])
def customer_segmentation_view(request):
    data = Customer.objects.all().values()
    df = pd.DataFrame(data)

    # Select relevant features and apply clustering
    features = df[['cost_of_the_product', 'prior_purchases', 'customer_rating', 'discount_offered']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['segment'] = kmeans.fit_predict(scaled_features)

    # Return clustered data
    return Response(df[['id', 'segment']].to_dict(orient="records"))
