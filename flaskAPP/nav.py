from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for
)

bp = Blueprint('nav',__name__,url_prefix='/nav')

@bp.route('/home')
def home():
    kwargs={
        'title':'Home',
        'jumbotron':{
            "header":"Image Style Playground",
            "bg_image":url_for('static',filename = '/images/bg1450496.jpg'),
             "text":"Add text"
        },
        'homePageContents':[{
        "Title":"Style Transfer",
        "Text": "Neural Style Transfer (NST) refers to a class of software algorithms that manipulate digital images, or videos, in order to adopt the appearance or visual style of another image. NST algorithms are characterized by their use of deep neural networks for the sake of image transformation. Common uses for NST are the creation of artificial artwork from photographs, for example by transferring the appearance of famous paintings to user-supplied photographs. Several notable mobile apps use NST techniques for this purpose, including DeepArt and Prisma. This method has been used by artists and designers around the globe to develop new artwork based on existent style(s). --Wikipedia Neural Style Transfer",
        "imagePath": url_for('static',filename = '/images/styleTransfer.jpeg'),
        "Link":"/styletransfer",
        "Action":"+ Go Style Transfer"
    },
    {

        "Title": "Color Harmonization",
        "Text": "In color theory, color harmony refers to the property that certain aesthetically pleasing color combinations have. These combinations create pleasing contrasts and consonances that are said to be harmonious. These combinations can be of complementary colors, split-complementary colors, color triads, or analogous colors. Color harmony has been a topic of extensive study throughout history, but only since the Renaissance and the Scientific Revolution has it seen extensive codification. Artists and designers make use of these harmonies in order to achieve certain moods or aesthetics.--Wikipedia Neural Style Transfer",
        "imagePath":url_for('static',filename ='/images/colorHar.png'),
        "Link":"/colorharm",
        "Action":"+ Go Color Harmonization"
    },{
        "Title":"Gallery",
        "Text":"In our Gallery, you can look at style transfer and color harmonization products.",
        "imagePath":url_for('static',filename ='/images/gallery.png'),
        "Link": "/gallery",
        "Action":"+ Go to gallery"
    }
    ]
    }

    return render_template('nav/home.html',**kwargs)