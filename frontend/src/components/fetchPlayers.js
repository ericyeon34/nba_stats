import React, { useState, useEffect } from 'react';
import { fetchPlayer, fetchPlayers } from './apiService';

const PlayersList = () => {
    const [players, setPlayers] = useState([]);

    useEffect(() => {
        const fetchPlayersList = async () => {
            const players = await fetchPlayers();
            setPlayers(players);
        }
        fetchPlayersList();
    }, []);

    return (
        <div>
            <h1 className='text-2xl font-bold mb-3'>Players</h1>
            <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'>
                {players.map(player => (
                    <div key={player.id} className='border p-4 rounded'>
                        <h2 className='text-xl font-bold'>{player.name}</h2>
                        <p>Player: {player.full_name}</p>
                        <p>Points: {player.points}</p>
                        <p>Assists: {player.assists}</p>
                        <p>Rebounds: {player.rebounds}</p>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default PlayersList;