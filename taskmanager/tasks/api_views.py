from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Task

@require_GET
def task_list_by_status(request, status):
    """
    API endpoint to get tasks by status.
    """
    if status not in ['in_progress', 'completed', 'overdue']:
        return JsonResponse({'error': 'Invalid status'}, status=400)

    tasks = Task.objects.filter(status=status)
    tasks_list = list(tasks.values('id', 'title', 'status', 'priority', 'due_date'))
    return JsonResponse(tasks_list, safe=False)
