import React, { useState } from 'react';
import './App.css';

function AppTexto() {
  const [text, setText] = useState('');
  const [predictions, setPredictions] = useState(null);

  const handleTextChange = (event) => {
    setText(event.target.value);
  };

  const handlePredictions = async () => {
    try {
      const response = await fetch('http://localhost:8000/predictText', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      if (response.ok) {
        const data = await response.json();
        setPredictions(data.predictions);
      } else {
        console.error('Error al realizar predicciones');
      }
    } catch (error) {
      console.error('Error de red:', error);
    }
  };

  return (
    <div className="container">
      <div>
        <h1>Predicciones con Texto Plano</h1>
        <div className="text-input-container">
          <label htmlFor="text-input" className="text-input-label">
            Ingrese el texto para hacer predicciones:
          </label>
          <textarea
            id="text-input"
            value={text}
            onChange={handleTextChange}
            className="text-input"
            rows="4"
          />
        </div>
        <div className="button-container">
          <button onClick={handlePredictions}>Realizar Predicciones</button>
        </div>
        {predictions && (
          <div>
            <h2>Resultado de la Predicción:</h2>
            <h4>El modelo hace una predicción con una precisión de 6  0%</h4>
            <div className="prediction-container">
              <p>Review: {predictions.Review}</p>
              <p>Clase: {predictions.Class}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default AppTexto;
