 # URL do postów (5 blogów, 5 postów)
URL_ZENJASKINIOWCA = 'https://zenjaskiniowca.pl/byc-jak-conor-mcgregor/'
URL_MRVINTAGE = 'https://mrvintage.pl/2013/04/biala-koszula-esencja-stylu.html'
URL_MINIMALISTS = 'https://www.theminimalists.com/fc/'
URL_OCZAMIMEZCZYZNY = 'https://www.oczamimezczyzny.pl/?p=43'
URL_MARKETINGNASTERYDACH = 'http://marketingnasterydach.pl/2016/03/3-emocjonalne-czynniki-mordujace-skutecztna-sprzedaz-i-finansowy-sukses/'

# GLOBALNE USTAWIENIA
IMG_WIDTH = '230px' # szerokość zdjęcia w pdf-ie

# -------- STRUKTURA POSTÓW --------
# ======== ZENJASKINIOWCA ========
# tytul posta: <h1 class="entry-title">Być jak Conor McGregor</h1>
# content posta: <div class="entry-content"></div>
TYTUL_TAG_ZENJASKINIOWCA = 'h1'
CONTENT_TAG_ZENJASKINIOWCA = 'div'
TYTUL_CLASS_ZENJASKINIOWCA = 'entry-title'
CONTENT_CLASS_ZENJASKINIOWCA = 'entry-content'

# ======== MRVINTAGE ========
# tytul posta: <h1 class="article-title">Biała koszula – esencja stylu</h1>
# content posta: <section class="single-content clearfix" itemprop="articleBody"></section>
TYTUL_TAG_MRVINTAGE = 'h1'
CONTENT_TAG_MRVINTAGE = 'section'
TYTUL_CLASS_MRVINTAGE = 'article-title'
CONTENT_CLASS_MRVINTAGE = 'single-content'

# ======== MINIMALISTS ========
# tytul posta: <h1>
# content posta: <div class="entry-content"></div>
TYTUL_TAG_MINIMALISTS  = 'h1'
CONTENT_TAG_MINIMALISTS  = 'div'
TYTUL_CLASS_MINIMALISTS = 'entry-title'
CONTENT_CLASS_MINIMALISTS  = 'entry-content'

# ======== OCZAMIMEZCZYZNY ========
# tytul posta: <h1 class="entry-title">Nie daj więc sobie nigdy wmówić, że czegoś nie potrafisz.</h1>
# content posta: <div class="format_text entry-content"></div>
TYTUL_TAG_OCZAMIMEZCZYZNY  = 'h1'
CONTENT_TAG_OCZAMIMEZCZYZNY  = 'div'
TYTUL_CLASS_OCZAMIMEZCZYZNY= 'entry-title'
CONTENT_CLASS_OCZAMIMEZCZYZNY  = 'entry-content'

# ======== MARKETINGNASTERYDACH ========
# tytul posta: <h1 class="post-title entry-title" itemprop="headline"></h1>
# content posta: <div class="format_text entry-content"></div>
TYTUL_TAG_MARKETINGNASTERYDACH  = 'h1'
CONTENT_TAG_MARKETINGNASTERYDACH  = 'div'
TYTUL_CLASS_MARKETINGNASTERYDACH = 'post-title'
CONTENT_CLASS_MARKETINGNASTERYDACH  = 'entry-content'

# ++++++++ SUMMARY ++++++++
POSTS_DICT = {
    'ZENJASKINIOWCA' : [URL_ZENJASKINIOWCA,TYTUL_TAG_ZENJASKINIOWCA, TYTUL_CLASS_ZENJASKINIOWCA,
                        CONTENT_TAG_ZENJASKINIOWCA, CONTENT_CLASS_ZENJASKINIOWCA],
    'MRVINTAGE' : [URL_MRVINTAGE,TYTUL_TAG_MRVINTAGE, TYTUL_CLASS_MRVINTAGE,
                        CONTENT_TAG_MRVINTAGE, CONTENT_CLASS_MRVINTAGE],
    'MINIMALISTS' : [URL_MINIMALISTS,TYTUL_TAG_MINIMALISTS, TYTUL_CLASS_MINIMALISTS,
                        CONTENT_TAG_MINIMALISTS, CONTENT_CLASS_MINIMALISTS],
    'OCZAMIMEZCZYZNY': [URL_OCZAMIMEZCZYZNY , TYTUL_TAG_OCZAMIMEZCZYZNY , TYTUL_CLASS_OCZAMIMEZCZYZNY ,
                  CONTENT_TAG_OCZAMIMEZCZYZNY , CONTENT_CLASS_OCZAMIMEZCZYZNY],
    'MARKETINGNASTERYDACH' : [URL_MARKETINGNASTERYDACH, TYTUL_TAG_MARKETINGNASTERYDACH, TYTUL_CLASS_MARKETINGNASTERYDACH,
                  CONTENT_TAG_MARKETINGNASTERYDACH, CONTENT_CLASS_MARKETINGNASTERYDACH]
}