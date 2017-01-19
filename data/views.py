# -*- coding:utf-8 -*-
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Record
from .serializers import (
    RecordSerializer,
    QuerySerializer,
)


class RecordList(generics.ListAPIView):
    serializer_class = RecordSerializer

    def get_queryset(self):
        ModelClass = self.serializer_class.Meta.model
        return ModelClass.objects.all()[:40]


def gap_calc(scheme, data, max_count=60):
    """根据开奖记录计算遗漏曲线

    开奖记录为倒叙, 第 0 条是最新开奖记录.

    连续两次出现, 遗漏为 0, 故差值需 -1
    """
    s = set(scheme)
    history = [idx for idx, item in enumerate(data)
               if s.issubset(item.win)]
    return [{
        'gap': i2-i1-1,
        'timestamp': data[i1].time,
        'win_str': data[i1].win_str,
    } for i1, i2 in zip(history[:-1], history[1:])]


@api_view(['GET'])
def gap(request):
    """遗漏查询

    关键词为 q, 支持一次查询多个 scheme

    e.g.: `/api/v1/gap?q=1+2+3+4+5&q=2+3`

    Response:

    - 400: bad request.
    - 200: data for gap curve
    """

    serializer = QuerySerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)

    schemes = serializer.validated_data.get('schemes')
    data = Record.objects.all()

    return Response(
        [{'scheme': s,
          'curve': gap_calc(s, data),
          } for s in schemes]
    )


record_list_views = RecordList.as_view()
