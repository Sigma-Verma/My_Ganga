import subprocess
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt
def chat_with_llm(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_question = data.get("question", "").strip()
        except json.JSONDecodeError:
            return JsonResponse({"error": " Invalid "}, status=400)

    elif request.method == "GET":
        user_question = request.GET.get("q", "").strip()

    else:
        return JsonResponse({"error": "Only GET and POST  allowed"}, status=405)

    if not user_question:
        return JsonResponse({"error": "Empty question"}, status=400)

    #   call the Ollama cli
    result = subprocess.run(
        ["ollama", "run", "deepseek-coder-v2:latest", user_question],
        capture_output=True,
        text=True
    )

    llm_response = result.stdout.strip()

    return JsonResponse({"response": llm_response})



def chat_page(request):
    return render(request, "chat/index.html")

