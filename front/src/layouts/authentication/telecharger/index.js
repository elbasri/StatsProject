
// react-router-dom components
import { useNavigate } from 'react-router-dom';

// @mui material components
import Card from "@mui/material/Card";
import Checkbox from "@mui/material/Checkbox";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDButton from "components/MDButton";

// Authentication layout components
import CoverLayout from "layouts/authentication/components/CoverLayout";

// Images
import bgImage from "assets/images/bg-up-cover.jpeg";

import React, { useState } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';

function Cover() {
  const [uploadedFile, setUploadedFile] = useState(null);
  const [selectedColumns, setSelectedColumns] = useState([]);
  const [selectedAlgorithm, setSelectedAlgorithm] = useState('');
  const [selectedAlgorithmType, setSelectedAlgorithmType] = useState('visualisation');
  const [selectedSubAlgorithmType, setSelectedSubAlgorithmType] = useState('');
  const [resultData, setResultData] = useState(null);
  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState(null);

  const onDrop = async (acceptedFiles) => {
    const file = acceptedFiles[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/uploaded-files/', formData);
      setUploadedFile(response.data);
      setSelectedColumns(response.data.parsed_data.columns);
      setResultData(response.data.parsed_data);
      console.log(response.data.id);
    } catch (error) {
      console.error('Error uploading file:', error.message);
    }
  };

  const handleAlgorithmTypeChange = (algorithmType) => {
    setSelectedAlgorithmType(algorithmType);
    setSelectedSubAlgorithmType('');
    setSelectedAlgorithm('');
  };

  const handleSubAlgorithmTypeChange = (subAlgorithmType) => {
    setSelectedSubAlgorithmType(subAlgorithmType);
    setSelectedAlgorithm('');
  };

  const handleApplyAlgorithm = () => {
    setErrorMessage(null);

    // Handle apply algorithm logic here based on selectedAlgorithmType and selectedAlgorithm
    if (selectedAlgorithmType === 'visualisation' && selectedSubAlgorithmType) {
      // Handle visualization algorithm based on selectedSubAlgorithmType
      // ...
    } else if (selectedAlgorithmType === 'numeric' && selectedSubAlgorithmType) {
      // Handle numeric algorithm based on selectedSubAlgorithmType
      // ...
    } else {
      setErrorMessage('Please select an algorithm and sub-algorithm type.');
      return;
    }

    const requestData = {
      selectedColumns,
      selectedAlgorithm,
      resultData,
      fID: uploadedFile.id,
    };

    // Make an API call to the backend endpoint for applying the algorithm
    axios
      .post('http://127.0.0.1:8000/api/apply-algorithm/', requestData)
      .then((response) => {
        if (response.status === 200) {
          const resultId = response.data;
          navigate(`/results/${resultId}`);
        } else {
          setErrorMessage(`Failed to apply algorithm: ${response.statusText}`);
        }
      })
      .catch((error) => {
        console.error('Error applying algorithm:', error.message);
        setErrorMessage(`Failed to apply algorithm: ${response.statusText}`);
      });
  };

  const handleColumnToggle = (column) => {
    const isSelected = selectedColumns.includes(column);
    if (isSelected) {
      setSelectedColumns((prevSelected) => prevSelected.filter((col) => col !== column));
    } else {
      setSelectedColumns((prevSelected) => [...prevSelected, column]);
    }
  };

  const handleAlgorithmChange = (event) => {
    setSelectedAlgorithm(event.target.value);
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
<DashboardLayout>
    <DashboardNavbar />
        <CoverLayout image={bgImage}>
          <Card>
            <MDBox
              variant="gradient"
              bgColor="info"
              borderRadius="lg"
              coloredShadow="success"
              mx={2}
              mt={-3}
              p={3}
              mb={1}
              textAlign="center"
            >
              <MDTypography variant="h4" fontWeight="medium" color="white" mt={1}>
                Télécharger un Fichier
              </MDTypography>
              <MDTypography display="block" variant="button" color="white" my={1}>
                Visualisez les données de votre fichier CSV/Excel dans un tableau. Choisissez le type d'algorithme à appliquer, les colonnes et lignes concernées, et visualisez les résultats dans un graphique.
              </MDTypography>
            </MDBox>
            <MDBox pt={4} pb={3} px={3}>
              <MDBox component="form" role="form">
                <MDBox display="flex" alignItems="center" ml={-1}>
                  <MDTypography
                    variant="button"
                    fontWeight="regular"
                    color="text"
                    sx={{ cursor: "pointer", userSelect: "none", ml: -1 }}
                  >
                    <div {...getRootProps()} style={{ border: '2px dashed #ccc', padding: '20px', textAlign: 'center' }}>
                      <input {...getInputProps()} />
                      {isDragActive ? <p>Déposez le fichier ici...</p> : <p>Faites glisser et déposez un fichier ici, ou cliquez pour en sélectionner un</p>}
                    </div>
                  </MDTypography>
                </MDBox>
                <MDBox mt={4} mb={1}>
                  <MDButton variant="gradient" color="info" fullWidth>
                    Télécharger et Visualiser
                  </MDButton>
                </MDBox>
              </MDBox>
            </MDBox>
          </Card>
        </CoverLayout>
        <MDTypography variant="h4" fontWeight="medium" mt={1}>
          <div>
            <h1>Graph</h1>
            <MDBox mt={3} lineHeight={1}>
              <MDTypography variant="h6">
                Quel est le type de traitement que vous voulez appliquer ?
              </MDTypography>
              <MDBox
                sx={{
                  display: "flex",
                  mt: 2,
                  mr: 1,
                }}
              >
                <MDButton
                  color="dark"
                  variant="gradient"
                  onClick={() => handleAlgorithmTypeChange('visualisation')}
                  disabled={selectedAlgorithmType === 'visualisation'}
                  fullWidth
                  sx={{
                    maxWidth: '250px',
                    padding: '5px',
                    margin: '5px',
                  }}
                >
                  Visualisation
                </MDButton>
                <MDButton
                  color="dark"
                  variant="gradient"
                  onClick={() => handleAlgorithmTypeChange('numeric')}
                  disabled={selectedAlgorithmType === 'numeric'}
                  fullWidth
                  sx={{
                    maxWidth: '250px',
                    padding: '5px',
                    margin: '5px',
                  }}
                >
                  Mesures statistiques
                </MDButton>
              </MDBox>
            </MDBox>
            
            {selectedAlgorithmType && (
              <div>
                <MDBox mt={3} lineHeight={1}>
                  <MDTypography variant="h6">
                    Quel est le sous-type de traitement que vous voulez appliquer ?
                  </MDTypography>
                  <MDBox
                    sx={{
                      display: "flex",
                      mt: 2,
                      mr: 1,
                    }}
                  >
                    {selectedAlgorithmType === 'visualisation' ? (
                      <>
                        <MDButton
                          color="dark"
                          variant="gradient"
                          onClick={() => handleSubAlgorithmTypeChange('graphiqueBase')}
                          disabled={selectedSubAlgorithmType === 'graphiqueBase'}
                          fullWidth
                          sx={{
                            maxWidth: '250px',
                            padding: '5px',
                            margin: '5px',
                          }}
                        >
                          Graphiques de Base
                        </MDButton>
                        <MDButton
                          color="dark"
                          variant="gradient"
                          onClick={() => handleSubAlgorithmTypeChange('graphiqueDistribution')}
                          disabled={selectedSubAlgorithmType === 'graphiqueDistribution'}
                          fullWidth
                          sx={{
                            maxWidth: '250px',
                            padding: '5px',
                            margin: '5px',
                          }}
                        >
                          Graphiques de Distribution
                        </MDButton>
                        <MDButton
                          color="dark"
                          variant="gradient"
                          onClick={() => handleSubAlgorithmTypeChange('graphiqueCategoriel')}
                          disabled={selectedSubAlgorithmType === 'graphiqueCategoriel'}
                          fullWidth
                          sx={{
                            maxWidth: '250px',
                            padding: '5px',
                            margin: '5px',
                          }}
                        >
                          Graphiques Catégoriels
                        </MDButton>
                        <MDButton
                          color="dark"
                          variant="gradient"
                          onClick={() => handleSubAlgorithmTypeChange('autresGraphiques')}
                          disabled={selectedSubAlgorithmType === 'autresGraphiques'}
                          fullWidth
                          sx={{
                            maxWidth: '250px',
                            padding: '5px',
                            margin: '5px',
                          }}
                        >
                          Autres graphiques
                        </MDButton>
                      </>
                    ) : (
                      <>
                        <MDButton
                          color="dark"
                          variant="gradient"
                          onClick={() => handleSubAlgorithmTypeChange('tendanceCentrale')}
                          disabled={selectedSubAlgorithmType === 'tendanceCentrale'}
                          fullWidth
                          sx={{
                            maxWidth: '250px',
                            padding: '5px',
                            margin: '5px',
                          }}
                        >
                          Tendance centrale
                        </MDButton>
                        <MDButton
                          color="dark"
                          variant="gradient"
                          onClick={() => handleSubAlgorithmTypeChange('variabilite')}
                          disabled={selectedSubAlgorithmType === 'variabilite'}
                          fullWidth
                          sx={{
                            maxWidth: '250px',
                            padding: '5px',
                            margin: '5px',
                          }}
                        >
                          Variabilité
                        </MDButton>
                        <MDButton
                          color="dark"
                          variant="gradient"
                          onClick={() => handleSubAlgorithmTypeChange('autresMesures')}
                          disabled={selectedSubAlgorithmType === 'autresMesures'}
                          fullWidth
                          sx={{
                            maxWidth: '250px',
                            padding: '5px',
                            margin: '5px',
                          }}
                        >
                          Autres Mesures
                        </MDButton>
                      </>
                    )}
                  </MDBox>
                </MDBox>
                
                {selectedSubAlgorithmType && (
                  <div>
                    <select
                      value={selectedAlgorithm}
                      onChange={(e) => setSelectedAlgorithm(e.target.value)}
                    >
                      <option value="">Fonction à appliquer</option>
                      {selectedAlgorithmType === 'visualisation' ? (
                        <>
                          {selectedSubAlgorithmType === 'graphiqueBase' ? (
                            <>
                              <option value="graphiqueLineaire">Graphique Linéaire</option>
                              <option value="graphiqueDisperse">Graphique Dispersé</option>
                              <option value="graphiqueBarres">Graphique à Barres</option>
                            </>
                          ) : selectedSubAlgorithmType === 'graphiqueDistribution' ? (
                            <>
                              <option value="histogramme">Histogramme</option>
                              <option value="graphiqueKDE">Graphique KDE</option>
                              <option value="boiteMoustaches">Boîte à Moustaches</option>
                              <option value="graphiqueViolon">Graphique en Violon</option>
                            </>
                          ) : selectedSubAlgorithmType === 'graphiqueCategoriel' ? (
                            <>
                              <option value="diagrammeCirculaire">Diagramme Circulaire</option>
                              <option value="graphiquePaires">Graphique de Paires</option>
                            </>
                          ) : selectedSubAlgorithmType === 'autresGraphiques' ? (
                            <>
                              <option value="carteThermique1">Carte Thermique 1</option>
                              <option value="carteThermique2">Carte Thermique 2</option>
                            </>
                          ) : null}
                        </>
                      ) : (
                        <>
                          {selectedSubAlgorithmType === 'tendanceCentrale' ? (
                            <>
                              <option value="calculeMoyenne">Calcule de moyenne</option>
                              <option value="calculeMediane">Calcule de médiane</option>
                              <option value="modeColonne">Mode de la colonne</option>
                            </>
                          ) : selectedSubAlgorithmType === 'variabilite' ? (
                            <>
                              <option value="esperance">Esperance</option>
                              <option value="calculeVariance">Calcule de variance</option>
                              <option value="ecartType">L'écart type</option>
                              <option value="etendue">Etendue</option>
                            </>
                          ) : selectedSubAlgorithmType === 'autresMesures' ? (
                            <>
                              <option value="descriptionDonnees">Description de données</option>
                              <option value="longueurDonnees">Longueur de données</option>
                              <option value="premieresValeurs">Premières valeurs</option>
                              <option value="valeursRecentes">Valeurs récentes</option>
                            </>
                          ) : null}
                        </>
                      )}
                    </select>
                    <button onClick={handleApplyAlgorithm}>Appliquer l'algorithme</button>
                    
                    {uploadedFile && (
                      <table style={{ width: '100%' }}>
                        <thead style={{ backgroundColor: 'yourColor', color: 'yourTextColor', fontWeight: 'bold' }}>
                          <tr>
                            {uploadedFile.parsed_data.columns.map((col) => (
                              <th key={col}>
                                <Checkbox
                                  checked={selectedColumns.includes(col)}
                                  onChange={() => handleColumnToggle(col)}
                                />
                                {col}
                              </th>
                            ))}
                          </tr>
                        </thead>
                        <tbody>
                          {uploadedFile.parsed_data.rows.map((row, index) => (
                            <tr key={index}>
                              {row.map((cell, cellIndex) => (
                                <td key={cellIndex}>{cell}</td>
                              ))}
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    )}
                  </div>
                )}
              </div>
            )}
          </div>
        </MDTypography>
    </DashboardLayout>
  );
}

export default Cover;