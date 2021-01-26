from django.shortcuts import render, redirect
from . import forms
from django.views import View
from django.views.generic import FormView
import requests
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from bs4 import BeautifulSoup

# Create your views here.
cbox = []
lotto = []
'''
    if form.is_valid():
        return render(request,"lottery.html",context={
            "form":form,
            "num1":form.cleaned_data.get("num1"),
            "num2":form.cleaned_data.get("num2"),
            "num3":form.cleaned_data.get("num3"),
            "num4":form.cleaned_data.get("num4"),
            "num5":form.cleaned_data.get("num5"),
            "num6":form.cleaned_data.get("num6"),
        })
    '''
class InputLottery(View):

    def l_num(self, page_num):
        global lotto
        global cbox
        try:
            url = requests.get(f"https://kr.lottolyzer.com/history/south-korea/6_slash_45-lotto/page/{page_num}/per-page/50/summary-view")
        except Exception:
            return 0
        indeed_soup = BeautifulSoup(url.text,"html.parser")
        last_num_table = indeed_soup.find("tbody").findAll("tr")
        first_num = last_num_table[0].find("td").text
        if first_num == "기록이 없습니다":
            return 0
        last_num = last_num_table[len(last_num_table)-1].find("td").text
        for i in range(int(last_num), int(first_num)+1):
            cbox.append(list(map(lambda x:int(x.strip()),last_num_table[i-int(last_num)].findAll("td",{"class":"sum-p1"})[1].text.split(','))))
    
        return int(last_num)

    def exe(self):
        global lotto
        global cbox
        if len(cbox) and len(lotto):
            return lotto
        else:
            page = 1
            while self.l_num(page):
                page+=1
            print(cbox)

            lotto = [0]*46
            size = len(cbox)
            for num in range(1,46):
                c = 0
                for i in range(size):
                    if num in cbox[i]:
                        c+=1
                lotto[num] = (c/size)
            return lotto

    def post(self, request):

        url = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=%EB%A1%9C%EB%98%90&qdt=0&ie=utf8&query=%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8%EC%A1%B0%ED%9A%8C")
        indeed_soup = BeautifulSoup(url.text,"html.parser")
        numbox = indeed_soup.find("div",{"class":"num_box"})

        container = []
        bonus = []
        for i in range(len(numbox.findAll("span"))):
            if i < 6:
                container.append(int(numbox.findAll("span")[i].text))
        bonus.append(int(numbox.findAll("span")[i].text))
        form = forms.InputForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            c = 0
            isbonus = False
            for i in range(1,7):
                if form.cleaned_data.get(f"num{i}") in list(container+bonus):
                    c+=1
                    if form.cleaned_data.get(f"num{i}") == list(container+bonus)[6]:
                        isbonus = True
            self.exe()
            num1 = int(form.cleaned_data.get(f"num1"))
            num2 = int(form.cleaned_data.get(f"num2"))
            num3 = int(form.cleaned_data.get(f"num3"))
            num4 = int(form.cleaned_data.get(f"num4"))
            num5 = int(form.cleaned_data.get(f"num5"))
            num6 = int(form.cleaned_data.get(f"num6"))
            pro = lotto[num1]*lotto[num2]*lotto[num3]*lotto[num4]*lotto[num5]*lotto[num6]
            expected = 1000*(int(1000*(1/pro))//1000)
            return render(request,"galleries/gallery_list.html", context={
                'form':form, 
                "container":container, 
                "bonus":bonus,
                "done":True, 
                "count":c,
                "eight":8, 
                "isbonus":isbonus,
                "lotto":lotto,
                "expected":expected,
            })

        return render(request,"galleries/gallery_list.html", context={'form':form, "done":None})
    def get(self, request):
        form = forms.InputForm()
        return render(request,"galleries/gallery_list.html", context={'form':form, "done":False})


class LoginView(FormView):

    template_name = "galleries/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("home:gallery")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email,password = password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def log_out(request):
    logout(request)
    return redirect(reverse("home:gallery"))

class SignUpView(FormView):
    template_name = "galleries/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("home:gallery")

    def form_valid(self,form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email,password = password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
