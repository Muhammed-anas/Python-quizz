import { useLocation, useNavigate } from 'react-router-dom'
import '../App.css'

function QuizResult() {
  const location = useLocation()
  const { score = 0, totalQuestions = 0, questionType } = location.state || {}
  const navigate = useNavigate()

  const percentage = totalQuestions > 0 ? Math.round((score / totalQuestions) * 100) : 0
  
  let message = ''
  let emoji = '🎯'
  
  if (percentage >= 90) {
    message = 'Outstanding! You\'re a Python expert!'
    emoji = '🏆'
  } else if (percentage >= 75) {
    message = 'Great job! You have a solid understanding!'
    emoji = '🌟'
  } else if (percentage >= 60) {
    message = 'Good work! Keep practicing!'
    emoji = '👍'
  } else if (percentage >= 50) {
    message = 'Not bad! Review the topics and try again!'
    emoji = '📚'
  } else {
    message = 'Keep learning! Practice makes perfect!'
    emoji = '💪'
  }

  return (
    <div className="container">
      <div className="card" style={{ maxWidth: '600px', margin: '2rem auto', textAlign: 'center' }}>
        <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>{emoji}</div>
        
        <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: '#333' }}>
          Quiz Complete!
        </h1>

        <div style={{ marginBottom: '2rem' }}>
          <div style={{ fontSize: '3rem', fontWeight: 'bold', color: '#667eea', marginBottom: '0.5rem' }}>
            {score} / {totalQuestions}
          </div>
          <div style={{ fontSize: '1.5rem', color: '#666', marginBottom: '1rem' }}>
            {percentage}% Correct
          </div>
          <div style={{ fontSize: '1.2rem', color: '#333', fontWeight: '500' }}>
            {message}
          </div>
        </div>

        {/* Progress visualization */}
        <div style={{ marginBottom: '2rem', padding: '1rem', background: '#f8f9fa', borderRadius: '8px' }}>
          <div style={{ marginBottom: '0.5rem', fontSize: '0.9rem', color: '#666', textAlign: 'left' }}>
            Correct Answers
          </div>
          <div style={{
            width: '100%',
            height: '30px',
            background: '#e0e0e0',
            borderRadius: '15px',
            overflow: 'hidden',
            position: 'relative'
          }}>
            <div style={{
              width: `${percentage}%`,
              height: '100%',
              background: percentage >= 75 
                ? 'linear-gradient(135deg, #28a745 0%, #20c997 100%)'
                : percentage >= 50
                ? 'linear-gradient(135deg, #ffc107 0%, #fd7e14 100%)'
                : 'linear-gradient(135deg, #dc3545 0%, #c82333 100%)',
              transition: 'width 0.5s ease',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: 'white',
              fontWeight: 'bold',
              fontSize: '0.9rem'
            }}>
              {percentage > 10 && `${percentage}%`}
            </div>
          </div>
        </div>

        <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', flexWrap: 'wrap' }}>
          <button
            className="btn btn-primary"
            onClick={() => navigate('/quiz-setup', { state: { questionType } })}
          >
            Try Again 🔄
          </button>
          <button
            className="btn btn-secondary"
            onClick={() => navigate('/')}
          >
            Back to Home 🏠
          </button>
        </div>
      </div>
    </div>
  )
}

export default QuizResult

