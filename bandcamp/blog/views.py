from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . models import BlogPost
from . forms import BlogPostForm
from django.views import generic

@login_required
def blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            print(form.errors)
    else:
        form = BlogPostForm
    return render(request, 'manage_blog_post.html', {'form': form})


class BlogPostListView(generic.ListView):
    model = BlogPost
    template_name = "blog_view.html"
    context_object_name = 'blogpost'

class BlogPostUpdateDeleteView(generic.UpdateView, LoginRequiredMixin):
    model = BlogPost
    template_name = "blog_post_update.html"
    success_url = reverse_lazy('blog')
    form_class = BlogPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_post = self.get_object()
        context['blog_post'] = blog_post
        return context

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  
        if 'delete' in request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        blog_post = self.get_object()
        blog_post.delete()
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


