from django import forms

class InputForm(forms.Form):
    num1 = forms.IntegerField(max_value=45,min_value=1)
    num2 = forms.IntegerField(max_value=45,min_value=1)
    num3 = forms.IntegerField(max_value=45,min_value=1)
    num4 = forms.IntegerField(max_value=45,min_value=1)
    num5 = forms.IntegerField(max_value=45,min_value=1)
    num6 = forms.IntegerField(max_value=45,min_value=1)

    def clean(self):
        s = set()
        for i in range(1,7):
            s.add(self.cleaned_data.get(f"num{i}"))
        if len(s) != 6:
            print("Not all numbers are distincts")
            self.add_error("num1", forms.ValidationError("Not all numbers are distincts"))
        for i in s:
            if type(i) != type(1):
                self.add_error("num1", forms.ValidationError("Numbers should be integer"))
            
            elif i<1 or i>45:
                self.add_error("num1", forms.ValidationError("Numbers should be between 1 and 45"))

                