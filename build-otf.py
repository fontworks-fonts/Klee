# build-otf.py
from fontmake import __main__
from fontTools.ttLib import TTFont, newTable
from pathlib import Path
import shutil

def GASP_set(font: TTFont):
    if "gasp" not in font:
        font["gasp"] = newTable("gasp")
        font["gasp"].gaspRange = {}
    if font["gasp"].gaspRange != {65535: 0x000A}:
        font["gasp"].gaspRange = {65535: 0x000A}

# Prepare output folder
Path("fonts/otf").mkdir(parents=True, exist_ok=True)

print("[Klee One] Generating OTFs")
for source in Path("sources").glob("*.glyphs"):
    # Generate .glyphs -> master_otf/*.otf
    __main__.main((
        "-g", str(source),
        "--keep-overlaps",  # Use same as TTF to avoid qcurve issues
        "-o", "otf",
    ))

# ----- OTF post-processing -----
for font_path in Path("master_otf").glob("*.otf"):
    modifiedFont = TTFont(font_path)
    font_name = font_path.name[:-4]  # e.g., KleeOne-Regular

    print(f"[{font_name}] Adding stub DSIG (OTF)")
    modifiedFont["DSIG"] = newTable("DSIG")
    modifiedFont["DSIG"].ulVersion = 1
    modifiedFont["DSIG"].usFlag = 0
    modifiedFont["DSIG"].usNumSigs = 0
    modifiedFont["DSIG"].signatureRecords = []

    # Adjust SemiBold weight value (same as TTF script)
    if "SemiBold" in font_name:
        modifiedFont["OS/2"].usWeightClass = 600

    print(f"[{font_name}] Making other changes (OTF)")
    # round PPEM to integer
    modifiedFont["head"].flags |= 1 << 3

    # Add Japanese family/style names (same as TTF script)
    modifiedFont["name"].addMultilingualName(
        {"ja": "クレー One"},
        modifiedFont,
        nameID=1,
        windows=True,
        mac=False,
    )
    if "SemiBold" in font_name:
        modifiedFont["name"].addMultilingualName(
            {"ja": "SemiBold"},
            modifiedFont,
            nameID=2,
            windows=True,
            mac=False,
        )
    elif "Regular" in font_name:
        modifiedFont["name"].addMultilingualName(
            {"ja": "Regular"},
            modifiedFont,
            nameID=2,
            windows=True,
            mac=False,
        )

    # Set GASP for OTF if needed
    GASP_set(modifiedFont)

    # Final save
    out_path = Path("fonts/otf") / font_path.name
    modifiedFont.save(out_path)
    print(f"[{font_name}] Saved to {out_path}")

# ----- Clean up temporary directories -----
if Path("instance_ufo").exists():
    shutil.rmtree("instance_ufo")
if Path("master_ufo").exists():
    shutil.rmtree("master_ufo")
if Path("master_otf").exists():
    shutil.rmtree("master_otf")

print("[Klee One] Done (OTFs)")