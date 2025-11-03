import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { getRandomQuestion, checkAnswer } from '../utils/api'
import '../App.css'

function MultipleChoiceQuestion() {
  const [question, setQuestion] = useState(null)
  const [selectedChoice, setSelectedChoice] = useState(null)
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
    setSelectedChoice(null)
    try {
      const data = await getRandomQuestion('multiple_choice')
      setQuestion(data)
    } catch (error) {
      console.error('Error loading question:', error)
      alert('Failed to load question. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async () => {
    if (!selectedChoice) {
      alert('Please select an answer')
      return
    }

    setSubmitting(true)
    try {
      const response = await checkAnswer(question.id, { choice_id: selectedChoice })
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

        <div style={{ marginBottom: '2rem' }}>
          {question.choices && question.choices.map((choice) => (
            <div
              key={choice.id}
              onClick={() => !result && setSelectedChoice(choice.id)}
              style={{
                padding: '1rem',
                marginBottom: '0.75rem',
                border: `2px solid ${selectedChoice === choice.id ? '#667eea' : '#e0e0e0'}`,
                borderRadius: '8px',
                cursor: result ? 'default' : 'pointer',
                background: selectedChoice === choice.id ? '#f0f4ff' : 'white',
                transition: 'all 0.2s',
                opacity: result ? 0.7 : 1
              }}
              onMouseEnter={(e) => {
                if (!result) e.target.style.borderColor = '#667eea'
              }}
              onMouseLeave={(e) => {
                if (!result && selectedChoice !== choice.id) e.target.style.borderColor = '#e0e0e0'
              }}
            >
              {choice.text}
            </div>
          ))}
        </div>

        {result && (
          <div className={`alert ${result.correct ? 'alert-success' : 'alert-error'}`}>
            {result.message}
          </div>
        )}

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button
            className="btn btn-primary"
            onClick={handleSubmit}
            disabled={!selectedChoice || submitting || result}
          >
            {submitting ? 'Checking...' : 'Submit Answer'}
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

export default MultipleChoiceQuestion

