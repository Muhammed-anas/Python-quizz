import { useState, useEffect } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import { getRandomQuestions, checkAnswer } from '../utils/api'
import '../App.css'

function MultipleChoiceQuiz() {
  const location = useLocation()
  const { questionCount = 10 } = location.state || {}
  
  const [questions, setQuestions] = useState([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [selectedChoices, setSelectedChoices] = useState({})
  const [answers, setAnswers] = useState({}) // Store if each answer is correct
  const [score, setScore] = useState(0)
  const [result, setResult] = useState(null)
  const [submitting, setSubmitting] = useState(false)
  const [quizStarted, setQuizStarted] = useState(false)
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  useEffect(() => {
    if (!quizStarted) {
      loadQuestions()
    }
  }, [])

  useEffect(() => {
    // Calculate score when answers change
    const correctCount = Object.values(answers).filter(Boolean).length
    setScore(correctCount)
  }, [answers])

  const loadQuestions = async () => {
    setLoading(true)
    try {
      const data = await getRandomQuestions('multiple_choice', questionCount)
      setQuestions(data)
      setQuizStarted(true)
      setSelectedChoices({})
      setAnswers({})
    } catch (error) {
      console.error('Error loading questions:', error)
      alert('Failed to load questions. Please try again.')
      navigate('/')
    } finally {
      setLoading(false)
    }
  }

  const handleSelectChoice = (choiceId) => {
    if (!result) {
      setSelectedChoices({
        ...selectedChoices,
        [currentIndex]: choiceId
      })
    }
  }

  const handleSubmit = async () => {
    if (!selectedChoices[currentIndex]) {
      alert('Please select an answer')
      return
    }

    setSubmitting(true)
    try {
      const question = questions[currentIndex]
      const response = await checkAnswer(question.id, { 
        choice_id: selectedChoices[currentIndex] 
      })
      
      setResult(response)
      setAnswers({
        ...answers,
        [currentIndex]: response.correct
      })
    } catch (error) {
      console.error('Error checking answer:', error)
      alert('Failed to check answer. Please try again.')
    } finally {
      setSubmitting(false)
    }
  }

  const handleNext = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(currentIndex + 1)
      setResult(null)
    } else {
      // Quiz completed
      handleFinish()
    }
  }

  const handleFinish = () => {
    navigate('/quiz-result', {
      state: {
        score,
        totalQuestions: questions.length,
        questionType: 'multiple_choice'
      }
    })
  }

  const getDifficultyClass = (difficulty) => {
    return `difficulty-badge difficulty-${difficulty}`
  }

  if (loading || !quizStarted) {
    return (
      <div className="container">
        <div className="loading">Loading questions...</div>
      </div>
    )
  }

  if (questions.length === 0) {
    return (
      <div className="container">
        <div className="card">
          <p>No questions available. Please check the backend.</p>
          <button className="btn btn-secondary" onClick={() => navigate('/')}>Go Home</button>
        </div>
      </div>
    )
  }

  const currentQuestion = questions[currentIndex]
  const progress = ((currentIndex + 1) / questions.length) * 100

  return (
    <div className="container">
      <div className="card">
        {/* Header with progress */}
        <div style={{ marginBottom: '2rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
            <button className="btn btn-secondary" onClick={() => navigate('/')}>← Back to Home</button>
            <div style={{ textAlign: 'center' }}>
              <div style={{ fontSize: '1.2rem', fontWeight: '600', color: '#333', marginBottom: '0.25rem' }}>
                Question {currentIndex + 1} of {questions.length}
              </div>
              <div style={{ fontSize: '1rem', color: '#667eea', fontWeight: '600' }}>
                Score: {score} / {questions.length}
              </div>
            </div>
            <span className={getDifficultyClass(currentQuestion.difficulty)}>
              {currentQuestion.difficulty}
            </span>
          </div>
          
          {/* Progress bar */}
          <div style={{
            width: '100%',
            height: '8px',
            background: '#e0e0e0',
            borderRadius: '4px',
            overflow: 'hidden'
          }}>
            <div style={{
              width: `${progress}%`,
              height: '100%',
              background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
              transition: 'width 0.3s ease'
            }} />
          </div>
        </div>

        {/* Question */}
        <h2 style={{ fontSize: '1.5rem', marginBottom: '1.5rem', lineHeight: '1.6', color: '#333' }}>
          {currentQuestion.text}
        </h2>

        {/* Choices */}
        <div style={{ marginBottom: '2rem' }}>
          {currentQuestion.choices && currentQuestion.choices.map((choice) => (
            <div
              key={choice.id}
              onClick={() => handleSelectChoice(choice.id)}
              style={{
                padding: '1rem',
                marginBottom: '0.75rem',
                border: `2px solid ${
                  selectedChoices[currentIndex] === choice.id 
                    ? '#667eea' 
                    : result && answers[currentIndex] && selectedChoices[currentIndex] === choice.id
                    ? '#28a745'
                    : result && !answers[currentIndex] && selectedChoices[currentIndex] === choice.id
                    ? '#dc3545'
                    : '#e0e0e0'
                }`,
                borderRadius: '8px',
                cursor: result ? 'default' : 'pointer',
                background: selectedChoices[currentIndex] === choice.id 
                  ? result && answers[currentIndex]
                    ? '#d4edda'
                    : result && !answers[currentIndex]
                    ? '#f8d7da'
                    : '#f0f4ff'
                  : 'white',
                transition: 'all 0.2s',
                opacity: result ? 0.8 : 1
              }}
              onMouseEnter={(e) => {
                if (!result && selectedChoices[currentIndex] !== choice.id) {
                  e.target.style.borderColor = '#667eea'
                }
              }}
              onMouseLeave={(e) => {
                if (!result && selectedChoices[currentIndex] !== choice.id) {
                  e.target.style.borderColor = '#e0e0e0'
                }
              }}
            >
              {choice.text}
            </div>
          ))}
        </div>

        {/* Result message */}
        {result && (
          <div className={`alert ${result.correct ? 'alert-success' : 'alert-error'}`} style={{ marginBottom: '1rem' }}>
            {result.message}
            {/* Show correct answer(s) when the user failed */}
            {!result.correct && result.correct_choices && (
              <div style={{ marginTop: '0.5rem', fontWeight: 600 }}>
                Correct answer{result.correct_choices.length > 1 ? 's' : ''}: {result.correct_choices.map(c => c.text).join(', ')}
              </div>
            )}
          </div>
        )}

        {/* Navigation buttons */}
        <div style={{ display: 'flex', gap: '1rem', justifyContent: 'space-between' }}>
          <div>
            {/* Skip button: allow user to move to next question without answering */}
            <button
              className="btn btn-secondary"
              onClick={() => {
                // mark current as incorrect/unanswered and move on
                setAnswers({
                  ...answers,
                  [currentIndex]: false
                })
                setResult(null)
                if (currentIndex < questions.length - 1) {
                  setCurrentIndex(currentIndex + 1)
                } else {
                  handleFinish()
                }
              }}
              disabled={submitting}
            >
              Skip Question →
            </button>
          </div>

          <div style={{ display: 'flex', gap: '1rem' }}>
            {!result ? (
              <button
                className="btn btn-primary"
                onClick={handleSubmit}
                disabled={!selectedChoices[currentIndex] || submitting}
              >
                {submitting ? 'Checking...' : 'Submit Answer'}
              </button>
            ) : (
              <button
                className="btn btn-primary"
                onClick={handleNext}
              >
                {currentIndex < questions.length - 1 ? 'Next Question →' : 'Finish Quiz ✓'}
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default MultipleChoiceQuiz

