import json
import os

class DocumentationViewController: # This class will control the DocumentationView
    def __init__(self, view): # Accept parent window
        self.view = view # Store the view

    def load_content(self, item): # This method will be called when the user clicks a topic in the table of contents
        topic = item.text().replace(" ", "_")  # Replace spaces with underscores to match filenames
        json_file_path = os.path.join("documentation", f"{topic}.json") # Build the path to the JSON file

        try: # Try to open the JSON file
            with open(json_file_path, 'r') as file: # Open the JSON file
                content_data = json.load(file) # Load the JSON data

            formatted_content = self.format_content(content_data) # Call the format_content method
            self.view.doc_browser.setHtml(formatted_content) # Set the HTML content
        except FileNotFoundError: # Catch file not found errors
            print(f"Documentation file for {topic} not found.")
        except json.JSONDecodeError: # Catch JSON errors
            print(f"Error parsing JSON file for {topic}.") 

    def format_content(self, content_data): # This method will be called when the user clicks a topic in the table of contents
        # Retrieve the title and sections from the JSON data
        title = content_data.get('title', '') # Default to an empty string
        sections = content_data.get('sections', []) # Default to an empty list

        # Build the HTML content with bright white text
        formatted_content = f"<h1 style='font-family: Arial; color: #ffffff;'>{title}</h1>" # Add the title

        # Loop through the sections and add them to the content
        # TODO: Add support for images

        for section in sections: # Loop through the sections
            section_title = section.get('title', '') # Get the section title
            section_content = section.get('content', '') # Get the section content
            formatted_content += f"""
            <h2 style='font-family: Arial; color: #ffffff;'>{section_title}</h2>
            <p style='font-family: Arial; font-size: 14px; line-height: 1.5; color: #ffffff;'>{section_content}</p> 
            """ 

        return formatted_content # Return the formatted content
