reports = []

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
    "photo": None,
    "status": "Reported",
    "priority": False
}

def create_new_report():
    new_report = report_template.copy()
    return new_report
