from typing import List, Optional, Union

# Choice class for input stages
class Choice:
    def __init__(self, text: str, next_chapter_id: int):
        self.text = text
        self.next_chapter_id = next_chapter_id

# Abstract base class for stages
class Stage:
    def __init__(self, stage_id: int, text: str):
        self.stage_id = stage_id
        self.text = text

# Subclass for linear stages
class LinearStage(Stage):
    def __init__(self, stage_id: int, text: str, next_stage_id: int):
        super().__init__(stage_id, text)
        self.next_stage_id = next_stage_id

# Subclass for input stages
class InputStage(Stage):
    def __init__(self, stage_id: int, text: str, input_key: Optional[str] = None,
                 choices: Optional[List[Choice]] = None, next_stage_id: Optional[int] = None,
                 special_case: Optional[str] = None, special_case_next_chapter_id: Optional[int] = None):
        super().__init__(stage_id, text)
        self.input_key = input_key
        self.choices = choices or []
        self.next_stage_id = next_stage_id
        self.special_case = special_case
        self.special_case_next_chapter_id = special_case_next_chapter_id

# Chapter class representing a collection of stages
class Chapter:
    def __init__(self, stages: List[Union[LinearStage, InputStage]]):
        self.stages = stages

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
            choices = [Choice(choice['text'], choice['next_chapter_id']) for choice in choices_data]
            stage = InputStage(stage_id, text, input_key, choices, next_stage_id, special_case,
                               special_case_next_chapter_id)
        stages.append(stage)
    return Chapter(stages)
