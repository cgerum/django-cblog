import re
from urlparse import urlparse

def markup_to_html(text, markup="html"):
    (urls, text) = replace_media(text)
    if markup == "html":
        res = text
    elif markup == "markdown":
        import markdown
        res = markdown.markdown(text)
    #Textile doesn't support unicode and seems quite broken.
    #elif markup == "textile":
    #    import textile
    #    return textile.textile(str(text))
    elif markup == "rest":
        from docutils.core import publish_parts
        res = publish_parts(text, writer_name = "html")['html_body']
    else:
        raise Exception("This type of markup isn't supported yet")
    
    res = handle_media(res, urls)

    return res

def replace_media(text):
    medias = re.finditer("\!media:.*?\!", text)
    l = []
    i=0
    for media in medias:
        id = "media__"+str(i)+"__media"
        text = re.sub(re.escape(media.group()), id, text)
        dict  = re.match("\!media: (?P<url>.*?)( (?P<width>\d*))?( (?P<height>\d*))?( \"?(?P<alt>\w*)\")? ?\!", media.group()).groupdict()
        i = i+1
        l.append((id, dict))

    return (l, text)
    
def handle_media(text, dict):
    
    def handle_youtube(dict):
        url = urlparse(dict['url'])
        m = re.match(".*?v\=(?P<id>\w+)&?.*", url[4])
        if m:
            id = m.group("id")
            temp = r'<object width="425" height="344"><param name="movie" value="http://www.youtube.com/v/<id>&hl=en"></param><embed src="http://www.youtube.com/v/<id>&hl=en" type="application/x-shockwave-flash" width="425" height="344"></embed></object>'
            
            return re.sub("\<id\>", id, temp, 2)

    def handle_image(dict):
        temp = "<img src=\""
        temp += dict['url'] + "\" "
        if dict['width']:
            temp += "width=" + dict['width'] + " "
        if dict['height']:
            temp += "height=" + dict['height'] + " "
        if dict['alt']:
            temp += "alt=\""+dict['alt']+"\""
        temp+= "></img>"
        return temp

    print dict
    for d in dict: 
        embed = ""
        url = d[1]['url']
        if re.match(".*youtube.*", url):
            embed = handle_youtube(d[1])
        if re.match(".*\.jpg", url) or  re.match(".*\.png", url):
            embed = handle_image(d[1]);
        text = re.sub(re.escape(d[0]), embed, text)
    return text
