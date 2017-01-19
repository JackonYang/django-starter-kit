# -*- coding:utf-8 -*-
from rest_framework import serializers

from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record


def validate_num(num, min_value=1, max_value=20):
    try:
        num = int(num)
    except ValueError:
        msg = u'号码只能是数字'
        raise serializers.ValidationError(msg)

    if num < min_value or num > max_value:
        msg = u'号码区间为: %s-%s' % (min_value, max_value)
        raise serializers.ValidationError(msg)
    return num


class QuerySerializer(serializers.Serializer):
    q = serializers.ListField(
        child=serializers.CharField()
    )

    def validate(self, data):
        max_length = 8
        q = data.get('q', [])
        schemes = []
        for q_str in q:
            query = map(validate_num, q_str.split())
            if len(query) > max_length:
                msg = u'最多选择 %s 个号码' % max_length
                raise serializers.ValidationError(msg)

            # ignore if query is empty
            if query:
                schemes.append(query)

        data['schemes'] = schemes
        return data
