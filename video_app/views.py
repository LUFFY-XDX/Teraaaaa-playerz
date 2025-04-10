from django.shortcuts import render
from django.http import JsonResponse


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

        
        if len(user_link) >= 25:
            extracted_part = user_link[25:]
            direct_link = f"https://www.terabox.tech/play.html?url=https://www.terabox.com/{extracted_part}"

            
            last_link = direct_link

            return JsonResponse({"direct_link": direct_link})

        return JsonResponse({"error": "Invalid link"}, status=400)

def play_video(request):
    """Render the custom player.html with the video stream link."""
    video_url = request.GET.get('url', '')
    return render(request, 'player.html', {'video_url': video_url})
