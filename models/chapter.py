from typing import List, Optional, Union

# Choice class for input stages
class Choice:
    def __init__(self, text: str, next_chapter_id: int): # next_chapter_id is the ID of the chapter to go to
        self.text = text # when the choice is selected
        self.next_chapter_id = next_chapter_id # next_chapter_id is None if the choice is a dead end

# Abstract base class for stages
class Stage:
    def __init__(self, stage_id: int, text: str): # stage_id is the ID of the stage
        self.stage_id = stage_id # text is the text to display when the stage is reached
        self.text = text # next_stage_id is the ID of the next stage to go to when the stage is reached

# Subclass for linear stages
class LinearStage(Stage):
    def __init__(self, stage_id: int, text: str, next_stage_id: int): # next_stage_id is None if the stage is a dead end
        super().__init__(stage_id, text) # next_stage_id is the ID of the next stage to go to when the stage is reached
        self.next_stage_id = next_stage_id # next_stage_id is None if the stage is a dead end

# Subclass for input stages
class InputStage(Stage):
    def __init__(self, stage_id: int, text: str, input_key: Optional[str] = None, # input_key is the key to use to get the user input
                 choices: Optional[List[Choice]] = None, next_stage_id: Optional[int] = None, # choices is a list of choices for the user to select from
                 special_case: Optional[str] = None, special_case_next_chapter_id: Optional[int] = None): # input_key is the key to use to get the user input
        super().__init__(stage_id, text) # input_key is the key to use to get the user input
        self.input_key = input_key # choices is a list of choices for the user to select from
        self.choices = choices or [] # next_stage_id is the ID of the next stage to go to when the stage is reached
        self.next_stage_id = next_stage_id # special_case is a special case for the input stage
        self.special_case = special_case # special_case_next_chapter_id is the ID of the chapter to go to if the special case is met
        self.special_case_next_chapter_id = special_case_next_chapter_id # special_case_next_chapter_id is None if the special case is not met

# Chapter class representing a collection of stages
class Chapter:
    def __init__(self, stages: List[Union[LinearStage, InputStage]]): # stages is a list of stages in the chapter
        self.stages = stages # current_stage_id is the ID of the current stage in the chapter

# Function to parse the JSON data into Chapter object
def parse_chapter(json_data: dict) -> Chapter: # json_data is the JSON data to parse
    stages = [] # stages is a list of stages in the chapter
    for stage_data in json_data['stages']: # current_stage_id is the ID of the current stage in the chapter
        stage_id = stage_data['stage_id'] # stage_id is the ID of the stage
        text = stage_data['text'] # text is the text to display when the stage is reached
        stage_type = stage_data['type'] # stage_type is the type of the stage
        if stage_type == 'Linear': # stage_type is the type of the stage
            next_stage_id = stage_data['next_stage_id'] # next_stage_id is the ID of the next stage to go to when the stage is reached
            stage = LinearStage(stage_id, text, next_stage_id) # next_stage_id is None if the stage is a dead end
        else:  # Input stage
            input_key = stage_data.get('input_key') # input_key is the key to use to get the user input
            next_stage_id = stage_data.get('next_stage_id') # choices is a list of choices for the user to select from
            special_case = stage_data.get('special_case') # next_stage_id is the ID of the next stage to go to when the stage is reached
            special_case_next_chapter_id = stage_data.get('special_case_next_chapter_id') # special_case is a special case for the input stage
            choices_data = stage_data.get('choices', []) # special_case_next_chapter_id is the ID of the chapter to go to if the special case is met
            choices = [Choice(choice['text'], choice['next_chapter_id']) for choice in choices_data] # special_case_next_chapter_id is None if the special case is not met
            stage = InputStage(stage_id, text, input_key, choices, next_stage_id, special_case, # special_case_next_chapter_id is None if the special case is not met
                               special_case_next_chapter_id) # special_case_next_chapter_id is the ID of the chapter to go to if the special case is met
        stages.append(stage) # special_case_next_chapter_id is None if the special case is not met
    return Chapter(stages) # special_case_next_chapter_id is the ID of the chapter to go to if the special case is met
