# Ocarina CampusFix
Team members: Matthew Wybranski (lead) and Laurence Orji

### How to run CampusFix:
* Download the ZIP file and extract its contents.
* Open your Python IDE of choice (Visual Studio Code) and open up the extracted project folder in the IDE.
* Create a virtual environment inside that folder using `requirements.txt` to obtain the necessary dependencies.
* Execute the command `streamlit run .\frontend.py` in the IDE terminal.
  * While in the IDE terminal, ensure you are in the folder that contains `frontend.py` before executing the command.
* The app will open in a new tab in your default browser.
* The `admin` page is hidden by default. To open it, add `/admin` to the default URL for the app.

### Features built:
Ocarina CampusFix helps users easily:
* Report issues observed on campus, including functionality for images.
* Look thorugh all public reports lodged by other users.
* Search for specific reports.
* Track and modify the status of a report.
  * Status modification is accessible only to administrators.
* Compare new reports to existing reports before submitting to guard against duplicates.

### Tools and Technologies Used
* Python libraries
  * Streamlit: Frontend design and web server functionality
  * Pillow: Image manipulation
* VS Code Copilot: Minor code suggestions and improvements
* Git: Source control
