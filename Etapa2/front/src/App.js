import React, { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [predictions, setPredictions] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handlePredictions = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        const data = await response.json();
        setPredictions(data);
      } else {
        console.error('Error al realizar predicciones');
      }
    } catch (error) {
      console.error('Error de red:', error);
    }
  };

  return (
    <div>
      <h1>Carga de Archivo CSV y Predicciones</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handlePredictions}>Realizar Predicciones</button>
      {predictions && (
        <div>
          <h2>Resultados de las Predicciones:</h2>
          <pre>{JSON.stringify(predictions, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
