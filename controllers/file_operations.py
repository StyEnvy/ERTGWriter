import json
from models.chapter import LinearStage, InputStage, Choice, Chapter

class FileOperations:
    def load_chapter_from_file(self, file_path: str) -> dict:
        with open(file_path, 'r') as file:
            return json.load(file)

    def save_to_file(self, stage_editor_container, file_path: str):
        stages = []
        for index in range(0, stage_editor_container.count(), 2):  # Step by 2 to skip separators
            stage_editor_panel = stage_editor_container.itemAt(index).widget()
            stage = stage_editor_panel.build_stage()
            stages.append(stage)
        chapter_data = {'stages': stages}
        with open(file_path, 'w') as file:
            json.dump(chapter_data, file, indent=4)

    def parse_chapter(self, json_data: dict) -> Chapter:
        stages = []
        for stage_data in json_data['stages']:
            stage_id = stage_data['id']
            text = stage_data['text']
            properties = stage_data['properties']
            stage_type = properties['type']
            next_stage_id = properties.get('next_stage_id')
            if stage_type == 'linear':
                stage = LinearStage(stage_id, text, next_stage_id)
            else:  # Input stage
                input_key = properties.get('input_key')  # Get input_key if it exists, otherwise None
                special_case = properties.get('special_case')
                special_case_next_chapter_id = properties.get('special_case_next_chapter_id')
                choices_data = properties.get('choices', [])
                choices = [Choice(choice['text'], choice['next_chapter_id']) for choice in choices_data]
                stage = InputStage(stage_id, text, input_key, choices, next_stage_id, special_case,
                                   special_case_next_chapter_id)

            stages.append(stage)
        return Chapter(stages)
