"""Django app models serializers."""
from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """Serialize User model."""
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role']


class MessageSerializer(serializers.ModelSerializer):
    """Serialize Message model."""
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'message_body', 'sent_at', 'conversation', 'sender']


class ConversationSerializer(serializers.ModelSerializer):
    """Serialize Conversation model."""
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True) 
 
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'created_at', 'participants', 'messages']
