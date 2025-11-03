import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import QuizSetup from './pages/QuizSetup'
import MultipleChoiceQuiz from './pages/MultipleChoiceQuiz'
import CodingQuiz from './pages/CodingQuiz'
import QuizResult from './pages/QuizResult'
import MultipleChoiceQuestion from './pages/MultipleChoiceQuestion'
import CodingQuestion from './pages/CodingQuestion'
import './App.css'

function App() {
  return (
    <Router>
      <div className="app">
        <nav className="navbar">
          <Link to="/" className="nav-link">
            <h1>🐍 Python Quiz</h1>
          </Link>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/quiz-setup" element={<QuizSetup />} />
          <Route path="/multiple-choice-quiz" element={<MultipleChoiceQuiz />} />
          <Route path="/coding-quiz" element={<CodingQuiz />} />
          <Route path="/quiz-result" element={<QuizResult />} />
          <Route path="/multiple-choice" element={<MultipleChoiceQuestion />} />
          <Route path="/coding" element={<CodingQuestion />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
