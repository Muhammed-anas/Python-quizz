import { useNavigate } from 'react-router-dom'
import '../App.css'

function Home() {
  const navigate = useNavigate()

  return (
    <div className="container">
      <div className="card" style={{ textAlign: 'center', padding: '4rem 2rem' }}>
        <h1 style={{ fontSize: '3rem', marginBottom: '1rem', background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
          🐍 Python Quiz Platform
        </h1>
        <p style={{ fontSize: '1.2rem', color: '#666', marginBottom: '3rem' }}>
          Test your Python knowledge with multiple choice and coding questions
        </p>
        
        <div style={{ display: 'flex', gap: '2rem', justifyContent: 'center', flexWrap: 'wrap' }}>
          <button 
            onClick={() => navigate('/quiz-setup', { state: { questionType: 'multiple_choice' } })}
            className="btn btn-primary" 
            style={{ padding: '1.5rem 3rem', fontSize: '1.2rem' }}
          >
            📝 Multiple Choice Quiz
          </button>
          <button 
            onClick={() => navigate('/quiz-setup', { state: { questionType: 'coding' } })}
            className="btn btn-success" 
            style={{ padding: '1.5rem 3rem', fontSize: '1.2rem' }}
          >
            💻 Coding Quiz
          </button>
        </div>

        <div style={{ marginTop: '3rem', padding: '2rem', background: '#f8f9fa', borderRadius: '12px' }}>
          <h2 style={{ marginBottom: '1rem', color: '#333' }}>Features</h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1.5rem', textAlign: 'left' }}>
            <div>
              <h3 style={{ color: '#667eea', marginBottom: '0.5rem' }}>📚 Comprehensive Questions</h3>
              <p style={{ color: '#666' }}>Multiple choice questions covering Python basics to advanced topics</p>
            </div>
            <div>
              <h3 style={{ color: '#667eea', marginBottom: '0.5rem' }}>💻 Code Editor</h3>
              <p style={{ color: '#666' }}>Practice coding with real-time execution and test case validation</p>
            </div>
            <div>
              <h3 style={{ color: '#667eea', marginBottom: '0.5rem' }}>✅ Instant Feedback</h3>
              <p style={{ color: '#666' }}>Get immediate feedback on your answers with detailed explanations</p>
            </div>
            <div>
              <h3 style={{ color: '#667eea', marginBottom: '0.5rem' }}>📊 Difficulty Levels</h3>
              <p style={{ color: '#666' }}>Questions ranging from easy to hard to suit all skill levels</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home

