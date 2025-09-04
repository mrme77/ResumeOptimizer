from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

# Font handling
def find_font() -> str:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "C:/Windows/Fonts/arialuni.ttf"
    ]
    for path in candidates:
        if Path(path).exists():
            return path
    return None

font_path = find_font()
if font_path:
    pdfmetrics.registerFont(TTFont("CustomUnicode", font_path))
    DEFAULT_FONT = "CustomUnicode"
else:
    DEFAULT_FONT = "Helvetica"
    print("[WARNING] Using Helvetica (limited Unicode support).")

def generate_resume_pdf(text: str, filename: str):
    """Generate styled resume PDF using ReportLab."""
    doc = SimpleDocTemplate(filename, pagesize=LETTER,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)
    story = []
    styles = getSampleStyleSheet()
    for s in styles.byName.values():
        s.fontName = DEFAULT_FONT

    section_header_style = ParagraphStyle(
        "SectionHeader",
        parent=styles["Heading2"],
        fontSize=12,
        textColor=colors.darkblue,
        spaceBefore=12,
        spaceAfter=6,
        fontName=DEFAULT_FONT,
    )

    for line in text.split("\n"):
        if not line.strip():
            story.append(Spacer(1, 10))
        elif line.strip().endswith(":"):
            story.append(Paragraph(line.strip(), section_header_style))
        else:
            story.append(Paragraph(line.strip(), styles["Normal"]))
    doc.build(story)
    return filename
