
// react-router-dom components
import { Link } from "react-router-dom";

// @mui material components
import Card from "@mui/material/Card";
import Checkbox from "@mui/material/Checkbox";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDInput from "components/MDInput";
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

  const onDrop = async (acceptedFiles) => {
    const file = acceptedFiles[0];
    const formData = new FormData();
    formData.append('file', file);
    formData.append('selected_columns', JSON.stringify(selectedColumns)); // Include selected columns

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/uploaded-files/', formData);
      setUploadedFile(response.data);
      // Set all columns as initially selected
      setSelectedColumns(response.data.parsed_data.columns);
    } catch (error) {
      console.error('Error uploading file:', error.message);
    }
  };

  const handleColumnToggle = (column) => {
    const isSelected = selectedColumns.includes(column);
    if (isSelected) {
      setSelectedColumns((prevSelected) => prevSelected.filter((col) => col !== column));
    } else {
      setSelectedColumns((prevSelected) => [...prevSelected, column]);
    }
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
            <h4>File Data:</h4>
            {/* Display the table using a table component or any preferred method */}
            <table style={{ width: '100%' }}>
            <thead>
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
