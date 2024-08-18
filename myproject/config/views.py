from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
import boto3
from botocore.exceptions import NoCredentialsError
from django.shortcuts import render

def hello_world(request):
    return HttpResponse('Hello World !')

def hello_japan(request):
    return HttpResponse('Hello Japan !')

class FirstClassBaseView(TemplateView):
    template_name = 'first-class-base.html'

class CompanyDetailView(TemplateView):
    template_name = 'company-detail.html'

class IndexView(TemplateView):
    template_name = 'config/index.html'

class FileUploadView(TemplateView):
    template_name = "config/upload.html"

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        s3 = boto3.client('s3', 
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                          region_name=settings.AWS_S3_REGION_NAME)
        
        content_type = file.content_type  # ファイルのContent-Typeを取得

        try:
            s3.upload_fileobj(
                file, 
                settings.AWS_STORAGE_BUCKET_NAME, 
                file.name,
                ExtraArgs={'ContentType': content_type}  # Content-Typeを指定
            )
            return render(request, self.template_name, {'success': True})
        except NoCredentialsError:
            return render(request, self.template_name, {'error': 'Credentials not available'})
