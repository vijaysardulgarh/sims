from reportlab.platypus import SimpleDocTemplate



def export_to_pdf(filename):

    document = SimpleDocTemplate(filename)

    return document