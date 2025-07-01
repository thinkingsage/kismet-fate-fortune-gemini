"""Tests for fortune generation."""
import pytest
from unittest.mock import Mock, patch
from kismet_fortune.fortune import FortuneGenerator


def test_fortune_generator_requires_api_key():
    """Test that FortuneGenerator requires an API key."""
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(ValueError, match="GEMINI_API_KEY environment variable not set"):
            FortuneGenerator()


def test_fortune_generator_with_api_key():
    """Test that FortuneGenerator initializes with API key."""
    with patch.dict('os.environ', {'GEMINI_API_KEY': 'test-key'}):
        generator = FortuneGenerator()
        assert generator.api_key == 'test-key'


@patch('kismet_fortune.fortune.genai.Client')
def test_generate_fortune(mock_client):
    """Test fortune generation."""
    mock_message = Mock()
    mock_message.text = "Test fortune"
    mock_client.return_value.models.generate_content_stream.return_value = [mock_message]
    
    with patch.dict('os.environ', {'GEMINI_API_KEY': 'test-key'}):
        generator = FortuneGenerator()
        result = generator.generate("test prompt")
        assert result == "Test fortune"