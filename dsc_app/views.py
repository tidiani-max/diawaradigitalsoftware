from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            return JsonResponse({"error": "Veuillez remplir tous les champs."}, status=400)

        subject = "Nouveau message de contact"
        body = f"Nom: {name}\nEmail: {email}\nMessage: {message}"

        try:
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,  # Must be configured in settings.py
                ["cheicktidianidiawara@gmail.com"],  # Replace with the recipient's email
                fail_silently=False,
            )
            return JsonResponse({"message": "Votre message a été envoyé avec succès!"})
        except Exception as e:
            return JsonResponse({"error": f"Erreur lors de l'envoi de l'email: {str(e)}"}, status=500)

    # Render the homepage if it's a GET request
    return render(request, "home.html")
