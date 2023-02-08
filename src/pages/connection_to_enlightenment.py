import dash
from dash import html, dcc

dash.register_page(__name__, order=1)

layout = html.Div(
    [
        dcc.Markdown("# The roots of anarchism", style={"textAlign": "center"}),
        html.Hr(),
        dcc.Markdown("## Introduction", style={"color": "grey"}),
        dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;The origins of anarchism as a political philosophy date back to the "
                     "17th century, when English philosopher William Godwin first proposed a form of political "
                     "philosophy based on the idea of “non-domination”. Godwin argued that the only way to guarantee "
                     "the freedom of individuals was through the absence of government and the absence of hierarchy."),
        dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;The ideas of Godwin were further developed by other thinkers, "
                     "such as Pierre-Joseph Proudhon and Mikhail Bakunin. Proudhon claimed that the only way to "
                     "ensure freedom was to abolish private property and ensure that the only form of government was "
                     "one based on mutual agreement between all participants. This became known as “anarchist "
                     "collectivism”. Bakunin, on the other hand, proposed a form of anarchism that rejected the idea "
                     "of government altogether and instead proposed a society based on free and voluntary "
                     "associations of individuals and groups. This form of anarchism became known as “libertarian "
                     "socialism”."),
        dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;The ideas of early philosophers such as Godwin, Proudhon have been "
                     "further developed in the 19th and 20th centuries by other anarchist writers such as Emma "
                     "Goldman, Peter Kropotkin and Noam Chomsky. But here we will mostly focus on Peter Kropotkin."),
        dcc.Markdown("## Kropotkin's vision", style={"color": "grey"}),
        dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;Peter Kropotkin was a Russian geographer, anarchist, and activist. He "
                     "was born in Moscow in 1842 and studied in St. Petersburg, where he worked at the Ministry of "
                     "Internal Affairs. Kropotkin was also a prominent anarchist thinker, writing extensively on the "
                     "subject and promoting his ideas within the Russian Empire. "),
        dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;In his book “State: Its Historic Role”, Peter Kropotkin presents an "
                     "argument that the very idea of a state is oppressive and authoritarian. He argues that the "
                     "state is not a tool for achieving social justice, but rather an instrument of domination and "
                     "control. He further argues that the state is not a natural phenomenon, but rather an artificial "
                     "construct created by powerful individuals and groups. Kropotkin's argument is that the state "
                     "emerged as a result of an unequal distribution of wealth and power. He thinks that the state "
                     "was created by the wealthy and powerful to protect their own interests and to prevent their "
                     "wealth and power from being challenged by the people. He also claims that the state has been "
                     "used throughout history to oppress and exploit the people, to maintain the status quo, "
                     "and to reinforce existing power structures."),
        dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;Peter also argues that the state has failed to achieve its stated goals "
                     "of protecting individual freedom, equality, justice, and security. He claims that the state has "
                     "been unsuccessful in achieving these goals and has instead been used to oppress and exploit the "
                     "people. He further argues that the state has been used to create an unjust system of inequality "
                     "and unfairness. The state is not necessary in order to protect individuals or groups from "
                     "external threats, as individuals and groups are capable of protecting themselves through mutual "
                     "aid and cooperation."),
        dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;Kropotkin denies that the state is the only possible form of social "
                     "organisation. Instead, he claims that a free and voluntary association of individuals and "
                     "groups can form an alternative form of social organisation, one in which individuals and groups "
                     "are free to make their own decisions and to live in harmony with others. He argues that such an "
                     "organisation would be more just and equitable than the state, as it would be based on "
                     "cooperation, rather than domination and oppression. He believes that the only way for society "
                     "to achieve true freedom and justice is for the state to be abolished and for individuals and "
                     "groups to form their own voluntary associations and take control of their own lives. Kropotkin "
                     "is certain that this is the only way for true social justice to be achieved."),
        dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;Later in 1914 Kropotkin’s ideas became inspiration for Ukrainian '
                     'anarchist Nestor Makhno, one time he even met with his “teacher”: when Makhno was in Moscow, '
                     'Despite his nervousness, he chose to meet with Kropotkin and uninvitedly visited him. Makhno '
                     'remembered, "He received me compassionately, like no one has ever received me. He also spent a '
                     'lot of time talking with me about the Ukrainian peasants. I asked him questions, '
                     'and he provided me with satisfactory answers to each one. just about everything!”. He was '
                     'obsessed with the idea of anarchism and gathered several thousand army of people who shared the '
                     'same ideology and. With the army and ideas they established an anarchist state with its capitan '
                     'in Hulaipole, more on this in the comic.')
    ]
)
