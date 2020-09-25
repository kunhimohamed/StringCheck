
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
	print(request.method)
	if request.method == 'GET':
		return render(request, 'string_check/index.html', {})
	elif request.method == 'POST':
		try:
			master_string = request.POST.get('master_string')
			string_1 = request.POST.get('string_1')
			string_2 = request.POST.get('string_2')
			string_3 = request.POST.get('string_3')
			string_4 = request.POST.get('string_4')
			
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
		except Exception as e:
			return JsonResponse({"reason":str(e), "status": "not success"})		