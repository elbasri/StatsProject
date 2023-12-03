/**
=========================================================
* Material Dashboard 2 React - v2.2.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2023 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// @mui material components
import Grid from "@mui/material/Grid";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";

// Material Dashboard 2 React example components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";
import ReportsBarChart from "examples/Charts/BarCharts/ReportsBarChart";
import ReportsLineChart from "examples/Charts/LineCharts/ReportsLineChart";
import ComplexStatisticsCard from "examples/Cards/StatisticsCards/ComplexStatisticsCard";

// Data
import reportsBarChartData from "layouts/dashboard/data/reportsBarChartData";
import reportsLineChartData from "layouts/dashboard/data/reportsLineChartData";

// Dashboard components
import Projects from "layouts/dashboard/components/Projects";
import OrdersOverview from "layouts/dashboard/components/OrdersOverview";

import React, { useEffect, useState } from 'react';

function Dashboard() {
  const { sales, tasks } = reportsLineChartData;
  const [dataFromServer, setDataFromServer] = useState(null);
  const [statistics, setStatistics] = useState(null);

  // Function to fetch data from the server
  const fetchDataFromServer = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/results/');
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setDataFromServer(data);
    } catch (error) {
      console.error('Error fetching data:', error.message);
    }
  };
   // Fetch data when the component mounts
   useEffect(() => {
    fetchDataFromServer();
  }, []);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/counts/');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setStatistics(data);
      } catch (error) {
        console.error('Error fetching statistics:', error.message);
      }
    };

    fetchData();
  }, []);

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <MDBox>
        {/* ... (existing code) */}
        {/* Display the data received from the server */}
        {dataFromServer && (
          <div>
            <h2>List des fichiers:</h2>
            {/*<pre>{JSON.stringify(dataFromServer, null, 2)}</pre>*/}
          </div>
        )}
        
      </MDBox>
      <MDBox py={3}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6} lg={4}>
            <MDBox mb={1.5}>
              <ComplexStatisticsCard
                color="dark"
                icon="person_add"
                title="Fichiers"
                count={statistics ? ( <span>{statistics.total_files}</span> ) : (  0 )}
                percentage={{
                  color: "success",
                  amount: "+90%",
                  label: "Nouveau utilisateurs (plusieurs fichiers par utilisateur)",
                }}
              />
            </MDBox>
          </Grid>
          <Grid item xs={12} md={6} lg={4}>
            <MDBox mb={1.5}>
              <ComplexStatisticsCard
                icon="store"
                title="Resultats"
                count={statistics ? ( <span>{statistics.total_results}</span> ) : (  0 )}
                percentage={{
                  color: "success",
                  amount: "+85%",
                  label: "Avec des graphs",
                }}
              />
            </MDBox>
          </Grid>
          <Grid item xs={12} md={6} lg={4}>
            <MDBox mb={1.5}>
              <ComplexStatisticsCard
                color="success"
                icon="leaderboard"
                title="Resultats avec des Graphs"
                count={statistics ? ( <span>{statistics.graph_results}</span> ) : (  0 )}
              />
            </MDBox>
          </Grid>
        </Grid>
        <MDBox mt={4.5}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6} lg={4}>
              <MDBox mb={3}>
                <ReportsBarChart
                  color="info"
                  title="website views"
                  description="Last Campaign Performance"
                  date="campaign sent 2 days ago"
                  chart={reportsBarChartData}
                />
              </MDBox>
            </Grid>
            <Grid item xs={12} md={6} lg={4}>
              <MDBox mb={3}>
                <ReportsLineChart
                  color="success"
                  title="daily sales"
                  description={
                    <>
                      (<strong>+15%</strong>) increase in today sales.
                    </>
                  }
                  date="updated 4 min ago"
                  chart={sales}
                />
              </MDBox>
            </Grid>
            <Grid item xs={12} md={6} lg={4}>
              <MDBox mb={3}>
                <ReportsLineChart
                  color="dark"
                  title="completed tasks"
                  description="Last Campaign Performance"
                  date="just updated"
                  chart={tasks}
                />
              </MDBox>
            </Grid>
          </Grid>
        </MDBox>
        <MDBox>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6} lg={8}>
              <Projects />
            </Grid>
            <Grid item xs={12} md={6} lg={4}>
              <OrdersOverview />
            </Grid>
          </Grid>
        </MDBox>
      </MDBox>
      <Footer />
    </DashboardLayout>
  );
}

export default Dashboard;
