import React, { useState } from 'react';
import axios from 'axios';

const JoinQuizForm = () => {
    const [quizId, setQuizId] = useState('');
    const [userId, setUserId] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/joinQuiz', {
                quiz_id: quizId,
                user_id: userId,
            });
            setMessage(response.data.message);
        } catch (error) {
            setMessage(error.response?.data?.detail || 'An error occurred');
        }
    };

    return (
        <div>
            <h1>Join Quiz</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Quiz ID:</label>
                    <input
                        type="text"
                        value={quizId}
                        onChange={(e) => setQuizId(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>User ID:</label>
                    <input
                        type="text"
                        value={userId}
                        onChange={(e) => setUserId(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Join</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default JoinQuizForm;
