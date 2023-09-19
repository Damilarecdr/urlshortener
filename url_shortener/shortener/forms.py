from django import forms

class URLForm(forms.Form):
    original_url = forms.URLField(
        label='Enter the URL you want to shorten:',
        widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}),
        required=True
    )
#We import the forms module from Django.
#We define a form class URLForm that inherits from forms.Form.
#Inside the form class, we define a single field called original_url as a forms.URLField.
#We set a label and placeholder text for the input field.
#This form allows users to submit URLs for shortening.

#The line widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}) in the forms.URLField definition within Django's form class specifies how the URL input field should be rendered in the HTML form. Let's break down what each part of this line does:

#widget: In Django forms, a widget is responsible for rendering the HTML representation of a form field. Different types of fields (e.g., text, URL, date) can have different widgets to control how they are displayed in the HTML form.

#forms.URLInput: forms.URLInput is a specific widget type provided by Django for handling URL input fields. It's designed to render an HTML input element with the appropriate attributes for capturing URLs. This widget is suitable for URLField, as it validates and expects URLs as input.

#attrs={'placeholder': 'https://example.com'}: This part defines HTML attributes for the rendered input element. In this case, it sets the placeholder attribute to 'https://example.com'. The placeholder attribute is used to provide a hint or example text inside the input field, which disappears when the user starts typing. In this context, it suggests to the user that they should input a URL in the format 'https://example.com'.

#So, when you define widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}) within a URLField in your Django form, it ensures that the corresponding HTML input element for that field includes a placeholder text of 'https://example.com' to provide guidance to the user on the expected input format (a URL).
#The term "attrs" is short for "attributes" in the context of web development and HTML. In Django forms, the attrs parameter is used to specify HTML attributes for form fields or widgets when they are rendered in an HTML template.