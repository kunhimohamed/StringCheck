
import json
from django.http import JsonResponse
from django.shortcuts import render
from .forms import SimpleForm

def index(request):
	if request.method == 'GET':
		form = SimpleForm()
		return render(request, 'string_check/index.html', {"form": form})
	elif request.method == 'POST':
		try:
			strings_req =json.loads(request.POST.get('strings'))	
			form = SimpleForm(strings_req)

			if form.is_valid():
				master_string = form.cleaned_data['master_string']
				string_1 = form.cleaned_data['string_1']
				string_2 = form.cleaned_data['string_2']
				string_3 = form.cleaned_data['string_3']
				string_4 = form.cleaned_data['string_4']
				
				master_str_list = list(master_string)
				stings_list = [string_1, string_2, string_3, string_4]

				result_dict_string = {}

				for each_str in stings_list:
					temp_list = []
					for each_chr in each_str:
						if each_chr in master_str_list:
							master_str_list.remove(each_chr)
							temp_list.append(each_chr)
							continue
					if(len(each_str) == len(temp_list)):
						result_dict_string[each_str] = "yes"
					else:
						result_dict_string[each_str] = "no"
				return JsonResponse({"result":result_dict_string, "status": "success"})
			else:
				return JsonResponse({"reason":"form not valid", "status": "not valid"})
		except Exception as e:
			return JsonResponse({"reason":str(e), "status": "not success"})		