# streamlit_app.py
import streamlit as st
import PIL
from PIL import Image
import backend

st.set_page_config(page_title="Campus Fix (LION Code Challenge 2026)", layout="wide")
st.title("Campus Fix (LION Code Challenge 2026) by Laurence Orji and Matthew Wybranski")

# Pop up dialog to show duplicate reports
@st.dialog("Review Similar Reports", dismissible=False)
def show_duplicate_warning(matches):
    st.warning("We found existing reports matching this category and building!")
    
    # Show the matching reports
    with st.container(height=450):
        for report in matches:
            current_status = report['status']
            st.subheader(report["title"])
            st.write(f"**Description:** {report['description']}")
            st.write(f"**Category:** {report['category']}")
            st.write(f"**Building:** {report['building']}")
            st.write(f"**Specific Location:** {report['specific_location']}")
            st.write(f"**Status:** {current_status}")
            if report["photo"]:
                image = PIL.Image.open(report["photo"])
                st.image(image, caption="Uploaded Photo")
    
    st.error("Does this report look similar to the one you want to submit?")
    
    if st.button("Yes, it does."):
        for report in matches:
            report["priority"] = True
        st.rerun()
    if st.button("Go Back"):
        st.rerun()

# Extract data from backend.py
campus_buildings = backend.campus_buildings
categories = backend.categories
report_template = backend.report_template
reports_match = []

def user():
    st.markdown(
    """
    <div style="margin-top:-8px; margin-bottom:18px;">
      <p style="font-size:18px; color:#6b7280; margin:0; max-width:1200px;">
        Write your report below and submit it to the campus maintenance team. You can also view the reports submitted by other students, faculty, and staff.
      </p>
      <p style="font-size:18px; color:#6b7280; margin:0; max-width:1200px;">
        To learn more about this project and the code, check out our github <a href="https://github.com/AzureWatcher/Campus-Fix-Challenge" target="_blank">here</a>
      </p>
    </div>
    """,
    unsafe_allow_html=True,
    )
    
    col1, col2 = st.columns(2)

    # with st.container(border=True, width=800, height="content"):
    with col1:
        st.header("Submit a New Report")
        with st.form(key="report_form"):
            title = st.text_input("Title", max_chars=100)
            description = st.text_area("Description", max_chars=500)
            category = st.selectbox("Category", categories)
            building = st.selectbox("Building", campus_buildings)
            specific_location = st.text_input("Specific Location (e.g., Room 101)")
            photo = st.file_uploader("Upload a Photo (optional)", type=["jpg", "jpeg", "png"])

            submit_button = st.form_submit_button(label="Submit Report")

        if submit_button:
            new_report = backend.create_new_report()
            new_report["title"] = title
            new_report["description"] = description
            new_report["category"] = category
            new_report["building"] = building
            new_report["specific_location"] = specific_location
            new_report["photo"] = photo

            if not title or not description or not category or not building or not specific_location:
                st.error("Please fill in all required fields.")
            else:
                for report in backend.reports:
                    if (report["category"] == category and report["building"] == building and report["specific_location"][-3:] == specific_location[-3:]):
                        reports_match.append(report)
                if reports_match:
                    show_duplicate_warning(reports_match)
                else:
                    st.success("Report submitted successfully!")
                    backend.reports.append(new_report)
                    
    # with st.container(border=True, width="content", height="content"):
    with col2:
        st.header("View Submitted Reports")
        st.markdown(
            """
            <div style="margin-top:-8px; margin-bottom:18px;">
                <p style="font-size:18px; color:#6b7280; margin:0; max-width:1200px;">
                Below are the reports submitted by other students. You can filter them by building and category.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Filters
        filter_building = st.selectbox("Filter by Building", ["All"] + campus_buildings)
        filter_category = st.selectbox("Filter by Category", ["All"] + categories)

        filtered_reports = [
            report for report in backend.reports
            if (filter_building == "All" or report["building"] == filter_building) and
                (filter_category == "All" or report["category"] == filter_category)
        ]
        
        with st.container(height=450):
            for report in filtered_reports:
                current_status = report['status']
                st.subheader(report["title"])
                st.write(f"**Description:** {report['description']}")
                st.write(f"**Category:** {report['category']}")
                st.write(f"**Building:** {report['building']}")
                st.write(f"**Specific Location:** {report['specific_location']}")
                st.write(f"**Status:** {current_status}")
                if report["photo"]:
                    image = PIL.Image.open(report["photo"])
                    st.image(image, caption="Uploaded Photo")
                    
            
def admin():
    st.markdown(
    """
    <div style="margin-top:-8px; margin-bottom:18px;">
      <p style="font-size:18px; color:#6b7280; margin:0; max-width:1200px;">
        You can browse and filter the reports submitted. You can also edit the status of reports. <strong><u>Users will be able to see your status changes once submitted.</u></strong>
      </p>
      <p style="font-size:18px; color:#6b7280; margin:0; max-width:1200px;">
        To learn more about this project and the code, check out our github <a href="https://github.com/AzureWatcher/Campus-Fix-Challenge" target="_blank">here</a>
      </p>
    </div>
    """,
    unsafe_allow_html=True,
    )
    
    st.header("View Submitted Reports")
    st.markdown(
        """
        <div style="margin-top:-8px; margin-bottom:18px;">
        <p style="font-size:18px; color:#6b7280; margin:0; max-width:1200px;">
            Below are the reports submitted by other students. You can filter them by building and category.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
        )
    
    # Filters
    filter_building = st.selectbox("Filter by Building", ["All"] + campus_buildings)
    filter_category = st.selectbox("Filter by Category", ["All"] + categories)
    
    filtered_reports = [
        report for report in backend.reports if (filter_building == "All" or report["building"] == filter_building) and
                (filter_category == "All" or report["category"] == filter_category)
                ]
    
    for report in filtered_reports:
        current_status = report['status']
        st.subheader(report["title"])
        st.write(f"**Description:** {report['description']}")
        st.write(f"**Category:** {report['category']}")
        st.write(f"**Building:** {report['building']}")
        st.write(f"**Specific Location:** {report['specific_location']}")
        st.write(f"**Status:** {current_status}")
        if report.get("priority") == True:
            st.warning("This report has been flagged by more than one user. Please review and attend to this issue ASAP.")

        statuses = ["Reported", "In Progress", "Resolved"]
        update_status_popover = st.popover(label="Update Status")
        with update_status_popover:
            select_key = f"{report['title']}_selectbox"
            validation_button_key = f"{report['title']}_validbutton"
            original_status = report["status"]
            new_status = st.selectbox("Status", statuses, key=select_key)
            validation_button = st.button(label="✅", key=validation_button_key)
            if validation_button:
                report["status"] = new_status

        if report.get("status") == "Resolved":
            report["priority"] = False
        
        if validation_button:
            st.success(f"Status successfully changed to {new_status}. Reload page to see changes.")

        if report["photo"]:
            expander_key = f"{report['title']}_img_expander"
            img_expander = st.expander(label="Show Image", key=expander_key)
            with img_expander:
                report_image = Image.open(report["photo"])
                # show_img_button_key = f"{report['photo']}_show_img_button"
                # show_img_button = st.button(label="Show Image", key=show_img_button_key)
                st.image(report_image, caption="Uploaded Photo")

pg1 = st.Page(user, title = "Submit and View Reports", default = True)
pg2 = st.Page(admin, title = "Admin Page")

pg = st.navigation([pg1, pg2], position="hidden")
pg.run()