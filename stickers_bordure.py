#!/usr/bin/env python

# -----------------------------------------------------------------
# doc

# fill the selection with withe (foreground color)
# pdb.gimp_edit_bucket_fill(current_layer, 0, 0, 100, 255, 0, 0, 0)

# black
# pdb.gimp_edit_bucket_fill(current_layer, 1, 0, 100, 255, 0, 0, 0)

# doc
# -----------------------------------------------------------------

import gimpfu
# import gimp
from gimpfu import pdb


def stickerify_bordure(image, tdrawable, black_grow=3, white_grow=12, shadow=True):
    def duplicate_layer():
        copy = current_layer.copy()
        image.add_layer(copy)
        # copy is added above so we want to go down a bit
        image.active_layer = current_layer
        return copy

    def fill_black():
        pdb.gimp_edit_bucket_fill(current_layer, 1, 0, 100, 255, 0, 0, 0)

    def fill_white():
        pdb.gimp_edit_bucket_fill(current_layer, 0, 0, 100, 255, 0, 0, 0)

    def set_colors():
        pass

    pdb.gimp_context_push()
    pdb.gimp_image_undo_group_start(image)

    pdb.gimp_context_set_foreground((255, 255, 255))
    pdb.gimp_context_set_background((0, 0, 0))

    set_colors()

    current_layer = image.active_layer

    duplicate_layer()

    # alpha to selection
    pdb.gimp_image_select_item(image, 0, current_layer)

    pdb.gimp_selection_grow(image, black_grow)
    fill_black()

    second_layer = duplicate_layer()

    pdb.gimp_selection_grow(image, white_grow)
    fill_white()

    if shadow:
        duplicate_layer()

        fill_black()

        current_layer.translate(8, 8)

        pdb.gimp_selection_all(image)
        pdb.plug_in_gauss(image, current_layer, 20, 20, 0)
        pdb.gimp_layer_set_opacity(current_layer, 70)

    pdb.gimp_image_merge_down(image, second_layer, 0)

    if shadow:
        pdb.gimp_image_merge_down(image, image.active_layer, 0)

    pdb.gimp_image_undo_group_end(image)
    pdb.gimp_context_pop()

    pdb.gimp_displays_flush()


gimpfu.register(
    "python_stickerify_bordure",
    "Put a sticker bordure arround the image",
    "Put a sticker bordure arround the image",
    "Laurent Peuch",
    "Laurent Peuch",
    "2018",
    "<Image>/Filters/Artistic/Stickerify",
    "",
    [
        (gimpfu.PF_ADJUSTMENT, "black_grow", "Size of black bordure", 3, (1, 200, 1, 3, 0, 0)),
        (gimpfu.PF_ADJUSTMENT, "black_grow", "Size of white bordure", 12, (1, 200, 1, 3, 0, 0)),
        (gimpfu.PF_TOGGLE, "shadow", "Display shadow", True),
    ],
    [],
    stickerify_bordure,
)

gimpfu.main()
