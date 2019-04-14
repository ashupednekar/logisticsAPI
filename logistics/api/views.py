from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from keras.models import model_from_yaml
from .models import Features
from .serializers import FeatureSerializer
import time


class FeatureView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        features = FeatureSerializer(data=request.data, required=False)
        first = time.time()
        if features.is_valid():
            attr = list()
            for k, v in features.data.items():
                attr.append([v])
            print(attr)
            #l = list()
            #l.append(attr)
            #for i in range(27):
            #    l.append([])
            #load YAML and create model
            yaml_file = open('api/model.yaml', 'r')
            loaded_model_yaml = yaml_file.read()
            yaml_file.close()
            loaded_model = model_from_yaml(loaded_model_yaml)
            # load weights into new model
            loaded_model.load_weights("api/model.h5")
            print("Loaded model from disk")
            import numpy as np
            X = np.asarray(attr)
            sh = X.shape
            # evaluate loaded model on test data
            loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
            #if (X.ndim == 1):
             #   X = np.array([X])
            print(X)
            print(X.T)
            y = loaded_model.predict(X.T)
            #print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))
            print(time.time() - first)
            return Response(y, status=status.HTTP_201_CREATED)
        else:
            return Response(features.errors, status=status.HTTP_400_BAD_REQUEST)
