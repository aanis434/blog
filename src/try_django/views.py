from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost


def home_page(resquest):
    # return HttpResponse("<h1>Hello Django!</h1>")
    # doc = "<h1>{title}</h1>.format(title=title)
    # django_rendered_doc = "<h1>{{title}}</h1>.format(title=title)
    qs = BlogPost.objects.all()[:3]
    title = "Welcome To Our Blog Site!"
    context = {
        "title": title,
        "object": qs
    }
    return render(resquest, "home.html", context)


def about_page(resquest):
    return render(resquest, "about.html", {"title": "About Us"})


def contact_page(resquest):
    form = ContactForm(resquest.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(resquest, "form.html", context)


def example_page(resquest):
    # ^rendering anykind of template with get_template()
    context = {"title": "Example Page"}
    template_name = "example.txt"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
