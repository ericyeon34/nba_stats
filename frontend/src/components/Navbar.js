import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        // <nav className='bg-blue-500 p-4'>
        <nav className='bg-teal-600 p-4'>
            <div className='container mx-auto flex justify-between items-center'>
                <div className='text-white text-xl font-bold'>
                    <Link to='/'>NBA Stats</Link>
                </div>
                <div>
                    <Link to='/' className='text-white px-4 py-2 hover:bg-blue-700 rounded'>Home</Link>
                    <Link to='/players' className='text-white px-4 py-2 hover:bg-blue-700 rounded'>Players</Link>
                </div>
            </div>
        </nav>
    )
}

export default Navbar;