# -*- coding: utf-8 -*-
import logging

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import QiniuUploadToken
from .serializers import UploadTokenSerializer


logger = logging.getLogger('rcxue.upload.qiniu')


class QiniuImgTokenList(generics.CreateAPIView):
    serializer_class = UploadTokenSerializer
    # permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = UploadTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = QiniuUploadToken.objects.create_img_token(request=request, **serializer.data)
        data = UploadTokenSerializer(token).data

        return Response(data, status=status.HTTP_200_OK)


img_token_list_view = QiniuImgTokenList.as_view()
