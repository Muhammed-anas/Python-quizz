import { useState } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import '../App.css'

function QuizSetup() {
  const location = useLocation()
  const { questionType = 'multiple_choice' } = location.state || {}
  const [questionCount, setQuestionCount] = useState(10)
  const navigate = useNavigate()

  const handleStartQuiz = () => {
    const route = questionType === 'multiple_choice' ? '/multiple-choice-quiz' : '/coding-quiz'
    navigate(route, { state: { questionCount, questionType } })
  }

  return (
    <div className="container">
      <div className="card" style={{ maxWidth: '600px', margin: '2rem auto', textAlign: 'center' }}>
        <button className="btn btn-secondary" onClick={() => navigate('/')} style={{ marginBottom: '2rem' }}>
          ← Back to Home
        </button>

        <h1 style={{ fontSize: '2rem', marginBottom: '1rem', color: '#333' }}>
          {questionType === 'multiple_choice' ? '📝' : '💻'} Quiz Setup
        </h1>

        <p style={{ fontSize: '1.1rem', color: '#666', marginBottom: '2rem' }}>
          Choose how many questions you'd like to answer
        </p>

        <div style={{ marginBottom: '2rem' }}>
          <label style={{ display: 'block', marginBottom: '1rem', fontWeight: '600', color: '#333' }}>
            Number of Questions:
          </label>
          <input
            type="number"
            min="1"
            max="50"
            value={questionCount}
            onChange={(e) => setQuestionCount(Math.max(1, Math.min(50, parseInt(e.target.value) || 1)))}
            style={{
              padding: '0.75rem',
              fontSize: '1.2rem',
              border: '2px solid #e0e0e0',
              borderRadius: '8px',
              width: '150px',
              textAlign: 'center'
            }}
          />
          <div style={{ marginTop: '0.5rem', color: '#666', fontSize: '0.9rem' }}>
            Select between 1 and 50 questions
          </div>
        </div>

        <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
          <button className="btn btn-primary" onClick={handleStartQuiz} style={{ padding: '1rem 2rem', fontSize: '1.1rem' }}>
            Start Quiz 🚀
          </button>
        </div>
      </div>
    </div>
  )
}

export default QuizSetup

