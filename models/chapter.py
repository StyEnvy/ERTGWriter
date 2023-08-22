from typing import List, Optional, Union

# Choice class for input stages
class Choice:
    def __init__(self, text: str, next_chapter_id: Optional[int] = None, next_stage_id: Optional[int] = None):
        self.text = text # text is the text to display for the choice
        self.next_chapter_id = next_chapter_id # next_chapter_id is the ID of the next chapter to go to when the choice is selected
        self.next_stage_id = next_stage_id # next_stage_id is the ID of the next stage to go to when the choice is selected

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
def parse_chapter(json_data: dict) -> Chapter:
    stages = []
    for stage_data in json_data['stages']:
        stage_id = stage_data['stage_id']
        text = stage_data['text']
        stage_type = stage_data['type']
        if stage_type == 'Linear':
            next_stage_id = stage_data['next_stage_id']
            stage = LinearStage(stage_id, text, next_stage_id)
        else:  # Input stage
            input_key = stage_data.get('input_key')
            next_stage_id = stage_data.get('next_stage_id')
            special_case = stage_data.get('special_case')
            special_case_next_chapter_id = stage_data.get('special_case_next_chapter_id')
            choices_data = stage_data.get('choices', [])
            choices = [Choice(choice['text'], choice.get('next_chapter_id'), choice.get('next_stage_id')) for choice in choices_data]
            stage = InputStage(stage_id, text, input_key, choices, next_stage_id, special_case, special_case_next_chapter_id)
        stages.append(stage)
    return Chapter(stages)
