import React, { useState } from 'react';
import './AppTexto.css';

function App() {
  const [file, setFile] = useState(null);
  const [predictions, setPredictions] = useState(null);
  const [buttonText, setButtonText] = useState('Seleccionar Archivo'); 

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
    const fileName = selectedFile ? selectedFile.name : 'Seleccionar Archivo';
    setButtonText(fileName);
  };

  const handlePredictions = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/predictCSV', {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        const data = await response.json();
        const transformedData = Object.keys(data.Review).map((key) => ({
          numReview: key,
          review: data.Review[key],
          clase: data.Class[key]
        }));
        setPredictions(transformedData);
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
        <h1>Carga de Archivo CSV y Predicciones</h1>
        <div className="file-input-container">
          <label htmlFor="file-input" className="file-input-label">
            {buttonText}
          </label>
          <input
            id="file-input"
            type="file"
            onChange={handleFileChange}
            className="file-input"
          />
        </div>
        <div className="button-container">
          <button onClick={handlePredictions}>Realizar Predicciones</button>
        </div>
        {predictions && (
          <div>
            <h2>Resultados de las Predicciones:</h2>
            <div className="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Review No.</th>
                    <th>Review</th>
                    <th>Calificacion</th>
                  </tr>
                </thead>
                <tbody>
                  {predictions.map((prediction) => (
                    <tr key={prediction.numReview}>
                      <td>{prediction.numReview}</td>
                      <td>{prediction.review}</td>
                      <td>{prediction.clase}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
