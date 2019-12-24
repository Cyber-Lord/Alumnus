from django.shortcuts import render
from django.views import View
from .models import Faculty

class HomeView(View):
	template_name = "home.html"
	model = Faculty
	def get(self, request):
		f = self.model.objects.all()
		ct = {'faculties' : f}
		return render(request, self.template_name, ct)

	def post():
		pass