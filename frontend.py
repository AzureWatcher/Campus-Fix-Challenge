# streamlit_app.py
import streamlit as st
import PIL
import backend

st.set_page_config(page_title="Campus Fix (LION Code Challenge 2026)", layout="wide")
st.title("Campus Fix (LION Code Challenge 2026) by Laurence Orji and Matthew Wybranski")

st.markdown(
    """
    <div style="margin-top:-8px; margin-bottom:18px;">
      <p style="font-size:18px; color:#6b7280; margin:0; max-width:1200px;">
        Write your report below and submit it to the campus maintenance team. You can also view the reports submitted by other students.
      </p>
      <p style="font-size:18px; color:#6b7280; margin:0; max-width:1200px;">
        To learn more about this project and the code, check out our github <a href="https://github.com/AzureWatcher/Campus-Fix-Challenge" target="_blank">here</a>
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Extract data from backend.py
campus_buildings = backend.campus_buildings
categories = backend.categories
report_template = backend.report_template

def user():
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

      # Placeholder for submitted reports (in a real application, this would be fetched from a database)
      submitted_reports = [
          {
              "title": "Broken Light in Sutherland",
              "description": "The light in the main hallway is flickering.",
              "category": "broken light",
              "building": "Sutherland",
              "specific_location": "Main Hallway",
              "photo": None
          },
          {
              "title": "Leaking Tap in Springhouse",
              "description": "The tap in the bathroom is leaking water.",
              "category": "leaking tap",
              "building": "Springhouse",
              "specific_location": "Bathroom 2",
              "photo": None
          },
          {
              "title": "Leaking Tap in Springhouse",
              "description": "The tap in the bathroom is leaking water.",
              "category": "leaking tap",
              "building": "Springhouse",
              "specific_location": "Bathroom 2",
              "photo": None
          },
          {
              "title": "Leaking Tap in Springhouse",
              "description": "The tap in the bathroom is leaking water.",
              "category": "leaking tap",
              "building": "Springhouse",
              "specific_location": "Bathroom 2",
              "photo": None
          }
      ]

      # Filters
      filter_building = st.selectbox("Filter by Building", ["All"] + campus_buildings)
      filter_category = st.selectbox("Filter by Category", ["All"] + categories)

      filtered_reports = [
          report for report in submitted_reports
          if (filter_building == "All" or report["building"] == filter_building) and
            (filter_category == "All" or report["category"] == filter_category)
      ]

      for report in filtered_reports:
          st.subheader(report["title"])
          st.write(f"**Description:** {report['description']}")
          st.write(f"**Category:** {report['category']}")
          st.write(f"**Building:** {report['building']}")
          st.write(f"**Specific Location:** {report['specific_location']}")
          if report["photo"]:
              image = PIL.Image.open(report["photo"])
              st.image(image, caption="Uploaded Photo", use_column_width=True)
        
def admin():
    st.header("Admin Page")
    st.write("This is the content of the admin page.")

pg1 = st.Page(user, title = "Submit and View Reports", default = True)
pg2 = st.Page(admin, title = "Admin Page")

pg = st.navigation([pg1, pg2], position="hidden")
pg.run()


# # Cache the analysis to avoid rerunning it on every page load
# @st.cache_data
# def load_analysis_results():
#     """Load and cache the analysis results."""
#     return run_analysis()

# # Load results
# with st.spinner("Loading analysis results..."):
#     results = load_analysis_results()

# # Extract results
# working_data = results['working_data']
# museum_ranking = results['museum_ranking']
# top_10_museums = results['top_10_museums']
# cluster_dict = results['cluster_dict']
# clustering_plot = results['clustering_plot']
# correlation_plot = results['correlation_plot']
# least_correlated_museums = results['least_correlated_museums']
# cluster_summary = results['cluster_summary']

# # Create tabs for different views
# tab1, tab2, tab3, tab4, tab5 = st.tabs(
#     ["Top Museums", "Clustering Analysis", "Sentiment Correlation", "Cluster Details", "Raw Data"]
# )

# with tab1:
#     st.header("Top 10 Museums by Weighted Score")
#     st.dataframe(
#         top_10_museums.reset_index(drop=True),
#         use_container_width=True,
#         hide_index=True
#     )
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader("Complete Museum Rankings")
#         st.dataframe(
#             museum_ranking.sort_values('weighted_score', ascending=False).reset_index(drop=True),
#             use_container_width=True,
#             hide_index=True
#         )

# with tab2:
#     st.header("Museum Clustering Visualization")
#     st.markdown("Museums grouped into 4 clusters using K-Means, visualized with PCA dimension reduction.")
#     st.pyplot(clustering_plot, use_container_width=True)
    
#     st.subheader("Cluster Summary Statistics")
#     st.dataframe(cluster_summary, use_container_width=True)

# with tab3:
#     st.header("Sentiment Analysis vs. User Ratings")
#     st.markdown("Correlation between museum average ratings and review sentiment polarity.")
#     st.pyplot(correlation_plot, use_container_width=True)
    
#     st.subheader("Museums with Lowest Sentiment-Rating Alignment")
#     st.markdown("These museums have the biggest discrepancy between their ratings and the sentiment of their reviews.")
#     st.dataframe(
#         least_correlated_museums[['name', 'museum_average_rating', 'average_polarity', 'residuals']].head(10).reset_index(drop=True),
#         use_container_width=True,
#         hide_index=True
#     )

# with tab4:
#     st.header("Cluster Characteristics")
#     st.markdown("Top categories in each cluster:")
    
#     for cluster_id in sorted(cluster_dict.keys()):
#         with st.expander(f"Cluster {cluster_id}", expanded=True):
#             categories = cluster_dict[cluster_id]
#             st.write("Top 10 categories in this cluster:")
#             st.dataframe(
#                 pd.DataFrame({"Category": categories.index, "Count": categories.values}).reset_index(drop=True),
#                 use_container_width=True,
#                 hide_index=True
#             )

# with tab5:
#     st.header("Raw Data Browser")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         show_all_reviews = st.checkbox("Show all review data", value=False)
#         if show_all_reviews:
#             st.subheader("All Reviews with Sentiment Analysis")
#             st.dataframe(
#                 working_data[['name', 'review_text', 'polarity', 'subjectivity', 'museum_average_rating', 'average_polarity']].reset_index(drop=True),
#                 use_container_width=True,
#                 hide_index=True
#             )
    
#     with col2:
#         show_summary = st.checkbox("Show museum summary data", value=False)
#         if show_summary:
#             st.subheader("Museum Summary")
#             st.dataframe(
#                 working_data[['name', 'museum_average_rating', 'average_polarity', 'review_rating']].drop_duplicates(subset=['name']).reset_index(drop=True),
#                 use_container_width=True,
#                 hide_index=True
#             )

# st.success("Analysis loaded successfully! Use the tabs above to explore different views.")
