import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib import messages
from .models import Questions
from .forms import Importdataform
from docx2python import docx2python
from PIL import Image

class ImportDocx(LoginRequiredMixin, CreateView):
    model = Questions
    form_class = Importdataform
    template_name = 'import.html'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_path = os.path.join(BASE_DIR, 'media/')
    
    
    def post(self, *args,**kwargs):
        uploaded_file = self.request.FILES['document']
        document = docx2python(uploaded_file,self.img_path)
        os.chdir(self.img_path)
        for f in os.listdir(self.img_path):
            if f.endswith('.wmf') or f.endswith('.emf') or f.endswith('.jpeg'):
                i = Image.open(f)
                fn,fext = os.path.splitext(f)
                i.save('{}.png'.format(fn))
        document_content=document.body
        z=document_content[0][0][0]
        composite_list = [z[x:x+8] for x in range(0, len(z),8)]
        for row in composite_list:
            try:
                data = Questions.objects.create(
                    subject=row[0],
                    question=row[1],
                    ques_image=row[2],
                    option_a=row[3],
                    option_b=row[4],
                    option_c=row[5],
                    option_d=row[6],
                    ans=row[7]
                )
            except Exception as e:
                print(e)
        messages.success(self.request,'Data uploded successfully')
        return redirect("admin/")