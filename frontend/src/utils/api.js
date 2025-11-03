import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const getRandomQuestion = async (type = null) => {
  const url = type ? `/questions/random/?type=${type}` : '/questions/random/'
  const response = await api.get(url)
  return response.data
}

export const getRandomQuestions = async (type = null, count = 10) => {
  const url = type ? `/questions/random/?type=${type}&count=${count}` : `/questions/random/?count=${count}`
  const response = await api.get(url)
  return response.data
}

export const getQuestions = async (type = null, difficulty = null, category = null) => {
  const params = {}
  if (type) params.type = type
  if (difficulty) params.difficulty = difficulty
  if (category) params.category = category
  
  const response = await api.get('/questions/', { params })
  return response.data
}

export const checkAnswer = async (questionId, data) => {
  const response = await api.post(`/questions/${questionId}/check_answer/`, data)
  return response.data
}

export const getCategories = async () => {
  const response = await api.get('/categories/')
  return response.data
}

export default api

