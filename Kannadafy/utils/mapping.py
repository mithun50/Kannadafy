"""Utilities for handling character mappings in Kannadafy."""
import os
import yaml
import json
from typing import List, Dict, Optional

class MappingLoader:
    """Handles loading and validation of character mappings."""

    @staticmethod
    def load_yaml(file_path: str) -> List[str]:
        """Load mapping from YAML file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if isinstance(data, dict) and 'characters' in data:
                return data['characters']
            raise ValueError("YAML file must contain a 'characters' key with list of characters")

    @staticmethod
    def load_json(file_path: str) -> List[str]:
        """Load mapping from JSON file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and 'characters' in data:
                return data['characters']
            raise ValueError("JSON file must contain a list or dict with 'characters' key")

    @staticmethod
    def load_txt(file_path: str) -> List[str]:
        """Load mapping from text file (one character per line)."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]

    @classmethod
    def load(cls, file_path: str) -> List[str]:
        """Load mapping from file based on extension."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Mapping file '{file_path}' not found")

        ext = os.path.splitext(file_path)[1].lower()
        loaders = {
            '.yaml': cls.load_yaml,
            '.yml': cls.load_yaml,
            '.json': cls.load_json,
            '.txt': cls.load_txt
        }

        if ext not in loaders:
            raise ValueError(f"Unsupported file extension: {ext}")

        return loaders[ext](file_path)

class MappingGenerator:
    """Generates mapping template files."""

    @staticmethod
    def create_template(output_file: str, script_type: str, characters: List[str]) -> None:
        """Create a mapping template file."""
        template = {
            'name': f'Custom {script_type.title()} Mapping',
            'description': 'Custom character mapping for Kannadafy',
            'author': 'Your Name',
            'script_type': script_type,
            'characters': characters
        }

        ext = os.path.splitext(output_file)[1].lower()

        with open(output_file, 'w', encoding='utf-8') as f:
            if ext in ['.yaml', '.yml']:
                yaml.safe_dump(template, f, allow_unicode=True, default_flow_style=False)
            elif ext == '.json':
                json.dump(template, f, ensure_ascii=False, indent=2)
            else:
                raise ValueError("Template file must have .yaml, .yml, or .json extension")
