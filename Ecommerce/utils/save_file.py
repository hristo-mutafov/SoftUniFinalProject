from django.http import HttpResponse


def upload_photo(image, path):
    with open(path, 'wb') as file:
        try:
            for chunk in image.chunks():
                file.write(chunk)
        except Exception:
            return HttpResponse(status=500)
