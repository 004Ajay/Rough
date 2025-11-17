# IN CONFIG_UTILS.PY
# shortforms: h - height, w - width, bc - barcode
PRINTER_CONFIGS = {
    "ZD421": {
        "7x3": {
            "printer_type": "ZPL", "label_w": 820, "label_h": 354, "label_origin_x": 10, "label_origin_y": 20, "bc_pos_x": 20, "bc_pos_y": 18, "bc_narrow_bar_w": 4, "bc_wide_bar_w": 4, "bc_bar_h": 150,
            "sap_subsap_pos_x": 20, "sap_subsap_pos_y": 200, "sap_subsap_font_h": 28, "sap_subsap_font_w": 28,"sap_subsap_spacing": 35,
            "desc_pos_x": 20, "desc_pos_y": 250, "desc_font_h": 28, "desc_font_w": 28
        },

        "6x4": {
            "printer_type": "ZPL",
            "label_w": 709, "label_h": 472, "label_origin_x": 10, "label_origin_y": 20,
            "bc_pos_x": 30, "bc_pos_y": 18, "bc_narrow_bar_w": 4, "bc_wide_bar_w": 4, "bc_bar_h": 150,
            "sap_subsap_pos_x": 30, "sap_subsap_pos_y": 200, "sap_subsap_font_h": 28, "sap_subsap_font_w": 28, "sap_subsap_spacing": 14,
            "desc1_pos_x": 30, "desc1_pos_y": 250, "desc1_font_h": 28, "desc1_font_w": 28,
            "desc2_pos_x": 30, "desc2_pos_y": 285, "desc2_font_h": 28, "desc2_font_w": 28
        }
    },

    "GT800": {
        "7x3": {
            "printer_type": "EPL", "label_w": 560, "label_h": 240,
            "sap_subsap_pos_x": 20, "sap_subsap_pos_y": 150, "sap_subsap_font": 2, "sap_subsap_spacing": 35,
            "desc_pos_x": 20, "desc_pos_y": 180, "desc_font": 2,
            "barcode_x": 20, "barcode_y": 15, "bc_narrow_bar_w": 2, "bc_wide_bar_w": 5, "barcode_height": 110
        },

        "6x4": {
            "printer_type": "EPL", "label_w": 480, "label_h": 320,
            "sap_subsap_pos_x": 30, "sap_subsap_pos_y": 140, "sap_subsap_font": 3, "sap_subsap_spacing": 12,
            "desc1_pos_x": 30, "desc1_pos_y": 180, "desc1_font": 2,
            "desc2_pos_x": 30, "desc2_pos_y": 215, "desc2_font": 2,
            "barcode_x": 30, "barcode_y": 5, "bc_narrow_bar_w": 2, "bc_wide_bar_w": 5, "barcode_height": 110
        } # check sizes of bc nbw, wbw, height
    },

    "ZD230": {
        "7x3": {
            "printer_type": "ZPL", "label_w": 820, "label_h": 354, "label_origin_x": 10, "label_origin_y": 20,
            "bc_pos_x": 140, "bc_pos_y": 18, "bc_narrow_bar_w": 3, "bc_wide_bar_w": 3, "bc_bar_h": 100,
            "sap_subsap_pos_x": 140, "sap_subsap_pos_y": 130, "sap_subsap_font_h": 20, "sap_subsap_font_w": 20, "sap_subsap_spacing": 35,
            "desc_pos_x": 140, "desc_pos_y": 170, "desc_font_h": 20, "desc_font_w": 20
        },

        "5x2.5": {
            "printer_type": "ZPL", "label_w": 400, "label_h": 200, "label_origin_x": 10, "label_origin_y": 20,
            "bc_pos_x": 12, "bc_pos_y": 7, "bc_narrow_bar_w": 2, "bc_wide_bar_w": 2, "bc_bar_h": 100,
            "sap_subsap_pos_x": 10, "sap_subsap_pos_y": 120, "sap_subsap_font_h": 15, "sap_subsap_font_w": 15, "sap_subsap_spacing": 35,
            "desc_pos_x": 10, "desc_pos_y": 150, "desc_font_h": 13, "desc_font_w": 13
        }
    }
}