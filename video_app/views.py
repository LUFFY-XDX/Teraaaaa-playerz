from django.shortcuts import render
from django.http import JsonResponse

# Store the last used link
last_link = ""

def index(request):
    """Render the main page with the last used video link."""
    global last_link
    return render(request, 'index.html', {"saved_link": last_link})

def generate_link(request):
    """Generate a direct video link from the user's input."""
    global last_link

    if request.method == "GET":
        user_link = request.GET.get("link", "")

        # Ensure the link is valid
        if len(user_link) >= 25:
            extracted_part = user_link[25:]
            direct_link = f"https://www.terabox.tech/play.html?url=https%3A%2F%2Fteraboxapp.com%2Fs%2F{extracted_part}"

            # Store the last valid link
            last_link = direct_link

            return JsonResponse({"direct_link": direct_link})

        return JsonResponse({"error": "Invalid link"}, status=400)
