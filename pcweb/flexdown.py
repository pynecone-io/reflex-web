import flexdown

import reflex as rx
from pcweb.templates.docpage import (
    code_block_markdown,
    code_comp,
    docdemo,
    docgraphing,
    doclink2,
    h1_comp,
    h2_comp,
    h3_comp,
    text_comp,
)


class AlertBlock(flexdown.blocks.Block):
    """A block that displays a component along with its code."""

    starting_indicator = "```md alert"
    ending_indicator = "```"
    include_indicators = True

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)

        args = lines[0].removeprefix(self.starting_indicator).split()

        if len(args) == 0:
            args = ["info"]
        status = args[0]

        if lines[1].startswith("#"):
            title = lines[1].strip("#").strip()
            content = "\n".join(lines[2:-1])
        else:
            title = ""
            content = "\n".join(lines[1:-1])

        return rx.alert(
            rx.alert_icon(),
            rx.box(
                rx.alert_title(markdown(title)) if title else "",
                rx.alert_description(markdown(content)),
            ),
            status=status,
        )

class SectionBlock(flexdown.blocks.Block):
    """A block that displays a component along with its code."""

    starting_indicator = "```md section"
    ending_indicator = "```"

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)

        # Split up content into sections based on markdown headers.
        header_indices = [i for i, line in enumerate(lines) if line.startswith("#")]
        header_indices.append(len(lines))
        sections = [
            (lines[header_indices[i]].strip("#"), "\n".join(lines[header_indices[i] + 1 : header_indices[i + 1]]))
            for i in range(len(header_indices) - 1)
        ]


        return rx.box(
            rx.vstack(
                *[
                    rx.fragment(
                        rx.text(
                            rx.span(
                                header,
                                font_weight="bold",
                            ),
                            width="100%",
                        ),
                        rx.box(
                            markdown(section),
                            width="100%",
                        ),
                    )
                    for header, section in sections
                ],
                text_align="left",
                margin_bottom="2em",
                width="100%",
            ),
            margin_top="1em",
            margin_left=".5em",
            border_left="1px #F4F3F6 solid",
            padding_left="1em",
            width="100%",
        )

class DemoBlock(flexdown.blocks.Block):
    """A block that displays a component along with its code."""

    starting_indicator = "```python demo"
    ending_indicator = "```"
    include_indicators = True

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)
        code = "\n".join(lines[1:-1])

        args = lines[0].removeprefix(self.starting_indicator).split()

        if "exec" in args:
            exec(code, env, env)
            comp = env[list(env.keys())[-1]]()
        elif "graphing" in args:
            exec(code, env, env)
            comp = env[list(env.keys())[-1]]()
            # Get all the code before the final "def".
            parts = code.rpartition(
                "def",
            )
            data, code = parts[0], parts[1] + parts[2]
            comp = docgraphing(code, comp=comp, data=data)
        else:
            comp = eval(code, env, env)

        return docdemo(code, comp=comp)


component_map = {
    "h1": lambda text: h1_comp(text=text),
    "h2": lambda text: h2_comp(text=text),
    "h3": lambda text: h3_comp(text=text),
    "p": lambda text: text_comp(text=text),
    "a": doclink2,
    "code": lambda text: code_comp(text=text),
    "codeblock": code_block_markdown,
}
# Monkeypatch markdown custom components.
md = rx.markdown("", component_map=component_map)
custom = md.get_custom_components()


@rx.memo
def markdown1(text):
    return rx.markdown(text, component_map=component_map)


def get_custom_components(self, seen):
    return custom


rx.Markdown.get_custom_components = get_custom_components


xd = flexdown.Flexdown(block_types=[DemoBlock, AlertBlock, SectionBlock], component_map=component_map)


def markdown(text):
    return xd.default_block_type().render_fn(content=text)
