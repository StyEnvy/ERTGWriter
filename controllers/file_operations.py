import json
from models.chapter import LinearStage, InputStage, Choice, Chapter

class FileOperations:
    def load_chapter_from_file(self, file_path: str) -> dict: # Function to load a chapter from a file
        with open(file_path, 'r') as file: # Open the file
            return json.load(file) # Load the JSON data

    def save_to_file(self, stage_editor_container, file_path: str): # Function to save the current chapter to a file
        stages = [] # stages is a list of stages in the chapter
        for index in range(0, stage_editor_container.count(), 2):  # Step by 2 to skip separators
            stage_editor_panel = stage_editor_container.itemAt(index).widget() # Get the stage editor panel
            stage_data = stage_editor_panel.build_stage() # Build the stage data
            stages.append(stage_data) # Add the stage to the list

        chapter_data = {'stages': stages} # Create the chapter data
        with open(file_path, 'w') as file: # Open the file
            json.dump(chapter_data, file, indent=4) # Dump the JSON data to the file

    def parse_chapter(self, json_data: dict) -> Chapter: # Function to parse the JSON data into Chapter object
        stages = [] # stages is a list of stages in the chapter
        for stage_data in json_data['stages']: # current_stage_id is the ID of the current stage in the chapter
            stage_id = stage_data['id'] # stage_id is the ID of the stage
            text = stage_data['text'] # text is the text to display when the stage is reached
            properties = stage_data['properties'] # stage_type is the type of the stage
            stage_type = properties['type'] # stage_type is the type of the stage
            next_stage_id = properties.get('next_stage_id') # next_stage_id is the ID of the next stage to go to when the stage is reached
            if stage_type == 'linear': # stage_type is the type of the stage
                stage = LinearStage(stage_id, text, next_stage_id) # next_stage_id is None if the stage is a dead end
            else:  # Input stage
                input_key = properties.get('input_key')  # Get input_key if it exists, otherwise None
                special_case = properties.get('special_case') # Get special_case if it exists, otherwise None
                special_case_next_chapter_id = properties.get('special_case_next_chapter_id') # Get special_case_next_chapter_id if it exists, otherwise None
                choices_data = properties.get('choices', []) # Get choices_data if it exists, otherwise []
                choices = [Choice(choice['text'], choice.get('next_chapter_id'), choice.get('next_stage_id')) for choice in choices_data] # Get choices if it exists, otherwise []
                stage = InputStage(stage_id, text, input_key, choices, next_stage_id, special_case, # special_case_next_chapter_id is None if the special case is not met
                                   special_case_next_chapter_id) # special_case_next_chapter_id is the ID of the chapter to go to if the special case is met

            stages.append(stage) # special_case_next_chapter_id is None if the special case is not met
        return Chapter(stages) # special_case_next_chapter_id is the ID of the chapter to go to if the special case is met
    
    def validate_stages(self, stage_editor_container):
        for index in range(0, stage_editor_container.count(), 2):  # Step by 2 to skip separators
            stage_editor_panel = stage_editor_container.itemAt(index).widget()  # Get the stage editor panel
            stage_id = stage_editor_panel.stage_id_edit.text().strip()  # Get the stage ID as a string
            if not stage_id or not stage_id.isdigit():
                return False
        return True
