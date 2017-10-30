from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
import os, shutil, errno
from blog.models import folder, project
from blog.forms import FolderForms
from django.conf import settings

class ProjectCreate(CreateView):
	model = project
	fields = ['title']


	def get_success_url(self):
		return reverse_lazy('blog:folder', kwargs = {'ti':self.object.title})


class FolderCreate(CreateView):
	model = folder
	fields = ['title', 'project1']

	
	def get_context_data(self, **kwargs):
		context = super(FolderCreate, self).get_context_data(**kwargs)
		if self.request.POST:
			context['folder'] = FolderForms(self.request.POST, self.request.FILES)
			context['name'] = folder.objects.filter(project1__title= self.kwargs['ti'])
			context['proj'] = project.objects.get(title= self.kwargs['ti'])
		else:
			context['folder'] = FolderForms()
			context['name'] = folder.objects.filter(project1__title= self.kwargs['ti'])
			context['proj'] = project.objects.get(title= self.kwargs['ti'])
		
		return context

	
#	def delete(self,request, context):
		
#		return render(request, 'blog/delete.html', context)
		

	
	def get_success_url(self):
		return reverse_lazy('blog:folder', kwargs = {'ti':self.object.project1.title})


#	def form_valid(self, form):
#		form.instance_owner = self.request.user
#		context = self.get_context_data()
#		folder = context['folder']
#
#		if folder.is_valid():
#			self.object = form.save()
#			folder.instance = self.object
#			folder.save() 
#		return super(FolderCreate,self).form_valid(form)


	def create(request):
		static_dir = settings.STATICFILES_DIR[0]

		new_dir_path = os.path.join(static_dir, folder.title)
		try:
			os.makedir(new_dir_path)
			print(1)
		except OSError as e:
			if e.errno !=errno.EEXIST:
				print(2)
				pass
			else:
				print(error)



def folder_delete(request, id):
	folder = get_object_or_404(folder,id=folder.id)
	if request.method =='POST':
		folder.delete()
		return redirect('blog:folder')
	return render(request, 'blog/delete.html', {'folder':folder})
	 





	
