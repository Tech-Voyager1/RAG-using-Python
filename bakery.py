from fpdf import FPDF

# Create PDF instance
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)  # Use core font to avoid warnings

# Bakery info content
bakery_info = """
Bakery Name: Sweet Treats Bakery

Opening Hours:
- Monday to Friday: 7:00 AM - 8:00 PM
- Saturday & Sunday: 8:00 AM - 9:00 PM

Menu:
- Breakfast (7:00 AM - 11:00 AM): Croissants, Muffins, Pancakes, Bagels, Danish Pastries
- Lunch (11:30 AM - 3:00 PM): Sandwiches, Salads, Quiches, Burgers, Soups
- Evening Snacks (3:30 PM - 7:00 PM): Donuts, Cookies, Pastries, Brownies
- Beverages: Coffee, Tea, Juice, Smoothies (All Day)

Staff Contacts:
- Manager: Alice - 123-456-7890
- Owner: Bob - 987-654-3210
- Bakers: Charlie - 555-555-5555, Diana - 555-555-5556
- Delivery: Evan - 555-555-5557
- Cashier: Fiona - 555-555-5558

Special Notes:
- Custom cakes require 24 hours prior order
- Online orders accepted via website and phone
- Gluten-free and vegan options available
- Catering available for events upon request
"""

# Add content to PDF safely using multi_cell
for line in bakery_info.strip().split("\n"):
    pdf.multi_cell(0, 8, line)

# Save PDF file
file_path = "./Bakery_Info_Sample.pdf"
pdf.output(file_path)
file_path
