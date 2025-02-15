from flask import Flask, render_template, request, jsonify
from ..detector.ai_detector import AIContentDetector
import os

app = Flask(__name__)
detector = AIContentDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_content():
    content = request.json.get('content')
    if not content:
        return jsonify({
            'error': 'No content provided'
        }), 400

    try:
        # Analyze the content using our detector
        analysis_result = detector.analyze_text(content)
        
        # Format the response with detailed analysis
        response = {
            'ai_probability': analysis_result['ai_probability'],
            'confidence': analysis_result['confidence'],
            'analysis': {
                'statistical_features': {
                    'word_diversity': analysis_result['statistical_features']['unique_words_ratio'],
                    'avg_word_length': analysis_result['statistical_features']['avg_word_length'],
                    'sentence_complexity': analysis_result['statistical_features']['sentence_length_variance'],
                    'punctuation_density': analysis_result['statistical_features']['punctuation_ratio']
                }
            },
            'relationships': detector.analyze_relationships(content, []),
            'interpretation': {
                'risk_level': 'high' if analysis_result['ai_probability'] > 0.7 else 
                             'medium' if analysis_result['ai_probability'] > 0.4 else 'low',
                'confidence_level': 'high' if analysis_result['confidence'] > 0.7 else 
                                  'medium' if analysis_result['confidence'] > 0.4 else 'low'
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            'error': f'Analysis failed: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)