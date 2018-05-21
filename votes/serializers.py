from rest_framework import serializers
from .models import Vote

"""
http://www.django-rest-framework.org/api-guide/serializers/#modelserializer
"""

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id','subject', 'vote_taken', 'ayes', 'nays')
