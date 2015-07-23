from django.shortcuts import render


class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last 20 cards."""
        return Card.objects.order_by('-created_at')[:20]


class DetailView(generic.DetailView):
    model = Card
    template_name = 'cards/detail.html'
