from urllib import parse
from django import template

register = template.Library()

def video_embed(context, url):
    url_data = urlparse.urlparse(url)
    query = urlparse.parse_qs(url_data.query)
    try:
        video_id = query["v"][0]
        context['embed_url'] = ('http://youtube.com/embed/%s' % video_id)
    except KeyError:
        context['video_url'] = url
    return context('trail_detail.html', {'youtube_video': youtube_video})