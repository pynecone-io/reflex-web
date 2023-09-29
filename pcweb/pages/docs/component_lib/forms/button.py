import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext, docpage
from pcweb import flexdown

# Forms
basic_button = """rx.button("Click Me!")
"""
button_style = """rx.button_group(
    rx.button("Example", bg="lightblue", color="black", size = 'sm'),
    rx.button("Example", bg="orange", color="white", size = 'md'),
    rx.button("Example", color_scheme="red", size = 'lg'),
    space = "1em",
)
"""
button_visual_states = """rx.button_group(
    rx.button("Example", bg="lightgreen", color="black", is_loading = True),
    rx.button("Example", bg="lightgreen", color="black", is_disabled = True),
    rx.button("Example", bg="lightgreen", color="black", is_active = True),
    space = '1em',
)
"""

button_group_example = """rx.button_group(
    rx.button(rx.icon(tag="minus"), color_scheme="red"),
    rx.button(rx.icon(tag="add"), color_scheme="green"),
    is_attached=True,
)
"""

button_sizes ="""rx.button_group(
    rx.button('Example', bg='lightblue', color='black', size='sm'),
    rx.button('Example', bg='orange', color='white', size='md'),
    rx.button('Example', color_scheme='red', size='lg'),
)
"""


button_colors = """rx.button_group(
            rx.button('White Alpha', color_scheme='whiteAlpha', min_width='unset'),
            rx.button('Black Alpha', color_scheme='blackAlpha', min_width='unset'),
            rx.button('Gray', color_scheme='gray', min_width='unset'),
            rx.button('Red', color_scheme='red', min_width='unset'),
            rx.button('Orange', color_scheme='orange', min_width='unset'),
            rx.button('Yellow', color_scheme='yellow', min_width='unset'),
            rx.button('Green', color_scheme='green', min_width='unset'),
            rx.button('Teal', color_scheme='teal', min_width='unset'),
            rx.button('Blue', color_scheme='blue', min_width='unset'),
            rx.button('Cyan', color_scheme='cyan', min_width='unset'),
            rx.button('Purple', color_scheme='purple', min_width='unset'),
            rx.button('Pink', color_scheme='pink', min_width='unset'),
            rx.button('LinkedIn', color_scheme='linkedin', min_width='unset'),
            rx.button('Facebook', color_scheme='facebook', min_width='unset'),
            rx.button('Messenger', color_scheme='messenger', min_width='unset'),
            rx.button('WhatsApp', color_scheme='whatsapp', min_width='unset'),
            rx.button('Twitter', color_scheme='twitter', min_width='unset'),
            rx.button('Telegram', color_scheme='telegram', min_width='unset'),
            width='100%',
    )
    
"""


button_variants = """rx.button_group(
            rx.button('Ghost Button', variant='ghost'),
            rx.button('Outline Button', variant='outline'),
            rx.button('Solid Button', variant='solid'),
            rx.button('Link Button', variant='link'),
            rx.button('Unstyled Button', variant='unstyled'),
        )
"""


button_disable = """rx.button('Inactive button', is_disabled=True)"""

loading_states = """rx.button(
                'Random button',
                is_loading=True,
                loading_text='Loading...',
                spinner_placement='start'
        )
"""

stack_buttons_vertical = """rx.stack(
            rx.button('Button 1'),
            rx.button('Button 2'),
            rx.button('Button 3'),
            direction='column',
    )
    
"""

stack_buttons_horizontal = """rx.stack(
            rx.button('Button 1'),
            rx.button('Button 2'),
            rx.button('Button 3'),
            direction='row',
    )
"""

button_group = """rx.button_group(
                rx.button('Option 1'),
                rx.button('Option 2'),
                rx.button('Option 3'),
                variant='outline',
                is_attached=True,
            )
"""


button_state = """class ButtonState(State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
"""
exec(button_state)
button_state_example = """rx.hstack(
    rx.button(
        "Decrement",
        bg="#fef2f2",
        color="#b91c1c",
        border_radius="lg",
        on_click=ButtonState.decrement,
    ),
    rx.heading(ButtonState.count, font_size="2em", padding_x="0.5em"),
    rx.button(
        "Increment",
        bg="#ecfdf5",
        color="#047857",
        border_radius="lg",
        on_click=ButtonState.increment,
    ),
)
"""


button_state_code = f"""
import reflex as rx

{button_state.replace("(State)", "(rx.State)")}

def index():
    return {button_state_example}

app = rx.App()
app.add_page(index)
app.compile()"""

button_state2 = """class ExampleButtonState(State):
    text_value: str = "Random value"
"""
exec(button_state2)

button_state2_render_code = """rx.vstack(
	rx.text(ExampleButtonState.text_value),
        rx.button(
            "Change Value",
            on_click=ExampleButtonState.set_text_value("Modified value"))
    )
"""

button_state2_code = f"""
import reflex as rx

{button_state2.replace("(State)", "(rx.State)")}

def index():
    return {button_state2_render_code}

app = rx.App()
app.add_page(index)
app.compile()"""

def render_button():
    return rx.vstack(
        doctext("A button is a clickable element that is used to trigger an event."),
        docdemo(basic_button),
        doctext(
            "Buttons can range in size and style. You can style it with traditional props or with the color scheme prop for ease of use."
        ),
        docdemo(button_style),
        doctext("Buttons can also have different visual states."),
        docdemo(button_visual_states),
        doctext("You can group buttons together using button group."),
        docdemo(button_group_example),
        doctext(
            "Buttons are use to trigger events using the",
            rx.code("on_click"),
            " event handler. ",
        ),
        docdemo(
            button_state_example,
            state=button_state,
            comp=eval(button_state_example),
            context=True,
        ),
        align_items="start",
    )


iconbutton_example = """rx.icon_button(icon="search")"""


def render_iconbutton():
    return rx.vstack(
        doctext("IconButton display a clickable Icon"),
        docdemo(iconbutton_example),
        doctext(
            "Since IconButton only renders an icon, you must pass the `aria_label` prop, so screen readers can give meaning to the button."
        ),
    )


@docpage()
def button():
    _, output = flexdown.read("docs/library/forms/button.md")
    return rx.box(
        *output,
    )
