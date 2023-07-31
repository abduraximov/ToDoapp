from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.todo.models import Todo
from apps.api.todo.serializer import TodoSerializer


@api_view(["get", "post"])
def list_todo(request):
    if request.method == "GET":
        todos = Todo.objects.all().order_by("-created_at")
        serializer = TodoSerializer(instance=todos, many=True)
        return Response(serializer.data, status=200)
    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["get", "put", "delete"])
def detail_todo(request, slug):
    if request.method == "GET":
        todo = Todo.objects.get(slug=slug)
        serializer = TodoSerializer(instance=todo)
        return Response(serializer.data)

    elif request.method == "PUT":
        todo = Todo.objects.get(slug=slug)
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        todo = Todo.objects.get(slug=slug)
        todo.delete()
        return Response(data={
            "success": True,
            "message": "Todo successfully deleted. "
        })


@api_view(["get"])
def not_completed(request):
    if request.method == "GET":
        todos = Todo.objects.filter(completed=False)
        serializer = TodoSerializer(instance=todos, many=True)
        return Response(serializer.data, status=200)


@api_view(["get"])
def is_completed(request):
    if request.method == "GET":
        todos = Todo.objects.filter(completed=True)
        serializer = TodoSerializer(instance=todos, many=True)
        return Response(serializer.data, status=200)


@api_view(["get"])
def set_completed(request, pk):
    if request.method == "GET":
        try:
            todos = Todo.objects.get(id=pk, completed=False)
        except Todo.DoesNotExist:
            return Response(status=404)

        todos.completed = True
        todos.save()
        serializer = TodoSerializer(instance=todos)
        return Response(serializer.data)


@api_view(["get"])
def set_not_completed(request, pk):
    if request.method == "GET":
        try:
            todos = Todo.objects.get(id=pk, completed=True)
        except Todo.DoesNotExist:
            return Response(status=404)

        todos.completed = False
        todos.save()
        serializer = TodoSerializer(instance=todos)
        return Response(serializer.data)



