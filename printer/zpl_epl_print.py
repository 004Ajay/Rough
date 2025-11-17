def zpl_printer(z, asset, sub_asset, barcode, description, printer_name=None, print_count=1):

    zpl_cmd = (
    "^XA\n"                                                              # XA = Start Format, means starting a new ZPL label format
    f"^PW{label_width}\n"                                                # PW = Print Width, max width of the printable area (in dots) [827 dots = 7 cm at 300 DPI (7 / 2.54 * 300)]
    f"^LL{label_height}\n"                                               # LL = Label Length in dots [354 dots = 3 cm at 300 DPI]
    f"^LH{label_origin_x},{label_origin_y}\n"                            # LH = Label Home (origin point), (0,0) = (x=0, y=0) default top-left corner of the label
    f"^FO0,0^FS\n"                                                       # FO0,0 = Field Origin at (x=0, y=0) ; FS = Field Separator (Ends the current field/command)
    f"^FO{barcode_pos_x},{barcode_pos_y}\n"                              # FO = Field Origin [Position the next item at (x, y) (offset from the top-left corner)]
    f"^BY{bc_narrow_bar_width},{bc_wide_bar_width},{bc_bar_height}\n"    # BY = Barcode Field Default settings ; 4 = Module width (narrow bar width in dots) ; 4 = Wide bar to narrow bar ratio (only used in some barcodes) ; 150 = Height of the barcode in dots
    f"^BCN,{bc_bar_height},N,N,N\n"                                      # BC = Code128, N = Normal orientation, 150 = Barcode height, N = Do not print human-readable text, N = No interpretation line (used for security), N = No check digit (used in some symbologies)
    f"^FD{barcode}^FS\n"                                                 # FD = Field Data, FS = End field
    f"^FO{sap_subsap_pos_x},{sap_subsap_pos_y}\n"                        # FO = Field Origin, Position next field at (x, y) i.e, SAP/Sub SAP text position
    f"^A0N,{sap_subsap_font_height},{sap_subsap_font_width}\n"           # A0 = Use Font 0 (default font, monospaced sans-serif) ; N = Normal orientation ; (Font height, Font width)
    f"^FDSAP:{asset}{' ' * sap_subsap_spacing}Sub SAP:{sub_asset}^FS\n"  # FD = Field Data, FS = End field
    f"^FO{desc_pos_x},{desc_pos_y}\n"                                    # FO = Field Origin, Start new field at (x, y) i.e, Description text position
    f"^A0N,{desc_font_height},{desc_font_width}\n"                       # A0 = Use Font 0 (default font, monospaced sans-serif) ; N = Normal orientation ; (Font height, Font width)
    f"^FD{description}^FS\n"                                             # FD = Field Data, FS = End field
    f"^PQ{print_count}\n"                                                # PQ = Print Quantity
    "^XZ"                                                                # XZ = End Format
)

    logger.info(f"Sending EPL to printer 'zd421_zpl_printer'\nZPL Code:\n'''\n{zpl_cmd}\n'''")

    z.output(zpl_cmd)

def epl_printer(z, asset, sub_asset, barcode, description=None, SsSfs=2, Dfs=2, nbw=2, wbw=5, bh=110, printer_name=None, print_count=1, desc_char_count=None): ...
    """
    Make and Send ZPL Command to Zebra GT800 Printer

    z,
    asset -> SAP code, eg: 1234
    sub_asset -> Sub SAP Code, eg: 5 
    barcode -> combination of asset and sub_asset, delim pipe (|), eg: 1234|5
    description -> 
    
    SsSfs -> SAP and Sub_SAP font size
    Dfs -> Description font size

    nbw -> narrow bar width 
    wbw -> wide bar width
    bh -> bar height

    desc_char_count -> length of description (in chars)
    """
    if printer_name is not None:
        z.setqueue(printer_name)

    desc1 = desc2 = None
        
    try:
        limit = 30
        pattern = r"[^A-Za-z0-9]"      # any special character

        matches = list(re.finditer(pattern, description[:limit])) # all special characters before "limit"

        if matches:
            split_pos = matches[-1].start()  # last special char before limit
        else:
            split_pos = limit                # fallback

        desc1 = description[:split_pos]
        desc2 = description[split_pos+1:]
    except Exception as e:
        print(f"error: {e}")
        logger.info(f"error: {e}")
    
    logger.info(f"""Print Info:\nasset: {asset}\nsub_asset: {sub_asset}\ndescription: {description}
                \ndesc1: {desc1}\ndesc2: {desc2}\nprinter_name: {printer_name}\nprint_count: {print_count}\ndesc_char_count: {desc_char_count}\n""")
    logger.info(f"Barcode printer controls:\nSsSfs: {SsSfs}\nDfs: {Dfs}\nnbw: {nbw}\nwbw: {wbw}\nbh: {bh}\n")

    epl_cmd = ( # the non-tunable areas were done after checking the printing of barcodes 
        "N\n" # Clear image buffer (start a new label)
        "q480\n" # Label width (560)
        "Q320,24\n" # Label height (240) and gap (24 dots)
        f"A30,140,0,{SsSfs},1,1,N,\"SAP: {asset}{' ' * 12}Sub SAP: {sub_asset}\"\n" # Text at X=5, Y=140, rotation=0°, font=4, x-scale=1, y-scale=1, normal print, text="SAP: ... Sub SAP: ..."
        f"A30,180,0,{Dfs},1,1,N,\"{desc1}\"\n" # Text at X=5, Y=180, rotation=0°, font=4, x-scale=1, y-scale=1, normal print, text=description
        f"A30,215,0,{Dfs},1,1,N,\"{desc2}\"\n" # Text at X=5, Y=180, rotation=0°, font=4, x-scale=1, y-scale=1, normal print, text=description
        f"B30,5,0,3,{nbw},{wbw},{bh},N,\"{barcode}\"\n" # Barcode at X=20, Y=15, rotation=0°, Type=3 (Code128), narrow bar width=3 dots, wide bar width=6 dots, height=100 dots, human-readable text=N (No), data=barcode
        f"P{print_count}\n" # Print 1 label ; controlled by user in GUI; default 1
    )

    logger.info(f"Sending EPL to printer 'gt800_medium_epl_printer'\nEPL Code:\n'''\n{epl_cmd}\n'''")

    z.output(epl_cmd)    
