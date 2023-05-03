from rest_framework.response import Response
from rest_framework.decorators import api_view

from entries.models import Entry
from entries.serializers import EntrySerializer

from django.http import HttpResponse


@api_view(['GET'])
def get_all_entries(request):
    """Endpoint to retreive all existing entries"""

    entries = Entry.objects.order_by('-date').all()
    serializers = EntrySerializer(entries, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def new_entry(request):
    """Endpoint to form new Entry"""

    # Get post data then check for empty fields
    post_data = request.data
    for data in post_data:
        if not post_data[data]:
            # Bad Request
            print(post_data)
            return HttpResponse(status=400, content='Cannot submit with empty fields.')

    new = Entry(location=post_data['location'],
                title=post_data['title'], content=post_data['content'])
    new.save()
    return HttpResponse(status=200, content='New Entry is created successfuly.')


@api_view(['POST'])
def delete_entry(request):
    """Endpoint to delete Entry"""

    entry_pk = request.data['entry-id']
    Entry.objects.filter(pk=entry_pk).delete()
    return HttpResponse(status=200, content='Entry has successfuly been deleted.')
