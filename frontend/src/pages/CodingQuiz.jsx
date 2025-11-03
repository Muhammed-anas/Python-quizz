import { useState, useEffect } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import { getRandomQuestions, checkAnswer } from '../utils/api'
import '../App.css'

function CodingQuiz() {
  const location = useLocation()
  const { questionCount = 10 } = location.state || {}
  
  const [questions, setQuestions] = useState([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [codes, setCodes] = useState({}) // Store code for each question
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
      const data = await getRandomQuestions('coding', questionCount)
      setQuestions(data)
      // Initialize code state with starter_code
      const initialCodes = {}
      data.forEach((q, idx) => {
        initialCodes[idx] = q.starter_code || ''
      })
      setCodes(initialCodes)
      setQuizStarted(true)
      setAnswers({})
    } catch (error) {
      console.error('Error loading questions:', error)
      alert('Failed to load questions. Please try again.')
      navigate('/')
    } finally {
      setLoading(false)
    }
  }

  const handleCodeChange = (code) => {
    setCodes({
      ...codes,
      [currentIndex]: code
    })
  }

  const handleSubmit = async () => {
    if (!codes[currentIndex] || !codes[currentIndex].trim()) {
      alert('Please write some code')
      return
    }

    setSubmitting(true)
    try {
      const question = questions[currentIndex]
      const response = await checkAnswer(question.id, { code: codes[currentIndex] })
      
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
        questionType: 'coding'
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

        {/* Test Cases */}
        {currentQuestion.test_cases && currentQuestion.test_cases.length > 0 && (
          <div style={{ marginBottom: '1.5rem', padding: '1rem', background: '#f8f9fa', borderRadius: '8px' }}>
            <h3 style={{ marginBottom: '0.75rem', color: '#333' }}>Test Cases:</h3>
            {currentQuestion.test_cases.map((testCase, idx) => (
              <div key={idx} style={{ marginBottom: '0.5rem', fontSize: '0.9rem', color: '#666' }}>
                <strong>Input:</strong> <code>{JSON.stringify(testCase.input_data)}</code>
                <br />
                <strong>Expected Output:</strong> <code>{JSON.stringify(testCase.expected_output)}</code>
              </div>
            ))}
          </div>
        )}

        {/* Code Editor */}
        <div style={{ marginBottom: '1.5rem' }}>
          <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: '600', color: '#333' }}>
            Your Code:
          </label>
          <textarea
            value={codes[currentIndex] || ''}
            onChange={(e) => handleCodeChange(e.target.value)}
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

        {/* Result message */}
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

        {/* Navigation buttons */}
        <div style={{ display: 'flex', gap: '1rem', justifyContent: 'space-between' }}>
          <div>
            {/* Skip button: allow user to move to next question without answering */}
            <button
              className="btn btn-secondary"
              onClick={() => {
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
            {/* Show Run Tests unless the current result is a successful pass. If failed, allow re-run. */}
            {!(result && result.correct) ? (
              <button
                className="btn btn-primary"
                onClick={handleSubmit}
                disabled={!codes[currentIndex]?.trim() || submitting}
              >
                {submitting ? 'Running Tests...' : (result ? 'Re-run Tests' : 'Run Tests')}
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

export default CodingQuiz

