from django.shortcuts import render, redirect
from django.http import Http404
from . import util
import random
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search(request):
    query = request.GET.get('q')

    if not query:
        return redirect('index')

    all_entries = util.list_entries()
    matching_entries = [entry for entry in all_entries if query.lower() in entry.lower()]

    # If query matches exactly with an entry title, redirect to that entry's page
    if query.lower() in [entry.lower() for entry in all_entries]:
        return redirect('entry', title=query)

    return render(request, "encyclopedia/search_results.html", {
        "matching_entries": matching_entries,
        "query": query
    })


def entry(request, title):
    content = util.get_entry(title)
    if content:
        content_html = markdown2.markdown(content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content_html
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": f"The requested page '{title}' was not found. Please check the spelling or try searching for something else."
        })


def custom_404_view(request, exception):
    return render(request, "encyclopedia/error.html", {"message": str(exception)})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        if util.get_entry(title):
            # Entry already exists, show an error
            return render(request, "encyclopedia/create.html", {
                "error": "An entry with this title already exists."
            })

        # Save the new entry and redirect to its page
        util.save_entry(title, content)
        return redirect('entry', title=title)

    return render(request, "encyclopedia/create.html")


def edit(request, title):
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(title, content)
        return redirect('entry', title=title)

    content = util.get_entry(title)
    if content is None:
        return redirect('index')

    return render(request, "encyclopedia/edit.html", {
        'title': title,
        'content': content
    })


def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('entry', title=random_entry)


def handler404(request, exception):
    return render(request, 'encyclopedia/error.html', {'message': 'The page you are looking for does not exist.'}, status=404)