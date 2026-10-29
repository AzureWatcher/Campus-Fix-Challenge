campus_buildings = [
    "Sutherland", "Springhouse", "Woodland", 
    "Rydal", "New Academic", "Cloverly",
    "Athletic", "Lares"
    ]

categories = [
    "broken light", "leaking tap", "clogged toilet",
    "jammed door", "dead outlet", "missing toilet paper",
    "missing soap", "missing paper towels", "tv/display issue",
    "computer issue", "other" 
]

report_template = {
    "title": "",
    "description": "",
    "category": "",
    "building": "",
    "specific_location": "",
    "photo": ""
}

def create_new_report():
    new_report = report_template.copy()
    new_report["title"] = ""
    new_report["description"] = ""
    new_report["category"] = ""
    new_report["building"] = ""
    new_report["specific_location"] = ""
    new_report["photo"] = ""
    return new_report
