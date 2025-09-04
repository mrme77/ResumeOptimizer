from pdf_utils import parse_pdf_to_text
from llm_utils import rewrite_resume
from report_utils import generate_resume_pdf

SAMPLE_RESUME_TEXT = """
Jane Doe
23 Somewhere Street Anytown, CA 12345
(310) 217-9366 ssmith@email.com
Citizenship: USA Veterans Pref.: N/A

Profile: Highly-organized and detail-oriented Executive Assistant with over 15 years’
experience providing thorough and skillful administrative support to senior executives.

Employment History:

J.W. Associates, LLC
Executive Assistant 4/1996 - Present
Prepare proposals, manuscripts and reports; draft executive level documents and key
correspondence. Administer telecommunications, travel and calendars for three executives.
Lead support staff and comprehensive training.
- Coordinate projects and events exercising ability to improvise, improve procedures,
and meet demanding deadlines.
- Plan and coordinate corporate luncheons, and develop presentations for related on-
site and off-site meetings.
- Manage capital purchases, direct vendor relations, generate and maintain equipment
tracking records.

Pulsar Distribution Services
Executive Assistant 5/1991 - 4/1996

Supported senior-level executives at this $12 billion distribution company. Organized office
and designed systems to maximize operations. Arranged and maintained sensitive
documents in compliance with security procedures.
- Saved the organization $100,000 in travel expenses after implementing a detailed
travel program that placed limitations on air, hotel and rental car accommodations.
- Played a key role in the development of the company’s expense policies and
procedures.

Computer Skills
Microsoft Office Suite, Adobe Illustrator, Photoshop, Outlook Express, scanning technology,
HTML, website development, advanced Internet research.

Education
Lakeview College, Lakeview, NY
Bachelor of Science, Business Administration, 1990
"""

def process_resume(pdf_file):
    """Pipeline: parse → rewrite → generate."""
    if pdf_file is None:
        return None
    raw_text = parse_pdf_to_text(pdf_file)
    rewritten = rewrite_resume(raw_text, SAMPLE_RESUME_TEXT)
    if not rewritten:
        return None
    output_file = "rewritten_resume.pdf"
    generate_resume_pdf(rewritten, output_file)
    return output_file
