import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const joinQuiz = async (quizId, userId) => {
    return axios.post(`${API_URL}/joinQuiz`, { quiz_id: quizId, user_id: userId });
};
