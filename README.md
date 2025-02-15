# AI Feedback Loop Detection & Mitigation

> ⚠️ **WARNING**: This is a test project and is not intended for production use. It serves as a proof of concept for AI content detection and feedback loop analysis.

This tool analyzes and visualizes AI-generated content feedback loops in training data, helping to identify and mitigate potential quality degradation in AI training datasets.

## Features
- AI-generated content detection using transformer models
- Statistical text analysis and feature extraction
- Content relationship tracking and visualization
- Risk level assessment and confidence scoring
- Web-based interface for analysis

## Quick Start

1. Clone the repository:
```bash
git clone [your-repo-url]
cd AiLoopDetect
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create necessary Python package files:
```bash
touch src/__init__.py src/detector/__init__.py src/web/__init__.py
```

5. Run the application:
```bash
PYTHONPATH=$PYTHONPATH:. python -m src.web.app
```

6. Open http://localhost:5000 in your browser

## Usage Examples

### Web Interface

1. Navigate to http://localhost:5000
2. Paste your text in the analysis box
3. Click "Analyze"
4. View the results:
   - AI Generation Probability
   - Confidence Score
   - Risk Level Assessment
   - Statistical Text Features

### Example Results

The analyzer provides detailed metrics:

```json
{
    "ai_probability": 0.85,
    "confidence": 0.92,
    "analysis": {
        "statistical_features": {
            "word_diversity": 0.45,
            "avg_word_length": 5.2,
            "sentence_complexity": 12.8,
            "punctuation_density": 0.06
        }
    },
    "interpretation": {
        "risk_level": "high",
        "confidence_level": "high"
    }
}
```

### Understanding the Results

- **AI Probability**: Likelihood that the text is AI-generated (0-1)
- **Confidence**: How confident the model is in its prediction (0-1)
- **Risk Level**: 
  - High (>0.7): Strong indication of AI generation
  - Medium (0.4-0.7): Possible AI involvement
  - Low (<0.4): Likely human-generated
- **Statistical Features**:
  - Word Diversity: Ratio of unique words to total words
  - Average Word Length: Mean length of words
  - Sentence Complexity: Variance in sentence lengths
  - Punctuation Density: Ratio of punctuation marks to text length

## Project Structure
```
AiLoopDetect/
├── README.md
├── requirements.txt
├── src/
│   ├── detector/
│   │   ├── __init__.py
│   │   └── ai_detector.py
│   └── web/
│       ├── __init__.py
│       ├── app.py
│       └── templates/
│           └── index.html
```

## License
MIT

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.