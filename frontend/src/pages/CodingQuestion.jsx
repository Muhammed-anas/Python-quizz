import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { getRandomQuestion, checkAnswer } from '../utils/api'
import '../App.css'

function CodingQuestion() {
  const [question, setQuestion] = useState(null)
  const [code, setCode] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(true)
  const [submitting, setSubmitting] = useState(false)
  const navigate = useNavigate()

  useEffect(() => {
    loadQuestion()
  }, [])

  const loadQuestion = async () => {
    setLoading(true)
    setResult(null)
    setCode('')
    try {
      const data = await getRandomQuestion('coding')
      setQuestion(data)
      setCode(data.starter_code || '')
    } catch (error) {
      console.error('Error loading question:', error)
      alert('Failed to load question. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async () => {
    if (!code.trim()) {
      alert('Please write some code')
      return
    }

    setSubmitting(true)
    try {
      const response = await checkAnswer(question.id, { code })
      setResult(response)
    } catch (error) {
      console.error('Error checking answer:', error)
      alert('Failed to check answer. Please try again.')
    } finally {
      setSubmitting(false)
    }
  }

  const getDifficultyClass = (difficulty) => {
    return `difficulty-badge difficulty-${difficulty}`
  }

  if (loading) {
    return (
      <div className="container">
        <div className="loading">Loading question...</div>
      </div>
    )
  }

  if (!question) {
    return (
      <div className="container">
        <div className="card">
          <p>No questions available. Please check the backend.</p>
          <button className="btn btn-secondary" onClick={() => navigate('/')}>Go Home</button>
        </div>
      </div>
    )
  }

  return (
    <div className="container">
      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
          <button className="btn btn-secondary" onClick={() => navigate('/')}>← Back to Home</button>
          <span className={getDifficultyClass(question.difficulty)}>{question.difficulty}</span>
        </div>

        <h2 style={{ fontSize: '1.5rem', marginBottom: '1.5rem', lineHeight: '1.6', color: '#333' }}>
          {question.text}
        </h2>

        {question.test_cases && question.test_cases.length > 0 && (
          <div style={{ marginBottom: '1.5rem', padding: '1rem', background: '#f8f9fa', borderRadius: '8px' }}>
            <h3 style={{ marginBottom: '0.75rem', color: '#333' }}>Test Cases:</h3>
            {question.test_cases.map((testCase, idx) => (
              <div key={idx} style={{ marginBottom: '0.5rem', fontSize: '0.9rem', color: '#666' }}>
                <strong>Input:</strong> <code>{JSON.stringify(testCase.input_data)}</code>
                <br />
                <strong>Expected Output:</strong> <code>{JSON.stringify(testCase.expected_output)}</code>
              </div>
            ))}
          </div>
        )}

        <div style={{ marginBottom: '1.5rem' }}>
          <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: '600', color: '#333' }}>
            Your Code:
          </label>
          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            style={{
              width: '100%',
              minHeight: '300px',
              padding: '1rem',
              fontFamily: "'Fira Code', 'Courier New', monospace",
              fontSize: '0.9rem',
              border: '2px solid #e0e0e0',
              borderRadius: '8px',
              resize: 'vertical',
              lineHeight: '1.5'
            }}
            placeholder="Write your Python code here..."
          />
        </div>

        {result && (
          <div style={{ marginBottom: '1.5rem' }}>
            <div className={`alert ${result.correct ? 'alert-success' : 'alert-error'}`}>
              {result.message}
            </div>
            
            {result.test_results && result.test_results.length > 0 && (
              <div style={{ marginTop: '1rem' }}>
                <h4 style={{ marginBottom: '0.5rem', color: '#333' }}>Test Results:</h4>
                {result.test_results.map((testResult, idx) => (
                  <div
                    key={idx}
                    style={{
                      padding: '0.75rem',
                      marginBottom: '0.5rem',
                      background: testResult.passed ? '#d4edda' : '#f8d7da',
                      border: `1px solid ${testResult.passed ? '#c3e6cb' : '#f5c6cb'}`,
                      borderRadius: '6px',
                      fontSize: '0.9rem'
                    }}
                  >
                    <div style={{ fontWeight: '600', marginBottom: '0.25rem' }}>
                      Test {idx + 1}: {testResult.passed ? '✅ Passed' : '❌ Failed'}
                    </div>
                    {!testResult.passed && (
                      <div style={{ marginTop: '0.5rem', fontSize: '0.85rem' }}>
                        <div><strong>Input:</strong> <code>{JSON.stringify(testResult.input)}</code></div>
                        <div><strong>Expected:</strong> <code>{JSON.stringify(testResult.expected)}</code></div>
                        <div><strong>Got:</strong> <code>{testResult.got !== null ? JSON.stringify(testResult.got) : 'None'}</code></div>
                        {testResult.error && (
                          <div style={{ color: '#721c24', marginTop: '0.25rem' }}>
                            <strong>Error:</strong> {testResult.error}
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button
            className="btn btn-primary"
            onClick={handleSubmit}
            disabled={!code.trim() || submitting}
          >
            {submitting ? 'Running Tests...' : 'Run Tests'}
          </button>
          
          {result && (
            <button className="btn btn-secondary" onClick={loadQuestion}>
              Next Question
            </button>
          )}
        </div>
      </div>
    </div>
  )
}

export default CodingQuestion

