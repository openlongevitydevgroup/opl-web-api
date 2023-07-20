from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from posts_comments.models.comments import Comment
from posts_comments.models.submissions import Submission
from posts_comments.serializers.comments_serializer import CommentsSerializer

# Get comment for a particular post submission
@api_view(["GET"])
def get_comments(request,id): 
    submission = Submission.objects.get(submission_id = id) #Check if submission exists.
    if submission: 
        comments = Comment.objects.filter(submission_id = id)
        serializer = CommentsSerializer(comments, many=True)
        if comments:
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# Get particular comment and its children
@api_view(["GET"])
def get_single_comment(request, id): 
    comment = Comment.objects.get(comment_id = id) #Check is comment exists 
    if comment: 
        serializer = CommentsSerializer(comment)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)

