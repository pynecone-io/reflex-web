import reflex as rx
from pcweb import constants, styles
from pcweb.components.logo import logo
from pcweb.pages.docs import getting_started
from pcweb.pages.docs.gallery import gallery
from pcweb.pages.docs.library import library
from pcweb.pages.index import index

footer_item_style = {
    "font_family": styles.SANS,
    "font_weight": "500",
    "_hover": {"color": "#82799E"},
    "color": "#AA9EC3",
}

footer_style = {
    "box_shadow": "medium-lg",
    "border_top": "0.1em solid #82799E",
    "vertical_align": "bottom",
    "padding_top": "4em",
    "padding_bottom": "2em",
    "padding_x": styles.PADDING_X2,
    "bg": "#110F1F",
}


def footer(style=footer_style):
    from pcweb.pages.blog import blg
    from pcweb.pages.changelog import changelog
    from pcweb.pages.faq import faq

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.desktop_only(
                    logo(
                        width=["5em", "6em", "7em"],
                    ),
                ),
                rx.vstack(
                    rx.text("Site", color="#DACEEE"),
                    rx.link("Home", href=index.path, style=footer_item_style),
                    rx.link("Gallery", href=gallery.path, style=footer_item_style),
                    rx.link("Blog", href=blg.path, style=footer_item_style),
                    rx.link(
                        "Changelog",
                        href=changelog.path,
                        style=footer_item_style,
                    ),
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Documentation", color="#DACEEE"),
                    rx.link(
                        "Introduction",
                        href=getting_started.introduction.path,
                        style=footer_item_style,
                    ),
                    rx.link(
                        "Installation",
                        href=getting_started.installation.path,
                        style=footer_item_style,
                    ),
                    rx.link(
                        "Components",
                        href=library.path,
                        style=footer_item_style,
                    ),
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Resources", color="#DACEEE"),
                    rx.link(
                        "FAQ",
                        href=faq.path,
                        style=footer_item_style,
                    ),
                    rx.link(
                        "Roadmap",
                        href=constants.ROADMAP_URL,
                        style=footer_item_style,
                    ),
                    rx.link(
                        "Forum",
                        href=constants.GITHUB_DISCUSSIONS_URL,
                        style=footer_item_style,
                    ),
                    align_items="start",
                ),
                justify="between",
                color=styles.LIGHT_TEXT_COLOR,
                align_items="top",
                padding_bottom="3em",
                min_width="100%",
            ),
            rx.hstack(
                rx.text(
                    "Copyright © 2024 Pynecone, Inc.",
                    style=footer_item_style,
                ),
                rx.hstack(
                    rx.link(
                        rx.image(src="/companies/light/github.svg", alt="A link to Reflex's Github", height="1.75em"),
                        href=constants.GITHUB_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/linkedin.svg", alt="A link to Reflex's Linkedin", height="1.75em"),
                        href=constants.LINKEDIN_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/yc.svg", alt="A link to Reflex's YC profile", height="1.75em"),
                        href=constants.YC_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/twitter.svg", alt="A link to Reflex's Twitter", height="1.75em"),
                        href=constants.TWITTER_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/discord.svg", alt="A link to Reflex's Discord", height="1.75em"),
                        href=constants.DISCORD_URL,
                    ),
                    gap="1em",
                ),
                justify="between",
                color=styles.LIGHT_TEXT_COLOR,
                padding_bottom="2em",
                min_width="100%",
            ),
        ),
        **style,
    )
