import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Flask backend URL

export const fetchPlayers = async () => {
    const response = await axios.get(`${API_URL}/players`);
    return response.data;
}

export const fetchPlayer = async (playerId) => {
    const response = await axios.get(`${API_URL}/player/${playerId}`);
    return response.data;
}