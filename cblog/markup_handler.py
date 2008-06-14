def markup_to_html(text, markup="html"):
    if markup == "html":
        return text
    elif markup == "markdown":
        import markdown
        return markdown.markdown(text)
    #Textile doesn't support unicode and seems quite broken.
    #elif markup == "textile":
    #    import textile
    #    return textile.textile(str(text))
    elif markup == "rest":
        from docutils.core import publish_parts
        return publish_parts(text, writer_name = "html")['html_body']
    else:
        raise Exception("This type of markup isn't supported yet")
    
