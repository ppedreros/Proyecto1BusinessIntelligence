import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css'; 

function HomePage() {
  return (
    <div className="container">
      <h1 className="title">Bienvenido a la página principal</h1>
      <Link to="/app" className="link">Genera predicciones con archivo CSV</Link>
      <Link to="/appTexto" className="link">Genera predicciones de una review</Link>
    </div>
  );
}

export default HomePage;
