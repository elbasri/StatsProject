
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
      // Set all columns as initially selected
      setSelectedColumns(response.data.parsed_data.columns);
      setResultData(response.data.parsed_data);
      console.log(response.data.id)
    } catch (error) {
      console.error('Error uploading file:', error.message);
    }
  };
  const handleApplyAlgorithm = () => {
    setErrorMessage(null);
    const fID = uploadedFile.id
    const requestData = {
      selectedColumns,
      selectedAlgorithm,
      resultData,
      fID,
    };

    // Make an API call to the backend endpoint for applying the algorithm
    // Adjust the URL and method based on your backend API
    axios.post('http://127.0.0.1:8000/api/apply-algorithm/', requestData)
      .then((response) => {
        // Handle success
        console.log('Algorithm applied successfully:', response.data);
        if (response.status === 200) {
          const resultId = response.data;
          //console.log(resultId)
          navigate(`/results/${resultId}`);
        } else {
          // Set the error message
          setErrorMessage(`Failed to apply algorithm: ${response.statusText}`);
        }
      })
      .catch((error) => {
        // Handle error
        console.error('Error applying algorithm:', error.message);
        setErrorMessage(`Failed to apply algorithm: ${response.statusText}`);
      });
  };

  const handleColumnToggle = (column) => {
    const isSelected = selectedColumns.includes(column);
    console.log("column "+column);
    if (isSelected) {
      setSelectedColumns((prevSelected) => prevSelected.filter((col) => col !== column));
    } else {
      setSelectedColumns((prevSelected) => [...prevSelected, column]);
    }
  };
  const handleAlgorithmChange = (event) => {
    console.log("algo "+event.target.value);
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
            Telecharger un Fichier
          </MDTypography>
          <MDTypography display="block" variant="button" color="white" my={1}>
          visualiser les donnees de votre fichier csv/excel dans un tableau, Choisir le type d'algorithm a appliquer et les colonnes et lignes concernees, et visualiser les resultats dans un graph
          
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
              <div>
                <div {...getRootProps()} style={{ border: '2px dashed #ccc', padding: '20px', textAlign: 'center' }}>
                  <input {...getInputProps()} />
                  {isDragActive ? <p>Déposez le fichier ici...</p> : <p>Faites glisser et déposez un fichier ici, ou cliquez pour en sélectionner un</p>}
                </div>
                
              </div>
              </MDTypography>
            </MDBox>
            <MDBox mt={4} mb={1}>
              <MDButton variant="gradient" color="info" fullWidth>
                Telecharger et visualiser
              </MDButton>
            </MDBox>
          </MDBox>
        </MDBox>
      </Card>
      
    </CoverLayout>
    <div>
    {uploadedFile && (
        <div>
          <select value={selectedAlgorithm} onChange={handleAlgorithmChange}>
              <option value="">Fonction à appliquer</option>
              <option value="description_dataframe">Description de donnees</option>
              <option value="longueur_dataframe">longueur de donnees</option>
              <option value="premieres_valeurs">Premieres valeurs</option>
              <option value="valeurs_recentes">Valeurs recentes</option>
              <option value="visualiserCol">Visualiser la colonne</option>
              <option value="mediane_colonne">Calcule de médiane</option>
              <option value="moyenne_colonne">Calcule de moyenne</option>
              <option value="variance_colonne">Calcule de variance</option>
              <option value="ecart_type_colonne">l'écart type</option>
              <option value="mode">Mode de la colonne</option>
          </select>
          <button onClick={handleApplyAlgorithm}>Apply Algorithm</button>
          {errorMessage && (
            <div style={{ color: 'red', marginTop: '10px' }}>
              {errorMessage}
            </div>
          )}
            <h4>Donnees de fichier:</h4>
            {/* Display the table using a table component or any preferred method */}
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
          
            {/* Display additional fields from the parsed data */}
            {/* Add more fields based on the parsed data */}
        </div>
    )}
    </div>
    </DashboardLayout>
  );
}

export default Cover;
