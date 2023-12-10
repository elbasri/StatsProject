import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function Results() {
  const { resultId } = useParams();
  const [resultData, setResultData] = useState(null);

  useEffect(() => {
    const fetchResultData = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/results/${resultId}/`);
        setResultData(response.data);
        console.log(response)
      } catch (error) {
        console.error('Error fetching result data:', error.message);
      }
    };

    fetchResultData();
  }, [resultId]);

  if (!resultData) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Results</h1>
      {/* Display result data as needed */}
      <p>Result Text: {resultData.result_text}</p>
      {/* Add more display logic for other result fields */}
    </div>
  );
}

export default Results;
