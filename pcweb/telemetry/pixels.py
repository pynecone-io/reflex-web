from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import reflex as rx

from pcweb.telemetry import (
    pixels_clearbit,
    pixels_common_room,
    pixels_google,
    pixels_instantly,
    pixels_posthog,
)


def get_pixel_website_trackers() -> list[rx.Component]:
    return list(
        itertools.chain(
            pixels_google.get_pixel_website_trackers(),
            pixels_common_room.get_pixel_website_trackers(),
            pixels_posthog.get_pixel_website_trackers(),
            pixels_clearbit.get_pixel_website_trackers(),
            pixels_instantly.get_pixel_website_trackers(),
        ),
    )
