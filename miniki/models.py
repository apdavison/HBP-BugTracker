from django.db import models
from django.core.urlresolvers import reverse


class TicketPage(models.Model):
    """A Ticket page"""

    title = models.CharField(max_length=1024)
    text = models.TextField(help_text="formatted using ReST")
    # This field stores the UUID added as an argument by the Collaboratory.
    # ctx = models.UUIDField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    # UUIDField is not supported by automatic JSON serializer
    # so we add a method that retrieve a more convenient dict.
    def as_json(self):
        return {
            'title': self.title,
            'text': self.text,
            # 'ctx': str(self.ctx),
        }

    @models.permalink
    def get_absolute_url(self):
        return reverse('ticket_page_show') #, args=[str(self.ctx)])

class TicketPageCreate(models.Model):
    """A Ticket page"""

    title = models.CharField(max_length=1024)
    text = models.TextField(help_text="formatted using ReST")
    # This field stores the UUID added as an argument by the Collaboratory.
    # ctx = models.UUIDField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()

    def __unicode__(self):
        return self.title

    # UUIDField is not supported by automatic JSON serializer
    # so we add a method that retrieve a more convenient dict.
    def as_json(self):
        return {
            'title': self.title,
            'text': self.text,
            # 'ctx': str(self.ctx),
            'created_by': self.created_by
        }

    @models.permalink
    def get_absolute_url(self):
        return reverse('ticket_page_create') #, args=[str(self.ctx)])

class Home(models.Model):
    title = models.CharField(max_length=1024) 
    #ctx = models.UUIDField(unique=True)

    def __unicode__(self):
        return self.title

    def as_json(self):
        return {
            'title': self.title,
     #       'ctx': str(self.ctx),
        }

    @models.permalink
    def get_absolute_url(self):
        return reverse('home') #, args=[str(self.ctx)])
    
class TicketList (models.Model) :
    title = models.CharField(max_length=1024)
    ticket_list = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.title

    def as_json(self):
        return {
            'title': self.title,
            #'ctx': str(self.ctx),
            'ticket_list': [1,2,3,4,5] #self.ticket_list

        }