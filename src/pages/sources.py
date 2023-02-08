import dash
from dash import html, dcc
from dash_bootstrap_components import Row, Col

dash.register_page(__name__, order=2)

layout = html.Div(
    [
        Row(
            [
                Col(
                    [
                        dcc.Markdown("# Sources", className="mt-3"),
                        dcc.Markdown("### Comic book", style={"color": "gray"}),
                        dcc.Markdown("contents", style={"color": "green"}),
                        dcc.Markdown(
                            "Youtube.Com, 2023, https://www.youtube.com/watch?v=DggnyP0u0tM. Accessed 29 Jan 2023."),
                        dcc.Markdown(
                            '"Азбука Анархиста". Voenka.Kiev.Ua, 2023, '
                            'https://voenka.kiev.ua/products/azbuka-anarhista. Accessed 6 Feb 2023.'),
                        dcc.Markdown("pictures", style={"color": "green"}),  # add a source
                        dcc.Markdown('"The Black Army Of Ukraine - Historyhub.Info". Historyhub.Info - Building The '
                                     'Worlds Best Collection Of History Essays, 2018, '
                                     'https://historyhub.info/the-black-army-of-ukraine/. Accessed 3 Feb 2023.'),
                        dcc.Markdown('"Nestor Makhno - Wikipedia". En.Wikipedia.Org, 2023, '
                                     'https://en.wikipedia.org/wiki/Nestor_Makhno. Accessed 3 Feb 2023.'),
                        dcc.Markdown('"File:RPAU Flag.Svg - Wikimedia Commons". Commons.Wikimedia.Org, 2011, '
                                     'https://commons.wikimedia.org/wiki/File:RPAU_flag.svg. Accessed 3 Feb 2023.'),
                        dcc.Markdown('"The Circle-A Symbol Of Anarchism". Crwflags.Com, 2023, '
                                     'https://www.crwflags.com/fotw/flags/qt-a_%28a%29.html. Accessed 3 Feb 2023.'),
                        dcc.Markdown('"Каховська #Tachanka Судного Дня". Історична Правда, 2023, '
                                     'https://www.istpravda.com.ua/columns/2020/01/15/156881/. Accessed 3 Feb 2023.'),
                        dcc.Markdown('"Tachanka - Wikipedia". En.Wikipedia.Org, 2007, '
                                     'https://en.wikipedia.org/wiki/Tachanka. Accessed 3 Feb 2023.'),
                        dcc.Markdown('"Nestor Makhno". Timenote.Info, 2023, https://timenote.info/en/Nestor-Makhno. '
                                     'Accessed 3 Feb 2023.'),
                        dcc.Markdown("### Connection to enlightenment", style={"color": "gray"}),
                        dcc.Markdown("introduction", style={"color": "green"}),
                        dcc.Markdown('"Anarchism | Definition, Varieties, History, & Artistic Expression". '
                                     'Encyclopedia Britannica, 2023, https://www.britannica.com/topic/anarchism. '
                                     'Accessed 25 Jan 2023.'),
                        dcc.Markdown("Kropotkin's vision", style={"color": "green"}),
                        dcc.Markdown('"Кропоткин, Пётр Алексеевич — Википедия". Ru.Wikipedia.Org, 2023, '
                                     'https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%BE%D0%BF%D0%BE%D1%82%D0%BA%D0%B8'
                                     '%D0%BD,'
                                     '_%D0%9F%D1%91%D1%82%D1%80_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B5%D0%B2%D0'
                                     '%B8%D1%87. Accessed 25 Jan 2023.'),
                        dcc.Markdown('"Кропоткин Петр Алексеевич (1842-1921​) - ФИЛОСОФИЯ РОССИИ". Петр Щедровицкий, '
                                     '2021, https://shchedrovitskiy.com/kropotkin-peter-alekseyevich/. Accessed 29 '
                                     'Jan 2023.'),
                        dcc.Markdown('Кропоткин, Петр Кропоткин. Государство и его роль в истории. Geneva, “Bread and '
                                     'freedom”, 1904'),
                    ],
                    width={"size": 6, "offset": 2},
                )
            ],
            justify="center",
        )
    ]
)
