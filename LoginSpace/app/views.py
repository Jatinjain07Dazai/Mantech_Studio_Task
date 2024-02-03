from django.shortcuts import render

def login(request):
	name='jatinjain'
	password = 'hired'
	con = {"error": ""}
	if request.POST:
		if request.POST.get("fid", "Null") == name and request.POST.get("pas", "Null") == password:
			return render(request, "next.html", {})
		else:
			con = {"error": "* username and password is incorrect.Please enter correct Password.."}
	return render(request, "index.html", con)


def next(request):
	if request.POST:
		return render(request, "end.html", {})
	return render(request, "next.html", {})


def end(request):
	return render(request, 'end.html', {})